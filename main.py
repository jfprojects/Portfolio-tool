import sys

from dataManager import stockDataManager
from userSettings import userSelection
from interface import consoleInterface
from portfolio import portfolio


interface = consoleInterface()
stock_data_manager = stockDataManager()
user = userSelection(interface)
active_portfolio = portfolio()
    
interface.displayMessage("Welcome to the portfolio construction tool!")
interface.displayMessage(
"""STEP 1
Please select the stocks for your porfotio. Use the following commands make your edits.

1: Add stock ticker/symbol(s), separate with ',' 
2: Remove stock ticker/symbol(s), separate with ','
3: Finished selecting stocks, move onto next step
4: Exit program

Note: Tickers/symbols are unique series of letters assigned to a security for trading. Please input in uppercase."""
)
    
while True:
    selection = interface.getInput("Please type command: '1', '2', '3', or '4'")
    if selection == '1':
        user.getStocks()
        
    elif selection == '2':
        user.removeStocks()
        
    elif selection == '3':
        interface.displayMessage("Finished selecting stocks, moving onto portfolio weights.")
        break
        
    elif selection == '4':
        interface.displayMessage("Exiting the program")
        sys.exit()
        
    else:
        interface.displayErrorMessage(f"'{selection}' is not valid, must choose from '1', '2', or '3'")

"""
STEP 2
Specify the weights for your potfolio
"""
user.getWeights()
    
    
    