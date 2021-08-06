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
        
    
    def processYahooData(self, df):
        """
        df (dataframe): raw yahoo dataframe
        returns: processed dataframe
        """
        df['Dividends'] = df['Dividends']/df['Close']  # Convert dividends to percent
        df = df.drop('Stock Splits', axis=1)
        return df
        
        
    def getYahooData(self, ticker, start, end):
        """
        ticker (str): stock ticker
        returns: raw yahoo dataframe

        """
        ticker = yf.Ticker(ticker)
        df = ticker.history(start=start, end=end)
        return df
    
    
    def getStockCharacteristics(self, ticker):
        """
        ticker (str): stock ticker
        returns: dictionary of stock characteristics
        """
        ticker = yf.Ticker(ticker)
        info = ticker.info
        
        characteristics = {
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
        
