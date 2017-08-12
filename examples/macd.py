import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import math
import pickle

#tickers = ["MMM","ABT","ABBV","ACN","ATVI","AYI","ADBE","AMD","AAP","AES","AET","AMG","AFL","A","APD","AKAM","ALK","ALB","ARE","ALXN","ALGN","ALLE","AGN","ADS","LNT","ALL","GOOGL","GOOG","MO","AMZN","AEE","AAL","AEP","AXP","AIG","AMT","AWK","AMP","ABC","AME","AMGN","APH","APC","ADI","ANDV","ANSS","ANTM","AON","AOS","APA","AIV","AAPL","AMAT","ADM","ARNC","AJG","AIZ","T","ADSK","ADP","AN","AZO","AVB","AVY","BHGE","BLL","BAC","BK","BCR","BAX","BBT","BDX","BRK.B","BBY","BIIB","BLK","HRB","BA","BWA","BXP","BSX","BMY","AVGO","BF.B","CHRW","CA","COG","CPB","COF","CAH","CBOE","KMX","CCL","CAT","CBG","CBS","CELG","CNC","CNP","CTL","CERN","CF","SCHW","CHTR","CHK","CVX","CMG","CB","CHD","CI","XEC","CINF","CTAS","CSCO","C","CFG","CTXS","CLX","CME","CMS","COH","KO","CTSH","CL","CMCSA","CMA","CAG","CXO","COP","ED","STZ","COO","GLW","COST","COTY","CCI","CSRA","CSX","CMI","CVS","DHI","DHR","DRI","DVA","DE","DLPH","DAL","XRAY","DVN","DLR","DFS","DISCA","DISCK","DISH","DG","DLTR","D","DOV","DOW","DPS","DTE","DRE","DD","DUK","DXC","ETFC","EMN","ETN","EBAY","ECL","EIX","EW","EA","EMR","ETR","EVHC","EOG","EQT","EFX","EQIX","EQR","ESS","EL","ES","RE","EXC","EXPE","EXPD","ESRX","EXR","XOM","FFIV","FB","FAST","FRT","FDX","FIS","FITB","FE","FISV","FLIR","FLS","FLR","FMC","FL","F","FTV","FBHS","BEN","FCX","GPS","GRMN","IT","GD","GE","GGP","GIS","GM","GPC","GILD","GPN","GS","GT","GWW","HAL","HBI","HOG","HRS","HIG","HAS","HCA","HCP","HP","HSIC","HSY","HES","HPE","HLT","HOLX","HD","HON","HRL","HST","HPQ","HUM","HBAN","IDXX","INFO","ITW","ILMN","IR","INTC","ICE","IBM","INCY","IP","IPG","IFF","INTU","ISRG","IVZ","IRM","JEC","JBHT","SJM","JNJ","JCI","JPM","JNPR","KSU","K","KEY","KMB","KIM","KMI","KLAC","KSS","KHC","KR","LB","LLL","LH","LRCX","LEG","LEN","LVLT","LUK","LLY","LNC","LKQ","LMT","L","LOW","LYB","MTB","MAC","M","MRO","MPC","MAR","MMC","MLM","MAS","MA","MAT","MKC","MCD","MCK","MDT","MRK","MET","MTD","MGM","KORS","MCHP","MU","MSFT","MAA","MHK","TAP","MDLZ","MON","MNST","MCO","MS","MOS","MSI","MYL","NDAQ","NOV","NAVI","NTAP","NFLX","NWL","NFX","NEM","NWSA","NWS","NEE","NLSN","NKE","NI","NBL","JWN","NSC","NTRS","NOC","NRG","NUE","NVDA","ORLY","OXY","OMC","OKE","ORCL","PCAR","PKG","PH","PDCO","PAYX","PYPL","PNR","PBCT","PEP","PKI","PRGO","PFE","PCG","PM","PSX","PNW","PXD","PNC","RL","PPG","PPL","PX","PCLN","PFG","PG","PGR","PLD","PRU","PEG","PSA","PHM","PVH","QRVO","PWR","QCOM","DGX","RRC","RJF","RTN","O","RHT","REG","REGN","RF","RSG","RMD","RHI","ROK","COL","ROP","ROST","RCL","CRM","SCG","SLB","SNI","STX","SEE","SRE","SHW","SIG","SPG","SWKS","SLG","SNA","SO","LUV","SPGI","SWK","SPLS","SBUX","STT","SRCL","SYK","STI","SYMC","SYF","SNPS","SYY","TROW","TGT","TEL","FTI","TXN","TXT","TMO","TIF","TWX","TJX","TMK","TSS","TSCO","TDG","TRV","TRIP","FOXA","FOX","TSN","UDR","ULTA","USB","UA","UAA","UNP","UAL","UNH","UPS","URI","UTX","UHS","UNM","VFC","VLO","VAR","VTR","VRSN","VRSK","VZ","VRTX","VIAB","V","VNO","VMC","WMT","WBA","DIS","WM","WAT","WEC","WFC","HCN","WDC","WU","WRK","WY","WHR","WFM","WMB","WLTW","WYN","WYNN","XEL","XRX","XLNX","XL","XYL","YUM","ZBH","ZION","ZTS"]
tickers = ["FB", "IBM", "HD"]
#tick = "AMD"

