import joblib

# STEP 1: load files
model = joblib.load("aqi_model.pkl")
scaler = joblib.load("scaler.pkl")

# STEP 2: sample input
sample_input = [[18.52, 73.85, 20, 150]]

# STEP 3: scale input
sample_scaled = scaler.transform(sample_input)

# STEP 4: predict
prediction = model.predict(sample_scaled)

print("Predicted AQI (pollutant_avg):", prediction[0])
