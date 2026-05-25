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
| Embeddings | StandardScaler |
| Modeller | Scikit-learn, XGBoost, TensorFlow/Keras |
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
