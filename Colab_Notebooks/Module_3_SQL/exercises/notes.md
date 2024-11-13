import the necessary libraries (random for generating random numbers and matplotlib.pyplot for creating plots)

initialize variables:

num_simulations: Number of times we'll run the dice game simulation

successes: Counter for how many times we reach step 60

all_steps: List to store all final steps reached across simulations

For each simulation (num_simulations times):
Start at step 0
Roll the die 100 times
If we're clumsy (random number < 0.001), reset to step 0
Move up or down based on the die roll
On a 6, get a bonus roll
If we reach step 60, count it as a success and stop early

Store the final step reached in all_steps
Probability Calculation
probability = successes / num_simulations

This calculates the probability by dividing successes by total simulations and prints it.

Plot Creation
plt.figure(figsize=(10, 6))
plt.hist(all_steps, bins=30, edgecolor='black')
plt.title('Distribution of Steps Reached')
plt.xlabel('Final Step Number')
plt.ylabel('Frequency')
plt.axvline(x=60, color='r', linestyle='--', label='Goal (Step 60)')
plt.legend()
plt.show()
This creates a histogram of all final steps reached:
