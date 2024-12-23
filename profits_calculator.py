import tkinter as tk
from tkinter import ttk

# Function to calculate profits
def calculate_profits():
    try:
        # Retrieve user inputs
        option_type = option_var.get()
        current_price = float(current_price_entry.get())
        strike_price = float(strike_price_entry.get())
        premium = float(premium_entry.get())
        
       
        max_profit = None
        max_loss = None
        break_even = None

        # Perform calculations based on option type
        if option_type == "Long Call":
            max_profit = "Unlimited"
            max_loss = premium * 100
            break_even = strike_price + premium
        elif option_type == "Long Put":
            max_profit = (strike_price - premium) * 100
            max_loss = premium * 100
            break_even = strike_price - premium
        elif option_type == "Short Call":
            max_profit = premium * 100
            max_loss = "Unlimited"
            break_even = strike_price + premium
        elif option_type == "Short Put":
            max_profit = premium * 100
            max_loss = (strike_price - premium) * 100
            break_even = strike_price - premium

        #
        result_text = ""
        if isinstance(max_profit, float):
            result_text += f"Max Profit: ${max_profit:.2f}\n"
        else:
            result_text += f"Max Profit: Unlimited\n"
        
        if isinstance(max_loss, float):
            result_text += f"Max Loss: ${max_loss:.2f}\n"
        else:
            result_text += f"Max Loss: Unlimited\n"
        
        if option_type in ["Long Call", "Short Put"]:
            result_text += f"Break-Even Price: ${break_even:.2f} (At or Above)\n"
        else:
            result_text += f"Break-Even Price: ${break_even:.2f} (At or Below)\n"

        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text="Please enter valid numeric values for price, strike, and premium.")


root = tk.Tk()
root.title("Options Risk Calculator")

# Dropdown for option type
tk.Label(root, text="Option Type:").grid(row=0, column=0, padx=10, pady=5)
option_var = tk.StringVar(value="Long Call")
option_menu = ttk.Combobox(root, textvariable=option_var, values=["Long Call", "Long Put", "Short Call", "Short Put"], state="readonly")
option_menu.grid(row=0, column=1, padx=10, pady=5)

# Entry for current stock price
tk.Label(root, text="Current Stock Price ($):").grid(row=1, column=0, padx=10, pady=5)
current_price_entry = tk.Entry(root)
current_price_entry.grid(row=1, column=1, padx=10, pady=5)

# Entry for strike price
tk.Label(root, text="Strike Price ($):").grid(row=2, column=0, padx=10, pady=5)
strike_price_entry = tk.Entry(root)
strike_price_entry.grid(row=2, column=1, padx=10, pady=5)

# Entry for premium per share
tk.Label(root, text="Premium per Share ($):").grid(row=3, column=0, padx=10, pady=5)
premium_entry = tk.Entry(root)
premium_entry.grid(row=3, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=calculate_profits)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
