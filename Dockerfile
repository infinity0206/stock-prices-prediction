FROM python:3.8

RUN pip install pandas
RUN pip install pandas_datareader
RUN pip install statsmodels
RUN pip install matplotlib
RUN pip install u8darts
RUN pip install darts
RUN pip install backtesting
RUN pip install fbprophet

WORKDIR /app