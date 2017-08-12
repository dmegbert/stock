from pymongo import MongoClient
from bitcoin_price_prediction.bayesian_regression import *
import warnings
import pickle


client = MongoClient()
database = client['stock']
collection = database['x_daily']

collection = database['svxy_intra']



warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")
np.seterr(divide='ignore', invalid='ignore')

# Retrieve price, v_ask, and v_bid data points from the database.
prices = []
dates =[]
#v_ask = []
#v_bid = []
#num_points = 777600
#for doc in collection.find().limit(num_points):
for doc in collection.find():
    prices.append(doc['close'])
    dates.append(doc['date'])
    #v_ask.append(doc['v_ask'])
    #v_bid.append(doc['v_bid'])

prices = prices[::-1]
dates = dates[::-1]

# Divide prices into three, roughly equal sized, periods:
# prices1, prices2, and prices3.
[prices1, prices2, prices3] = np.array_split(prices, 3)
[dates1, dates2, dates3] = np.array_split(dates, 3)


with open('dps_svxy_intra.pickle', 'rb') as f:
    dps = pickle.load(f)

print(min(dps))
print(max(dps))

for i in range(50, len(prices3) - 1):
     print("thresh:" + str(dps[i-50]) + " | " + str(prices3[i]) + " date:" + str(dates3[i]))

thresh = 0.001
pnl = []
for i in range(1, 100):
    bank_balance = evaluate_performance(prices3, dates3, dps, t=thresh, step=1)
    pnl.append(bank_balance)
    thresh += 0.0001
    print(thresh)

print(pnl)