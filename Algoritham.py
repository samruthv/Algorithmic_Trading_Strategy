#In this program we will usae the dual moving average crossover to determine when to buy and sell stock
import pandas as pd
import numpy as np
import datetime as datetime
import matplotlib.pyplot as plt


#Load Data
fb = pd.read_csv('FB.csv')

#Visualize Data
plt.figure(figsize=(12.5,4.5))
plt.plot(fb['Adj Close'], label='FB')
plt.title('FB Adjusted Close Price History')
plt.xlabel('2010-09-15 to 2021-05-19')
plt.ylabel('Adjusted Closed Price')
plt.legend(loc='upper left')
plt.show()

#Create the simple moving average with 30 day window
sma30 = pd.DataFrame()
sma30['Adj Close'] = fb['Adj Close'].rolling(window= 30).mean()
sma30

#Create a simple moving 100 day average 
sma100 = pd.DataFrame()
sma100['Adj Close'] = fb['Adj Close'].rolling(window= 100).mean()
sma100

#Visualizations
plt.figure(figsize=(12.5,4.5))
plt.plot(fb['Adj Close'], label='FB')
plt.plot(sma30['Adj Close'], label='SMA30')
plt.plot(sma100['Adj Close'], label='SMA100')
plt.title('FB Adjusted Close Price History')
plt.xlabel('2010-09-15 to 2021-05-19')
plt.ylabel('Adjusted Closed Price')
plt.legend(loc='upper left')
plt.show()

#Create a new DF to store data
data = pd.DataFrame()
data['fb'] = fb['Adj Close']
data['sma30'] = sma30['Adj Close']
data['sma100'] = sma100['Adj Close']
data

#Create a function to signal when to buy and sell a stock

def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1
    
    for i in range(len(data)):
        if data['sma30'][i] > data['sma100'][i]:
            if flag != 1:
                sigPriceBuy.append(data['fb'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['sma30'][i] < data['sma100'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['fb'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
                
    return (sigPriceBuy, sigPriceSell)

#Storing buy and sell data into variables

buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]
data


#Visualitaion of our algoritham
plt.figure(figsize=(12.6, 4.6))
plt.plot(data['fb'], label=['FB'], alpha = 0.35)
plt.plot(data['sma30'], label=['SMA30'], alpha = 0.35)
plt.plot(data['sma100'], label=['SMA100'], alpha = 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label='Buy', marker='^', color='green')
plt.scatter(data.index, data['Sell_Signal_Price'], label='Sell', marker='v', color='red')
plt.title('Facebook Buy Sell Signals')
plt.xlabel('2010-09-15 to 2021-05-19')
plt.ylabel('Adj. Closed Price USD ($)')
plt.legend(loc='upper left')
plt.show()


            
                
                
                
