import datetime as dt
import yfinance as yf
import mysql.connector

class stockDataManager:
    """
    Manage stock historical prices and stock information
    """
    def __init__(self):
        
        self.db = mysql.connector.connect(host='localhost',
                                          user='jerry',
                                          password='Mrpopper5',
                                          db = '')
        
        self.date = dt.datetime.now().strftime("%m/%d/%Y")
        self.hour = dt.datetime.now().hour
        
        self.max_daily_queries = 1000
        self.max_hourly_queries = 100
        
    
    def getYahooData(self, ticker_name, start, end):
        """
        ticker_name (str): stock ticker
        returns: raw yahoo dataframe

        """
        ticker = yf.Ticker(ticker_name)
        df = ticker.history(start=start, end=end)
        return df
    
    
    def processYahooData(self, df, ticker_name):
        """
        df (dataframe): raw yahoo dataframe
        returns: processed dataframe
        """
        df['r'] = (df['Close'] - df['Close'].shift(1))/df['Close'].shift(1)
        df['Dividends_percent'] = df['Dividends']/df['Close']  # Convert dividends to percent
        df = df.drop('Stock Splits', axis=1)
        df['ticker'] = ticker_name
        return df
        
    
    def getStockCharacteristics(self, ticker_name):
        """
        ticker_name (str): stock ticker
        returns: dictionary of stock characteristics
        """
        ticker = yf.Ticker(ticker_name)
        info = ticker.info
        
        characteristics = {
            'ticker': ticker_name,
            'sector': info['sector'],
            'industry': info['industry'],
            'country': info['country'],
            'dividend_yield': info['fiveYearAvgDividendYield'],
            'market_cap': info['marketCap'],
            'net_income': info['netIncomeToCommon'],
            'recommendation': info['recommendationKey'],
            'employees': info['fullTimeEmployees'],
            'exchange': info['exchange']
        }
        return characteristics
    
        
class userDataManager:
    """
    Manager user profile information
    """
    def __init(self):
        self.db = mysql.connector.connect(host='localhost',
                                          user='jerry',
                                          password='Mrpopper5',
                                          db = '')
        
