#This program calcualted the max-profit, max-loss, and break-even number for options at expiration.
option_type = int(input('What type of Option Order? Long Call, Short Call, Long Put, or Short Put? (O for long call, 1 for long put, 2 for short call, 3 for short put)'))

current_price = input('What is the current price of the underlying asset?')
current_price = float(current_price)

strike_price = input('What is the strike price?')
strike_price = float(strike_price)

premium = input('What is the premium per share you are paying/receiving?')
premium = float(premium)

max_profit = None
max_loss = None
break_even = None

# def calculate_profits(option_type, current_price, strike_price, premium):
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

print(f"To break even, the price of the underset must be: ${break_even:.2f}.")

