from flask import Flask, render_template, request
import pickle
import pandas as pd
import anthropic
import json
import os

app = Flask(__name__)

# Indlæs model og scaler
with open('xgb_model.pkl', 'rb') as f:
    xgb_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

def fortolk_spoergsmaal(spoergsmaal):
    svar = client.messages.create(
        model='claude-haiku-4-5',
        max_tokens=512,
        messages=[{
            'role': 'user',
            'content': f"""Du er en assistent der hjælper Airbnb-udlejere med at sætte den rette pris.

Udtræk følgende information og returner KUN valid JSON uden forklaring eller markdown:
{{
    "room_type": "Entire home/apt" eller "Private room" eller "Shared room",
    "city": "amsterdam", "athens", "barcelona", "berlin", "budapest", "lisbon", "london", "paris", "rome" eller "vienna",
    "person_capacity": antal personer (2-6),
    "bedrooms": antal soveværelser (1-8),
    "dist": distance til centrum i km (1-10),
    "metro_dist": distance til metro i km (0.1-3),
    "host_is_superhost": 0 eller 1,
    "cleanliness_rating": 9,
    "guest_satisfaction_overall": 90,
    "multi": 0,
    "biz": 0,
    "attr_index_norm": 20,
    "rest_index_norm": 10
}}

Standardværdier hvis information mangler:
- room_type: "Private room"
- city: "london"
- person_capacity: 2
- bedrooms: 1
- dist: 3
- metro_dist: 0.5

Brugerens spørgsmål: {spoergsmaal}"""
        }]
    )
    tekst = svar.content[0].text.strip()
    tekst = tekst.replace('```json', '').replace('```', '').strip()
    return json.loads(tekst)

def forudsig_pris(features):
    input_data = {col: 0 for col in columns}

    if features['room_type'] == 'Entire home/apt':
        input_data['room_type_Entire home/apt'] = 1
        input_data['room_shared'] = 0
        input_data['room_private'] = 0
    elif features['room_type'] == 'Private room':
        input_data['room_type_Private room'] = 1
        input_data['room_shared'] = 0
        input_data['room_private'] = 1
    else:
        input_data['room_type_Shared room'] = 1
        input_data['room_shared'] = 1
        input_data['room_private'] = 0

    city_col = f"city_{features.get('city', 'london')}"
    if city_col in input_data:
        input_data[city_col] = 1

    for key in ['person_capacity', 'bedrooms', 'dist', 'metro_dist',
                'host_is_superhost', 'cleanliness_rating',
                'guest_satisfaction_overall', 'multi', 'biz',
                'attr_index_norm', 'rest_index_norm']:
        if key in input_data:
            input_data[key] = features[key]

    input_df = pd.DataFrame([input_data])
    input_scaled = scaler.transform(input_df)
    return xgb_model.predict(input_scaled)[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    resultat = None
    fejl = None
    spoergsmaal = ''

    if request.method == 'POST':
        spoergsmaal = request.form.get('spoergsmaal', '')
        try:
            features = fortolk_spoergsmaal(spoergsmaal)
            pris = forudsig_pris(features)
            resultat = {
                'pris': round(pris),
                'by': features.get('city', 'london').capitalize(),
                'boligtype': features['room_type'],
                'personer': features['person_capacity'],
                'sovevaerelser': features['bedrooms'],
                'dist': features['dist']
            }
        except Exception as e:
            fejl = str(e)

    return render_template('index.html', resultat=resultat, fejl=fejl, spoergsmaal=spoergsmaal)

if __name__ == '__main__':
    app.run(debug=True)
