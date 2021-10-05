import yfinance as yf
import re

class userSelection:
    """
    Class to get and store user stock selection
    """
    
    def __init__(self, interface_instance):
        self.selected_stocks = []  # list of selected stocks
        
        self.stock_weights = {}
        
        self.interface = interface_instance
        
    def parseStockInputStr(self, stock_str_input):
        parsed_stock_list = stock_str_input.replace(' ', '').upper().split(',')
        return parsed_stock_list
    
    def displaySelectedStocks(self):
        self.interface.displayMessage(f"Current stock selection: {self.selected_stocks}")
    
    def getStocks(self):
        stock_str_input = self.interface.getInput("Input stock ticker name(s) to add: ")
        stock_str_list = self.parseStockInputStr(stock_str_input)
        
        for stock_name in stock_str_list:
            # Check if the stock_ticker is valid
            
            ticker = yf.Ticker(stock_name)
            if ticker.info['regularMarketPrice'] != None:
                self.selected_stocks += [stock_name]
            else:
                self.interface.displayErrorMessage(f"{stock_name} is not a valid stock/ticker")
        
        self.selected_stocks = list(set(self.selected_stocks))
        self.displaySelectedStocks()
        
    def removeStocks(self):
        
        stock_str_input = self.interface.getInput("Input stock ticker name(s) to remove: ")
        stock_str_list = self.parseStockInputStr(stock_str_input)
        
        for stock_name in stock_str_list:
            if stock_name in self.selected_stocks:
                self.selected_stocks.remove(stock_name)
            else:
                self.interface.displayErrorMessage(f"{stock_name} not in selection: {self.selected_stocks}")
        self.displaySelectedStocks()
        

    def getWeights(self):
        
        self.interface.displayMessage(f"Please specify the relative weighting of your portfolio")
            
        def parseWeightsStr(weight_str):
            if re.match("^[0-9]+$", weight_str):
                return float('weight_str')
            else:
                return "Input contains non-numeric character."
        
        # Get weight for each stock
        for stock in self.selected_stocks:
            while True:
                weight_str = self.interface.getInput(f"{stock}: ")
                weight = parseWeightsStr(weight_str)
                if type(weight) == str:
                    self.interface.displayErrorMessage(f"{weight} Please try again.")
                else:
                    self.stock_weights[stock] = weight
                    break
                
        #### Normalize weights ####
        # The normalization method is based on one sided exposure. We will consider longs ans shorts separately 
        # and take the sum of the weights of the larger side to be the denominator
        long_stocks = [stock for stock in self.selected_stocks if self.stock_weights[stock] > 0]
        short_stocks = [stock for stock in self.selected_stocks if self.stock_weights[stock] < 0]
        
        total_long = sum([self.stock_weights[stock] for stock in long_stocks])
        total_short = abs(sum([self.stock_weights[stock] for stock in short_stocks]))
        
        denom = total_long if total_long > total_short else total_short
        
        for stock in self.selected_stocks:
            self.stock_weights[stock] = self.stock_weights[stock]/denom
            
        
        self.interface.displayMessage("The normalized weights of your portfolio are:")
        for stock in self.selected_stocks:
            self.interface.displayMessage(f"{stock}: {self.stock_weights[stock]}")
        
        

                
        
            
        
        
        
    
        
    
            


