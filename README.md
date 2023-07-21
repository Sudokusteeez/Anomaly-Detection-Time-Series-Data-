# Anomaly-Detection-Time-Series-Data

Overview
This repository showcases my skills in anomaly detection using time series data and Python. The project demonstrates various anomaly detection techniques applied to monthly gas price data obtained from a CSV file. The analysis involves using the adtk (Anomaly Detection Toolkit) library along with other popular libraries like pandas, matplotlib, and yfinance.

Key Features
Utilizes Python to read, process, and analyze time series data.
Implements three different anomaly detection techniques: Threshold-based Anomaly Detection, Quantile-based Anomaly Detection, and Volatility Shift-based Anomaly Detection.
Demonstrates data visualization using matplotlib to visualize detected anomalies.
Uses external data source for demonstration (monthly gas price data from a CSV file).

Requirements
Python 3.x
Libraries: pandas, matplotlib, yfinance, adtk

Instructions
Install the required libraries:

pip install pandas matplotlib yfinance adtk

Download the dataset: monthly_gas_csv.csv and place it in the "data" folder of the repository.
Run the Jupyter notebooks or Python scripts to see the anomaly detection techniques in action.

Usage
Threshold-based Anomaly Detection:

File: threshold_anomaly_detection.py
Description: This script applies threshold-based anomaly detection on the monthly gas price data.
Output: A plot with detected anomalies marked in red.
Quantile-based Anomaly Detection:

File: quantile_anomaly_detection.py
Description: This script uses quantile-based anomaly detection to identify anomalies in the time series data.
Output: A plot with detected anomalies marked in red.
Volatility Shift-based Anomaly Detection:

File: volatility_shift_anomaly_detection.py
Description: This script applies volatility shift-based anomaly detection on the monthly gas price data.
Output: A plot with detected anomalies marked in red.


Disclaimer
This repository is intended for educational and demonstrative purposes. The anomaly detection techniques and data used may not be suitable for real-world cybersecurity applications without further refinement and domain-specific considerations.

License
MIT License

# Enhancements:

The script has also been modified locally to include Interquartile anomalies and Persistent anomalies that persist over time. 
