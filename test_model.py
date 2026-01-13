import joblib
import pandas as pd

model = joblib.load("aqi_model.pkl")
scaler = joblib.load("scaler.pkl")

sample_input = pd.DataFrame(
    [[17.52, 76.20, 60, 220]],
    columns=["latitude", "longitude", "pollutant_min", "pollutant_max"]
)

sample_scaled = scaler.transform(sample_input)
prediction = model.predict(sample_scaled)

print("Predicted AQI (pollutant_avg):", prediction[0])
