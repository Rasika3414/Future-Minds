Project Name: Air Quality Index (AQI) Prediction System

# Problem Statement

Air pollution is a serious environmental issue that directly affects human health.
This project aims to predict the Air Quality Index (AQI) based on geographical location and pollutant values using Machine Learning techniques.

Predicting AQI in advance helps authorities and citizens to take preventive actions and improve air quality awareness.


# Project Objective

To analyze air pollution data
To build a Machine Learning model for AQI prediction
To predict AQI using minimum and maximum pollutant values
To understand the real-world application of ML in environmental monitoring


# Tools & Technologies Used

Programming Language: Python
Libraries: Pandas, NumPy, Scikit-learn, Joblib
IDE / Platform: Jupyter Notebook, VS Code
Version Control: Git & GitHub


# Dataset Information

The dataset contains air pollution-related parameters such as:
Latitude
Longitude
Minimum pollutant value
Maximum pollutant value
Data Source: Government API (not directly taken from Kaggle)
The data was cleaned and preprocessed before model training.

# Machine Learning Model

Algorithm Used: Regression-based ML Model
Scaler: StandardScaler (used for feature scaling)
The trained model and scaler are saved using Joblib for reuse.


# How the Prediction Works

User provides:
Latitude
Longitude
Pollutant minimum value
Pollutant maximum value
Input data is scaled using the saved scaler
The trained ML model predicts the average AQI value

# Conclusion

This project successfully demonstrates how Machine Learning can be used to predict air quality using real-world data.
It enhances understanding of data preprocessing, model training, and deployment using Python.