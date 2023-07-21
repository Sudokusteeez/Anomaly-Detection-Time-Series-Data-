import pandas as pd
import matplotlib.pyplot as plt

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import QuantileAD

data = pd.read_csv("monthly_gas_csv .csv")
data["Date"] = pd.to_datetime(data["Month"])
data = data.set_index("Date") #month is replaceable with whatever we want to be the center point
data = data ["Price"] #depends on dataset 


quantile_detector = QuantileAD(low=.01, high=.99)
anomalies = quantile_detector.fit_detect(data) #Trains the data
plot(data, anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
plt.show()


print(data)