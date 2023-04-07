
import numpy as np

#These are lists of item value found in each specific room, as well as the value of each keycard
#Each list will be separated into sets of 10, with a number denoting which set it belongs to.
#These prices are from the Flea Market average. The numbers are subject to change. What is seen here now may not reflect prices two months from now.

#List of Keycards and their prices.
keycards = {
    'Red Keycard': 63181574,
    'Violet Keycard': 9185470,
    'Black Keycard': 3018385,
    'Blue Keycard': 31889042,
    'Blue Marking Keycard': 453427,
    'Green Keycard': 65334709
}

#These arrays contain each set of profits from each set of ten raids.
RR_data = np.array([[48850, 80545, 70928, 252653, 107754, 142498, 29036, 118038, 69076, 76340],
                    [137083, 40151, 149265, 57967, 74128, 129230, 6324, 96138, 67567, 17602],
                    [68221, 160863, 115192, 45255, 135457, 132667, 97507, 79627, 35821, 55727]])
VR_data = np.array([[91103, 130361, 111532, 63606, 85761, 82815, 95240, 88396, 56131, 275653],
                    [84217, 75284, 85333, 186876, 117873, 263500, 70576, 88975, 439681, 200120],
                    [94685, 106264, 158590, 218659, 84934, 162750, 325609, 321045, 195312, 205042]])
BKR_data = np.array([[106991, 194536, 543250, 115567, 73425, 136198, 169482, 78655, 65638, 194115],
                     [121809, 25389, 284339, 87217, 90097, 101627, 87524, 119395, 176239, 27120],
                     [188664, 89038, 94201, 56219, 89253, 212319, 70433, 112193, 82530, 131888]])
BR_data = np.array([[95099, 71040, 17960, 32493, 79976, 27484, 44305, 11758, 91464, 22269],
                    [69920, 74646, 40376, 62036, 56541, 68220, 2016, 46789, 171720, 28665],
                    [70719, 13817, 126951, 86053, 45216, 38078, 93726, 29101, 86144, 46277]])
BMR_data = np.array([[99188, 65995, 52597, 103373, 25369, 137081, 50832, 0, 111343, 45480],
                     [57080, 128538, 54094, 57496, 184443, 55907, 69081, 57254, 55219, 35217],
                     [43787, 126063, 3598, 54961, 46650, 108853, 106291, 70893, 19336, 96824]])
GR_data = np.array([[32263, 172895, 42356, 84097, 157325, 87794, 113882, 148729, 99379, 43115],
                    [119437, 105378, 39744, 51169, 104930, 68192, 2495, 36101, 28316, 107791],
                    [19960, 186277, 108870, 185406, 162931, 289667, 101694, 260229, 87852, 88404]])

#Data Exploration portion of project

#First set Totals.
red_total = np.sum(RR_data[0])
violet_total = np.sum(VR_data[0])
black_total = np.sum(BKR_data[0])
blue_total = np.sum(BR_data[0])
blue_mark_total = np.sum(BMR_data[0])
green_total = np.sum(GR_data[0])
print("The totals from each room over the first set of ten runs were as follows: ",
      "Red Room: " + str(red_total),
      "Violet Room: " + str(violet_total),
      "Black Room: " + str(black_total),
      "Blue Room: " + str(blue_total),
      "Blue Mark Room: " + str(blue_mark_total),
      "Green Room: " + str(green_total),
      sep="\n")
print()

#Second set Totals.
red_total_1 = np.sum(RR_data[1])
violet_total_1 = np.sum(VR_data[1])
black_total_1 = np.sum(BKR_data[1])
blue_total_1 = np.sum(BR_data[1])
blue_mark_total_1 = np.sum(BMR_data[1])
green_total_1 = np.sum(GR_data[1])
print("The totals from each room over the second set of ten runs were as follows: ",
      "Red Room: " + str(red_total_1),
      "Violet Room: " + str(violet_total_1),
      "Black Room: " + str(black_total_1),
      "Blue Room: " + str(blue_total_1),
      "Blue Mark Room: " + str(blue_mark_total_1),
      "Green Room: " + str(green_total_1),
      sep="\n")
print()

#Third set totals.
red_total_2 = np.sum(RR_data[2])
violet_total_2 = np.sum(VR_data[2])
black_total_2 = np.sum(BKR_data[2])
blue_total_2 = np.sum(BR_data[2])
blue_mark_total_2 = np.sum(BMR_data[2])
green_total_2 = np.sum(GR_data[2])
print("The totals from each room over the third set of ten runs were as follows: ",
      "Red Room: " + str(red_total_2),
      "Violet Room: " + str(violet_total_2),
      "Black Room: " + str(black_total_2),
      "Blue Room: " + str(blue_total_2),
      "Blue Mark Room: " + str(blue_mark_total_2),
      "Green Room: " + str(green_total_2),
      sep="\n")
print()