#names = [tick]
winners = []

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

for tick in tickers:
    px = pd.DataFrame()
    try:
        names = [tick]
        px = pd.DataFrame({n: get_px(n, '8/6/2016', '8/6/2017') for n in names})
    except Exception as e:
        print("broken")
        continue
    else:
        print("All good")


    px['26 ema'] = pd.ewma(px[tick], span=26)
    px['12 ema'] = pd.ewma(px[tick], span=12)
    px['MACD'] = (px['12 ema'] - px['26 ema'])
    px['Signal'] = pd.ewma((px['12 ema'] - px['26 ema']), span=9)
    px['Diff'] = (px['MACD'] - px['Signal'])

    diff_list = []
    price_list = []
    date_list = []
    diff_list = px['Diff']
    price_list = px[tick]
    date_list = px.index.values
    macd_list = px['MACD']

    temp_dif = 0
    beg_balance = 10000
    beg_position = math.floor(beg_balance / price_list[0])
    position = beg_position
    test_balance = beg_balance
    test_balance -= beg_position * price_list[0]


    exp_balance = beg_balance
    exp_balance -= position * price_list[0]

    counter = 0


    print(date_list[0])

    for i in diff_list:
        if counter > 1:
            check_cross = temp_dif * i
            if check_cross < 0:
                if macd_list[counter] <= -0.5:
                    buy_amt = math.floor(exp_balance / price_list[counter])
                    if buy_amt > 0:
                        position += buy_amt
                        exp_balance -= buy_amt * price_list[counter]
                        print("buy balance:" + str(exp_balance) + " | " + str(date_list[counter]))
                if position > 0 and macd_list[counter] >= 0.5:
                    exp_balance += position * price_list[counter]
                    position -= position
                    print("sell balance:" + str(exp_balance) + " | " + str(date_list[counter]) +
                          " BnH: " + str(test_balance + (beg_position * price_list[counter])))
        counter += 1
        temp_dif = i

    if position > 0:
         exp_balance += position * price_list[counter - 1]

    test_balance += beg_position * price_list[counter -1]
    test_percent = (test_balance - beg_balance) / beg_balance
    exp_percent = (exp_balance - beg_balance) / beg_balance
    result = exp_balance - test_balance


    print("\nMACD balance:" + str(exp_balance))
    print("MACD strategy percent increase: " + str(exp_percent) + "\n")
    print("Buy and Hold balance: " + str(test_balance))
    print("Buy and Hold percent increase: " + str(test_percent) + "\n")
    print("Delta between buy and hold and MACD strategy (balances): " + str(result))
    print("Delta between buy and hold and MACD strategy (percent): " + str(exp_percent - test_percent) + "\n")


    if exp_percent > test_percent and exp_percent > 0.0:
        win = {}
        win = {"stock": tick, "MACD %": exp_percent, "BnH %": test_percent}
        winners.append(win)

for i in winners:
    print(i)

with open('winners.pickle', 'wb') as f:
    pickle.dump(winners, f)

# stock_plot = px.plot(y=['FB'], title='FB')
# macd_plot = px.plot(y=['MACD', 'Signal'], title='MACD')

# plt.show(block=True)
