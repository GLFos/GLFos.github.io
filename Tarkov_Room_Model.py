#This is a simple model meant to give an estimate on how many raids it may take to earn back the value of a keycard.
#It uses user input since the values in other documents can be inaccurate within the coming days or weeks.

keycard_color = input("Enter the keycard color: ")
keycard_value = float(input("Enter the keycard value: "))
avg_profit = float(input("Enter the average profit per raid: "))

#Determines if the Flea Market was used.
use_flea_market = input("Do you want to use the Flea Market? (yes:no): ")
if use_flea_market.lower() == 'yes':
    avg_profit *= 1.4
else: 
    avg_profit *= 1

# Calculate the rough number of raids needed to pay off the keycard
raids_needed = keycard_value / avg_profit

# Output the result
print(f"It will take approximately {raids_needed:.2f} raids to earn back the {keycard_color} keycard, assuming an average profit of {avg_profit:.2f}.")
