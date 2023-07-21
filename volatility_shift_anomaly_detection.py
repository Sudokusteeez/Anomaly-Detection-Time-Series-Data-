import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import VolatilityShiftAD

data = yf.download("C")['Open']

data = validate_series(data)


volatility_shift_ad = VolatilityShiftAD(c=1.0, side='positive', window=30)
anomalies = volatility_shift_ad.fit_detect(data)
plot(data, anomaly_tag="marker", anomaly=anomalies, anomaly_color='red')


print(data)