#First set of averages.
red_average = np.mean(RR_data[0])
violet_average = np.mean(VR_data[0])
black_average = np.mean(BKR_data[0])
blue_average = np.mean(BR_data[0])
blue_mark_average = np.mean(BMR_data[0])
green_average = np.mean(GR_data[0])
print("The averages from each room over the first set of ten runs were as follows: ",
      "Red Room: " + str(red_average),
      "Violet Room: " + str(violet_average),
      "Black Room: " + str(black_average),
      "Blue Room: " + str(blue_average),
      "Blue Mark Room: " + str(blue_mark_average),
      "Green Room: " + str(green_average),
      sep="\n")
print()

#Second set of averages.
red_average1 = np.mean(RR_data[1])
violet_average1 = np.mean(VR_data[1])
black_average1 = np.mean(BKR_data[1])
blue_average1 = np.mean(BR_data[1])
blue_mark_average1 = np.mean(BMR_data[1])
green_average1 = np.mean(GR_data[1])
print("The averages from each room over the second set of ten runs were as follows: ",
      "Red Room: " + str(red_average1),
      "Violet Room: " + str(violet_average1),
      "Black Room: " + str(black_average1),
      "Blue Room: " + str(blue_average1),
      "Blue Mark Room: " + str(blue_mark_average1),
      "Green Room: " + str(green_average1),
      sep="\n")
print()

#Third set of averages.
red_average2 = np.mean(RR_data[2])
violet_average2 = np.mean(VR_data[2])
black_average2 = np.mean(BKR_data[2])
blue_average2 = np.mean(BR_data[2])
blue_mark_average2 = np.mean(BMR_data[2])
green_average2 = np.mean(GR_data[2])
print("The averages from each room over the third set of ten runs were as follows: ",
      "Red Room: " + str(red_average2),
      "Violet Room: " + str(violet_average2),
      "Black Room: " + str(black_average2),
      "Blue Room: " + str(blue_average2),
      "Blue Mark Room: " + str(blue_mark_average2),
      "Green Room: " + str(green_average2),
      sep="\n")
print()


#Combined profit from each individual room over 30 runs.
red_room_profit = np.sum(RR_data)
violet_room_profit = np.sum(VR_data)
black_room_profit = np.sum(BKR_data)
blue_room_profit = np.sum(BR_data)
blue_mark_room_profit = np.sum(BMR_data)
green_room_profit = np.sum(GR_data)
print("The total profit earned from each room over 30 runs: ", 
      "Red Room: " + str(red_room_profit),
      "Violet Room: " + str(violet_room_profit),
      "Black Room: " + str(black_room_profit),
      "Blue Room: " + str(blue_room_profit),
      "Blue Mark Room: " + str(blue_mark_room_profit),
      "Green Room: " + str(green_room_profit),
      sep="\n")
print()

#Average profit made from each room over 30 individual runs.
red_room_average = np.mean(RR_data, axis=None)
violet_room_average = np.mean(VR_data, axis=None)
black_room_average = np.mean(BKR_data, axis=None)
blue_room_average = np.mean(BR_data, axis=None)
blue_mark_room_average = np.mean(BMR_data, axis=None)
green_room_average = np.mean(GR_data, axis=None)
print("The average profit earned per run from each room over 30 runs: ", 
      "Red Room: {:.2f}".format(red_room_average),
      "Violet Room: {:.2f}".format(violet_room_average),
      "Black Room: {:.2f}".format(black_room_average),
      "Blue Room: {:.2f}".format(blue_room_average),
      "Blue Mark Room: {:.2f}".format(blue_mark_room_average),
      "Green Room: {:.2f}".format(green_room_average),
      sep="\n")
print()

#Percentage of card's value earned from its own room after 30 runs
red_keycard_percentage = red_room_profit / keycards['Red Keycard'] * 100
violet_keycard_percentage = violet_room_profit / keycards['Violet Keycard'] * 100
black_keycard_percentage = black_room_profit / keycards['Black Keycard'] * 100
blue_keycard_percentage = blue_room_profit / keycards['Blue Keycard'] * 100

#Blue mark keycard has to be bought every run. This has to have its own unique expression where its value is subtracted by the profits 30 times over.
blue_mark_keycard_cost = 453427 * 30
blue_mark_room_profit_with_cost = blue_mark_room_profit - blue_mark_keycard_cost
blue_mark_keycard_percentage = blue_mark_room_profit_with_cost / keycards['Blue Marking Keycard'] * 100
green_keycard_percentage = green_room_profit / keycards['Green Keycard'] * 100
print("The percentage of the each card's value earned from its corresponding room over 30 runs: ",
"Red Keycard earned {:.2f}% of its worth".format(red_keycard_percentage),
"Violet Keycard earned {:.2f}% of its worth".format(violet_keycard_percentage),
"Black Keycard earned {:.2f}% of its worth".format(black_keycard_percentage),
"Blue Keycard earned {:.2f}% of its worth".format(blue_keycard_percentage),
"Keycard with a blue marking earned {:.2f}% of its worth".format(blue_mark_keycard_percentage),
"Green Keycard earned {:.2f}% of its worth".format(green_keycard_percentage),
sep="\n")
print()

#Lists for importation into the Tarkov_Room_Visuals.py file.
averages = [red_room_average, violet_room_average, black_room_average, blue_room_average, blue_mark_room_average, green_room_average]
profits = [red_room_profit, violet_room_profit, black_room_profit, blue_room_profit, blue_mark_room_profit, green_room_profit]