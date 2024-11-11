from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
def adf(data):
    result = adfuller(data)
    print(f'The ADF statistic is {result[0]}')
    print(f"The p-value: {result[1]}")
def acf_pacf(data,symbol):
    fig, (ax1,ax2)= plt.subplots(2,1, figsize=(12,8))
    plot_acf(data,ax=ax1)
    ax1.set_title(f"{symbol}'s ACF plot")
    plot_pacf(data,ax=ax2)
    ax2.set_title(f"{symbol}'s PACF plot")

def plot_difference(data,symbol,type):
    if type=='acf':
        diff = data['Close'].diff().dropna()
        diff2=diff.diff().dropna()
        fig, (ax1,ax2,ax3) = plt.subplots(3,1,figsize=(12,8))
        plot_acf(data,ax=ax1)
        ax1.set_title(f"{symbol}'s original ACF plot ")
        plot_acf(diff,ax=ax2)
        ax2.set_title(f"{symbol}'s ACF plot after differencing once")
        plot_acf(diff2,ax=ax3)
        ax3.set_title(f"{symbol}'s ACF plot after differencing twice")
        plt.subplots_adjust(wspace=0.5, hspace=0.5) 
        plt.show()
    elif type =='pacf':
        diff = data['Close'].diff().dropna()
        diff2=diff.diff().dropna()
        fig, (ax1,ax2,ax3) = plt.subplots(3,1,figsize=(12,8))
        plot_pacf(data,ax=ax1)
        ax1.set_title(f"{symbol}'s original PACF plot ")
        plot_pacf(diff,ax=ax2)
        ax2.set_title(f"{symbol}'s PACF plot after differencing once")
        plot_pacf(diff2,ax=ax3)
        ax3.set_title(f"{symbol}'s PACF plot after differencing twice")
        plt.subplots_adjust(wspace=0.5, hspace=0.5)  
        plt.show()
