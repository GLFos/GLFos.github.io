
import matplotlib.pyplot as plt
from Tarkov_Room_Analysis import averages, profits, keycards

#Lists and iterations for the visual analysis. The rooms value removes the keycard with a blue marking from the group.
#The rooms1 and keycard_costs values iterate through the entire keycard list, assigning values and rooms. 
rooms = ['Red Keycard', 'Violet Keycard', 'Black Keycard', 'Blue Keycard', 'Green Keycard']
rooms1 = list(keycards.keys())
keycard_costs = list(keycards.values())

#Graph comparing the average profit each room made over 30 raids
plt.bar(rooms1, averages, color=['red', 'purple', 'black', 'blue', 'lightblue', 'green'])
plt.title('Average Profit of Each Room per Raid')
plt.xlabel('Keycard Rooms')
plt.ylabel('Average Profit in Roubles')
plt.show()

#Graph comparing the total profits of each room over 30 raids
plt.bar(rooms1, profits, color=['red', 'purple', 'black', 'blue', 'lightblue', 'green'])
plt.title('Individual Room Profits Over 30 Raids')
plt.xlabel('Keycard Rooms')
plt.ylabel('Profit in Roubles (Millions)')
plt.show()

#Calculate the percentage of keycard cost covered by profit earned from each room WITH Blue mark
room_profits = [2697510, 4565923, 3925351, 1750859, -11488847, 3136678]
percentages = [profit/cost*100 for profit, cost in zip(room_profits, keycard_costs)]
plt.bar(rooms1, percentages, color=['red', 'purple', 'black', 'blue', 'lightblue', 'green'])
plt.title('Percentage of Keycard Cost Covered by Profit Earned')
plt.xlabel('Keycard Rooms')
plt.ylabel('Percentage of card value')
plt.show()

#Calculate the percentage of keycard cost covered by profit earned from each room
#This graph needed its own keycard_costs and room_profits lists because it doesn't use the Keycard with a blue marking. 
#For my skill level, it became too complicated to remove these values without implementing a heap of code. Moving forward, my projects will be structured differently for easier use.
keycard_costs = [63181574, 9185470, 3018385, 31889042, 65334709]
room_profits = [2697510, 4565923, 3925351, 1750859, 3136678]
percentages = [profit/cost*100 for profit, cost in zip(room_profits, keycard_costs)]
plt.bar(rooms, percentages, color=['red', 'purple', 'black', 'blue', 'green'])
plt.title('Percentage of Keycard Cost Covered by Profit Earned')
plt.xlabel('Keycard Rooms')
plt.ylabel('Percentage of card value')
plt.show()