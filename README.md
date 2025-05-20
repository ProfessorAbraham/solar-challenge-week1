# Solar Challenge Week 1

Project for 10 Academy - AIM Week 0.

## Exploratory Data Analysis (EDA)

This project includes comprehensive exploratory data analysis on solar farm datasets from three countries: **Benin**, **Sierra Leone**, and **Togo**. The goal is to profile, clean, and understand the data to prepare it for subsequent cross-country comparisons and region-ranking tasks.

### Key Features

- **Summary Statistics & Missing Value Report:**  
  Descriptive statistics on all numeric columns and identification of columns with significant missing values (>5%).

- **Outlier Detection & Cleaning:**  
  Identification of outliers using Z-scores on key solar and sensor measurements (GHI, DNI, DHI, ModA, ModB, WS, WSgust). Missing values are handled by median imputation or row removal as appropriate.

- **Time Series Analysis:**  
  Visualizations of solar irradiance and temperature variables over time, highlighting seasonal trends and anomalies.

- **Cleaning Impact Analysis:**  
  Comparison of sensor readings before and after cleaning.

- **Correlation & Relationship Analysis:**  
  Heatmaps and scatter plots to investigate relationships between variables such as wind speed/direction, humidity, and solar irradiance.

- **Wind & Distribution Analysis:**  
  Wind rose plots and histograms exploring wind behavior and solar variable distributions.

- **Temperature & Humidity Interactions:**  
  Analysis of how relative humidity affects temperature and solar radiation.

- **Bubble Charts:**  
  Multi-variable visualizations to show relationships between solar irradiance, temperature, and humidity or barometric pressure.

### How to Run

1. Make sure you have the required Python environment set up. Install dependencies from:
   ```bash
   pip install -r requirements.txt
   ```
