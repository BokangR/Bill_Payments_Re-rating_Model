#!/usr/bin/env python
# coding: utf-8

# In[46]:


#The fee structure should be determined for bill payment transactions.

fee_structure = [


{"range": (0, 9.99), "fee": 0},

{"range": (10, 50), "fee": 1.97},

{"range": (51, 100), "fee": 3.21},

{"range": (101, 250), "fee": 4.86},

{"range": (251, 500), "fee": 6.42},

{"range": (501, 1000), "fee":8.72},

{"range": (1001,2000),"fee" :13.44 },

{"range": (2001,3000), "Fee" :13.44 },

{"range": (3001,4000), "Fee": 13.44 },

{"range": (4001,5000), "Fee" :13.44},

{"range": (5001, 50000), "fee": 0.35, "is_percentage": True},
   
{"range": (50001, float('infinity')), "fee": 0.38, "is_percentage": True}

]

# This function calculates the transaction fee rate.

def calculate_fee_rate(transaction_amount):
    
    transaction_amount = int(transaction_amount)
    # Loop through the fee structure to find the applicable fee rate

    for fee_entry in fee_structure:

        min_amount, max_amount = fee_entry["range"]

        # Check if transaction amount falls within the current range

        if min_amount <= transaction_amount <= max_amount:

            # Check if the fee is a percentage or a fixed amount

            if "is_percentage" in fee_entry and fee_entry["is_percentage"]:

                return transaction_amount * (fee_entry["fee"] /100)   # Calculate percentage fee

            else:

                return fee_entry["fee"]   # Return fixed fee
# if amount of transaction does not falls in any group (impossible in case of full ranges)

    return None

# start of example usage:

# Example usage:

# Prompt user for input
user_input = input("Please enter the transaction amount: ")

try:
    transaction_amount = float(user_input)
    
    calculated_fee = calculate_fee_rate(transaction_amount)
    
except ValueError:
    
    print("Invalid input. Please enter a numeric value.")

# end of example usage

if calculated_fee is not None:

    print(f"Transaction Amount: {transaction_amount}, Calculated Fee: {calculated_fee}")

else:

    print("Error: Transaction amount does not fall within any defined range.")


# In[ ]:




