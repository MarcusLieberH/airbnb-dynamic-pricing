# airbnb-dynamic-pricing

# Dynamic Pricing Model — Airbnb Europæiske Byer

## Problembeskrivelse
Airbnb-udlejere har svært ved at sætte den rigtige pris for deres bolig.
Sætter de prisen for høj, får de ingen bookinger.
Sætter de den for lav, mister de indtægt.

Dette projekt bygger en ML-model der kan forudsige en fair pris for en
Airbnb-bolig baseret på boligens karakteristika — såsom by, boligtype,
antal soveværelser og afstand til centrum.

## Datasæt
**Airbnb Prices in European Cities** fra Kaggle.
- 10 europæiske byer: Amsterdam, Athen, Barcelona, Berlin, Budapest, Lissabon, London, Paris, Rom og Wien
- 51.571 boliger i alt
- Kilde: https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities

## Metode
Vi træner og sammenligner 3 modeller:
1. **Linear Regression** — simpel baseline model
2. **Deep Neural Network (DNN)** — neural netværk med 3 skjulte lag
3. **XGBoost** — tree-based model

Bygget med Anthropic Claude API + XGBoost model.

## Teknologi
| Komponent | Bibliotek |
|---|---|
| Data | Pandas |
| Numeriske beregninger | NumPy |
| Dataskalering | Scikit-learn (StandardScaler) |
| Linear Regression | Scikit-learn (LinearRegression) |
| DNN | TensorFlow / Keras |
| XGBoost | XGBoost |
| Visualisering | Matplotlib |
| AI Chat | Anthropic Claude Haiku |
| Miljø | Google Colab |
## Kode
Notebook: `EksamensOpgave_i_ML.ipynb`

GitHub: https://github.com/MarcusLieberH/airbnb-dynamic-pricing

## Resultater

### Modelsammenligning
| Model | RMSE | R² |
|---|---|---|
| Linear Regression | 132 kr. | 0.55 |
| DNN | 110 kr. | 0.69 |
| **XGBoost** | **103 kr.** | **0.73** |

XGBoost er den bedste model — lavest fejl og højest R².

### Hvad påvirker prisen mest?
De vigtigste faktorer ifølge XGBoost:
- **By** (Amsterdam, Budapest, Rom) — har størst indflydelse på prisen
- **Antal soveværelser** — mere plads = højere pris
- **Boligtype** — helt hjem koster mere end privat værelse

### Ekstra — Chat med AI
Projektet inkluderer en chat-løkke hvor udlejere kan stille spørgsmål
på naturligt dansk og få en prisforudsigelse tilbage.

Eksempel:






### Train/test split:
<img width="711" height="315" alt="image" src="https://github.com/user-attachments/assets/3fe95c4b-f188-4207-aa52-23521ff6514a" />

###  Linear Regression og XGBoost
<img width="936" height="734" alt="image" src="https://github.com/user-attachments/assets/85fc0cd4-2e64-4e08-b9c1-e28028b24f4b" />

### DNN træningen.
<img width="785" height="845" alt="image" src="https://github.com/user-attachments/assets/d43192e8-b3fa-4711-815d-f3690c9b3d97" />

### Output fra Optuna celle
<img width="1622" height="710" alt="image" src="https://github.com/user-attachments/assets/8e77e949-3df9-470d-bbc4-e9e32817edc3" />
<img width="914" height="395" alt="image" src="https://github.com/user-attachments/assets/fd07910e-79d5-4a41-bbed-041f5ff206d7" />


### Feature importance grafen
<img width="1116" height="656" alt="image" src="https://github.com/user-attachments/assets/e4f881ba-cc43-4f69-942b-5f1ae9e5bc07" />

### Sammenligning af modellerne
<img width="530" height="474" alt="image" src="https://github.com/user-attachments/assets/b6dd0842-99ca-43b3-9b9b-3092c8f46abb" />


### RMSE og R² graferne 
<img width="1179" height="785" alt="image" src="https://github.com/user-attachments/assets/683ccf37-4882-486b-aeda-2027b553b4b3" />

### Claude til at fortolke udlejerens spørgsmål
<img width="1140" height="675" alt="image" src="https://github.com/user-attachments/assets/a4801f58-c664-4920-94a0-7b5733d753f3" />



## Web App
Projektet inkluderer også en Flask web app (`app.py`) der kører modellen lokalt via en browser.

<img width="943" height="639" alt="image" src="https://github.com/user-attachments/assets/d3de6d23-573e-4ee1-a693-9f91a7b5732a" />
