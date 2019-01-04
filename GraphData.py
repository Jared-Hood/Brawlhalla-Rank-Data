import matplotlib.pyplot as plt
import matplotlib.axes
import numpy as np
import average

data = [0]
playerrank_list , num_players = average.averages()


for i in playerrank_list:
    data.append(round((playerrank_list[i] / num_players) * 100, 4 ))

#Cumulative percentage for rankings
for i in range(len(data)):
    if( i != 0):
        data[i] += data[i-1]

#ranking cutoffs
ranks = np.array([2300,2000,1700,1500,1200,1000,700])

plt.plot(ranks,data)
plt.xlabel("Rank")
plt.ylabel("Percentage of Players Above Rank")
plt.title("Cumalative Rank Percentages of Brawlhalla Players")


for i_x, i_y in zip(ranks,data):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, round(i_y,2)))

plt.show()
