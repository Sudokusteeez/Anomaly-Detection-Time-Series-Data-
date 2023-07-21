import pandas as pd
import matplotlib.pyplot as plt

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import ThresholdAD

data = pd.read_csv("monthly_gas_csv .csv")
data["Date"] = pd.to_datetime(data["Month"])
data = data.set_index("Date") #month is replaceable with whatever we want to be the center point
data = data ["Price"] #depends on dataset 


threshold_detector = ThresholdAD(low=1.5, high=5.75)
anomalies = threshold_detector.detect(data)
plot(data, anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
plt.show()



print(data)