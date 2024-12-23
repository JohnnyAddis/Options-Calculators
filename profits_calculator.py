#This program calcualted the max-profit, max-loss, and break-even number for options at expiration.

import tkinter as tk


option_type = int(input('What type of Option Order? Long Call, Short Call, Long Put, or Short Put? (O for long call, 1 for long put, 2 for short call, 3 for short put)'))
current_price = input('What is the current price of the underlying asset?')
current_price = float(current_price)
strike_price = input('What is the strike price?')
strike_price = float(strike_price)
premium = input('What is the premium per share you are paying/receiving?')
premium = float(premium)



def calculate_profits(option_type, current_price, strike_price, premium):
    if(option_type == 0):
        max_profit = "Unlimited"
        max_loss = premium*100
        break_even = strike_price + premium
    elif(option_type==1):
        max_profit = (strike_price - premium) * 100
        max_loss = premium * 100
        break_even = strike_price - premium
    elif (option_type ==2):
        max_profit = premium*100
        max_loss = "Unlimited"
        break_even = strike_price + premium
    else:
        max_profit = premium*100
        max_loss = (strike_price-premium) *100
        break_even = strike_price - premium

    #calculate_profits(option_type,  current_price, strike_price, premium)
    if(isinstance(max_profit,float)):
        print(f"Your max profit is: ${max_profit:.2f}.")
    else:
        print("Your max profit is Unlimited.")

    if(isinstance(max_loss,float)):
        print(f"You max loss is ${max_loss:.2f}")
    else:
        print(f"Your max loss is: Unlimited")

    if option_type == 0 or option_type == 3:
        print(f"To make at least 1 cent from the trade, the stock price must be equal to or above ${break_even:.2f} at expiration.")
    else:
        print(f"To make at least 1 cent from the trade, the the stock price must be equal to or below ${break_even:.2f} at expiration.")

calculate_profits(option_type, current_price, strike_price, premium)
