import pandas as pd

df = pd.read_csv('data/covid-19/pcr_positive_daily.csv', delimiter=",")

from darts import TimeSeries
series = TimeSeries.from_dataframe(df, time_col='日付', value_cols='PCR 検査陽性者数(単日)')

# ここでtraining setとtest setに分割
train, val = series.split_after(pd.Timestamp('20200810'))

from darts.models import ExponentialSmoothing
model = ExponentialSmoothing()
model.fit(train) 
prediction = model.predict(len(val))

import matplotlib.pyplot as plt

series.plot(label='actual', lw=3)
prediction.plot(label='forecast', lw=3)
plt.legend()
plt.xlabel('Year')

from darts.models.prophet import Prophet
models = [ExponentialSmoothing(), Prophet()]
backtests = [model.backtest(series,
                            start=pd.Timestamp('20200810'),
                            forecast_horizon=3)
             for model in models]

from darts.metrics import mape, rmse
for i, m in enumerate(models):
    err = rmse(backtests[i], series)
    backtests[i].plot(lw=3, label='{}, RMSE={:.2f}'.format(m, err))
plt.title('Predictive verification of 3 methods')
plt.legend()

plt.savefig("result2_pcr_positive_daily.png", bbox_inches='tight', dpi=120)