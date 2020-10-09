import pandas_datareader.data as pdr
import datetime

end = datetime.date.today()
start = end - datetime.timedelta(days=5000)

pd_data = pdr.DataReader('SNE', 'iex', start, end)

print(pd_data)
pd_data.to_csv("/app/data.csv")