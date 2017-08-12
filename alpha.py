import requests
from pytz import utc
from datetime import datetime
from pymongo import MongoClient

# API key is: 21ZE87MV4RDEZS40

# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=VIXY&interval=1min&outputsize=full&apikey=21ZE87MV4RDEZS40

client = MongoClient()
database = client['stock']
#collection = database['svxy_intra']
collection = database['x_daily']

#stock_info = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SVXY&interval=1min&outputsize=full&apikey=21ZE87MV4RDEZS40').json()
stock_info = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=X&outputsize=full&apikey=21ZE87MV4RDEZS40').json()


interval = "Time Series (Daily)"
count = 0
for i in stock_info[interval]:
    count += 1
    #timestamp = datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
    timestamp = datetime.strptime(i, "%Y-%m-%d")
    open_price = stock_info[interval][str(i)]["1. open"]
    high_price = stock_info[interval][str(i)]["2. high"]
    low_price = stock_info[interval][str(i)]["3. low"]
    close_price = stock_info[interval][str(i)]["4. close"]
    volume = stock_info[interval][str(i)]["5. volume"]
    fl_open = float(open_price)
    fl_high = float(high_price)
    fl_low = float(low_price)
    fl_close = float(close_price)
    int_volume = int(volume)
    avg_price= (fl_open + fl_high + fl_low + fl_close) / 4
    collection.insert({
        'date': timestamp,
        'avg_price': avg_price,
        'open': fl_open,
        'high': fl_high,
        'low': fl_low,
        'close': fl_close,
        'volume': volume
    })
    print(timestamp, avg_price, volume)

print("All done")
print(count)