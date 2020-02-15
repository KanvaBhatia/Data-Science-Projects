"""
    # 6_steps_game.py
    # in a game of dice,
    # if you toss a 1 or 2 you climb 1 step up the stairs
    # if you toss 3,4,5 you climb 1 step down the stairs
    # if you toss a 6, you toss again and climb the resulting number up the stairs
    # there is a 0.1%  or 0.001 chance that you will fall; in which case, you will have to start again from bottom
    # this program simulates the probability that you will reach the 60th step
    #to self: see rand gen note in numpy

    # other method ot make sure step doesnt fall below 0
    # if step == 0 and die <= 2:
    #       step = step
    Created by: temikelani on: 2/12/20
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Set the seed
np.random.seed(123)

# Initialize all_walks to collect the last step of each random walk
all_walks = []

# repeat random walk 10 times
for i in range(500):

    # Initialize list random_walk that contains the first step, which is the integer 0.
    random_walk = [0]

    # Simulate a random walk with 100 steps
    for x in range(100):
        # Set step: last element in random_walk / resets step to the current step with each loop
        step = random_walk[-1]

        # Use randint() to simulate a die
        die = np.random.randint(1, 7)

        # set up the control construct to climb up or down steps
        if die <= 2:
            # to avoid step becoming -1 (when step = 0) as there are no negative steps,
            # if step-1 goes below 0 it will be overridden by max. essentially, player throws die again
            step = max(0, step - 1)
        elif 3 <= die < 6:
            step += 1
        else:
            step += np.random.randint(1, 7)

        # generate a random float and implement fall control construct for any float between 0 and 0.001
        if np.random.rand() <= 0.001:
            step = 0

        # append next_step to random_walk
        random_walk.append(step)

    # append entire random_walk to all works. make list of list
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_awR
np_aw = np.array(all_walks)

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# # Plot all the walks
# plt.plot(np_aw_t)
# plt.show()

# clear figure
plt.clf()

# Select last row from np_aw_t: ends
ends = np_aw_t[100, :]

# # Plot histogram of ends, display plot
# plt.hist(ends, bins=20)
# plt.show()

"""
The histogram of the previous exercise was created from a Numpy array ends, that contains 500 integers. 
Each integer represents the end point of a random walk. To calculate the chance that this end point is greater than 
or equal to 60, you can count the number of integers in ends that are greater than or equal to 60 and divide that 
number by 500, the total number of simulations.
np.mean(ends>=60) gives you the fraction of simulations that ended higher than step 60.
"""
ends_60 = ends[ends >= 60]
print(len(ends_60) / len(ends))

