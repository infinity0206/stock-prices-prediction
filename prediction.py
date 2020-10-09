import warnings
warnings.filterwarnings('ignore') # 計算警告を非表示
warnings.simplefilter('ignore')

import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv('/app/data.csv')
tmd = pd.to_datetime(data['date'])
data.index = tmd

columns = "volume"
predictive_counts = 150


counts = len(data["date"])

pred_start = data.index[0]
pred_end = data.index[-1]
focus_start = pred_start
dynamic_start = data.index[counts - predictive_counts]
focus_end = pred_end
focus_time = [pred_start, focus_end]

## open 
model =  sm.tsa.statespace.SARIMAX(data[columns][:], order=(1, 0, 1), trend='c')
result = model.fit(disp=False)

# one-step-ahead forecast
predict = result.get_prediction(start=pred_start, end=pred_end)
predict_ci = predict.conf_int()
predict_mean = predict.predicted_mean

# dynamic prediction
predict_dy = result.get_prediction(start=pred_start, end=pred_end, dynamic = counts - predictive_counts)
predict_dy_ci = predict_dy.conf_int()
predict_dy_mean = predict_dy.predicted_mean

fig, ax = plt.subplots(figsize=(12, 6))

# data[columns].plot(color='red', ax=ax)
data[columns].iloc[:-predictive_counts].plot(color='black', ax=ax)
data[columns].iloc[-predictive_counts:].plot(color='b', ax=ax, alpha=0.5, style="--")

# one-step-ahead forecast
predict_mean.plot(color='r',ax=ax, label='One-step-ahead forecast')
ax.fill_between(predict_ci.index, predict_ci.iloc[:, 0], predict_ci.iloc[:, 1], alpha=0.1)

# dynamic prediction
predict_dy_mean.plot( color='g',ax=ax, label='dynamic forecast')
ax.fill_between(predict_dy_ci.index,  predict_dy_ci.iloc[:, 0], predict_dy_ci.iloc[:, 1], alpha=0.1)

ax.set_xlim(focus_time)
# ax.set_ylim([50, 150])

plt.savefig("result_" + columns + "_" + str(predictive_counts) + ".png", bbox_inches='tight', dpi=120)