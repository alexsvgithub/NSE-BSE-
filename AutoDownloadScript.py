import webbrowser
import time
import pandas as pd
df=pd.read_csv("NIFTY100.csv")
symbols = df['Symbol']
print(symbols)
#lists = [x for x in symbols]
lists = ['HDFC']
print(lists)
for i in lists:
    #nse data
    link='https://query1.finance.yahoo.com/v7/finance/download/'+i+'.NS?period1=1279929600&period2=1627084800&interval=1d&events=history&includeAdjustedClose=true'
    print(link)
    webbrowser.open(link, new=1)
    time.sleep(0.5)
    #bse data
    link='https://query1.finance.yahoo.com/v7/finance/download/'+i+'.BO?period1=1279929600&period2=1627084800&interval=1d&events=history&includeAdjustedClose=true'
    print(link)
    webbrowser.open(link, new=1)
print("DONE")

#1648524583 - 28-03-2022
