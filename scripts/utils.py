import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import seasonal_decompose
class preprocess:
    """
    This class is made to load and preprocess neccessary column of the financial data gathered from yfinance library
    """
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def load_ticker(self,ticker):
        """
        This class will load the mentioned ticker from the yfinance library with the necessary columns

        Parameter:
            - ticker- the ticker or symbol of the stock you want to analyze
        Returns:
            - A pandas dataframe with the neccessary attributes of the stock
        """
        ticker=yf.Ticker(ticker)
        dataset=ticker.history(start='2015-01-01',end='2024-10-31')
        return dataset
    def volatility(self,data):
        """
        This method will computes the 3 neccessary factors for volatility analysis:
        1. Daily percentage change
        2. Rolling means
        3. Rolling standard deviation

        Parameter:
            - data: the data you want to add these columns
        Returns:
            - An updated dataframe with the mentioned columns
        """
        #Calculating percentage change for the closing price
        data['Daily pct change']=data['Close'].pct_change()*100
        #Calculating rolling means with a window size of 14 days(2 weeks)
        data['rolling means']=data['Close'].rolling(window=14).mean()
        #Calculating rolling standard deviation with a window size of 14 days (2 weeks)
        data['rolling std']=data['Close'].rolling(window=14).std()
        return data


class EDA:
    """
    This class mostly consists of visualizations created for datasets
    """
    def __init__(self,data1,data2,data3):
        self.data1=data1
        self.data2=data2
        self.data3=data3
    def plot_close(self):
        """
        This method is used to visualize and compare the closing price of all 3 stocks across the years from
        2015-2024

        - Parameter:
            None
        - Returns:
            Lineplot containing 3 plots for each stock's closing price
        """
        fig=go.Figure()
        fig.add_trace(go.Line(x=self.data1.index,y=self.data1['Close'],name='Tesla'))
        fig.add_trace(go.Line(x=self.data2.index,y=self.data2['Close'],name= 'Vanguard index bonds'))
        fig.add_trace(go.Line(x=self.data3.index,y=self.data3['Close'],name='S&P 500'))
        fig.update_layout(height=600, width=900,title='The closing price of the 3 stocks across the years',xaxis_title='Date',yaxis_title='Closing Price (in $)')
        fig.show()
    def plot_volatility(self,column):
        """
        This method plots the distribution of the volatility indicator for all 3 datasts as a subplot.

        - Parameter:
            column- This column is for the volatility indicator (daily pct change, rolling means or rolling std)
        - Returns:
            Subplots of all 3 datasets
        """
        #Making of the subplots
        figure=make_subplots(rows=3)
        #Tracing each datasets subplot 
        figure.add_trace(go.Line(x=self.data1.index,y=self.data1[column],name='Tesla'),row=1,col=1)
        figure.add_trace(go.Scatter(x=self.data2.index,y=self.data2[column],name= 'Vanguard index bonds'),row=2,col=1)
        figure.add_trace(go.Scatter(x=self.data3.index,y=self.data3[column],name='S&P 500'),row=3,col=1)
        #Customize the layout 
        figure.update_layout(height=700, width=950,title=f'The {column} of all 3 stocks across the years')
        figure.show()
    def outlier_detection(self):
        """
        This method is used to show the boxplot of each stock to investigate the outliers distribution.

        - Parameter:
            None
        - Returns:
            A boxplot for all 3 stock's closing price
        """
        fig=go.Figure()
        fig.add_trace(go.Box(x=self.data1['Close'],name='Tesla'))
        fig.add_trace(go.Box(x=self.data2['Close'],name= 'Vanguard index bonds'))
        fig.add_trace(go.Box(x=self.data3['Close'],name='S&P 500'))
        fig.update_layout(height=600, width=900,title='The box plot of all 3 stocks')
        fig.show()
    def seasonal_decompose(self,data,symbol):
        """
        This method visulalizes the seasonal decompose of these financial time-series datasts. 
        - Parameter:
            data- the specific data you want to seasonally decompose
            symbol- the symbol for the specific stock
        - Returns:
            4 subplots for Observed, Trend, Seasonal and Residuals  
        """
        decomposition = seasonal_decompose(data['Close'], model='additive', period=365)
        #Making of the subplots
        fig = make_subplots(rows=4, cols=1, subplot_titles=['Observed', 'Trend', 'Seasonal', 'Residuals'])

        # Add traces for each component
        fig.add_trace(go.Scatter(x=decomposition.observed.index, y=decomposition.observed), row=1, col=1)
        fig.add_trace(go.Scatter(x=decomposition.trend.index, y=decomposition.trend), row=2, col=1)
        fig.add_trace(go.Scatter(x=decomposition.seasonal.index, y=decomposition.seasonal), row=3, col=1)
        fig.add_trace(go.Scatter(x=decomposition.resid.index, y=decomposition.resid), row=4, col=1)

        #Customize the layout and appearance
        fig.update_layout(height=900, title=f'Seasonal Decomposition for the Closing stock price of {symbol}',  title_x=0.5, showlegend=False)
        fig.show()
