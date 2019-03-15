# -*- coding: utf-8 -*-
"""
Anne Harding, 14/03/2019
GEOG5790 - Practical 9 (Cellular Automata)
Cellular automation of improved fire model.
"""

# Import modules:
import matplotlib.pyplot as plt
import numpy as np

# Variables:
number_of_iterations = 10
width = 10
height = 10
fire_start_x = 4
fire_start_y = 4
fuel_amount = 5

# ----------------------------------------------------------

# Create environment list and results list:
environment = []
results = []
for h in range(height):
    row = []
    results_row = []
    for w in range(width):
        row.append(fuel_amount)
        results_row.append(fuel_amount)
    environment.append(row)
    results.append(results_row)
    
# Function to check environment list:
def print_environment():
    for h in range(height):
        for w in range(width):
            print(environment[h][w], end=" ")
        print("")
    print("")

# Function to check results list:
def print_results():
    for h in range(height):
        for w in range(width):
            print(results[h][w], end=" ")
        print("")
    print("")    
    
# Call print_environment() to check environment list:
print_environment()
# Call print_results() to check results list:
print_results()

# ----------------------------------------------------------

# Start fire at location [fire_start_y, fire_start_x]:
# Simulate by reducing the amount of fuel available by 1:
environment[fire_start_y][fire_start_x] -= 1
# Call print_environment() to check environment list:
print_environment() 

# ----------------------------------------------------------

# Loop through iterations of model run:
for step in range(number_of_iterations):
    for h in range(1, height - 1):
        for w in range(1, width - 1):
            fire = False
            # Spread fire to surrounding cells:
            if (environment[h-1][w-1] < fuel_amount): fire = True 
            if (environment[h-1][w] < fuel_amount): fire = True 
            if (environment[h-1][w+1] < fuel_amount): fire = True 
            if (environment[h][w-1] < fuel_amount): fire = True 
            if (environment[h][w] < fuel_amount): fire = True 
            if (environment[h][w+1] < fuel_amount): fire = True
            if (environment[h+1][w-1] < fuel_amount): fire = True 
            if (environment[h+1][w] < fuel_amount): fire = True 
            if (environment[h+1][w+1] < fuel_amount): fire = True 
            # Write output to a results file to wait until all the cells have
            # finished processing:
            if (fire == True) & (environment[h][w] > 0): 
                results[h][w] -= 1
    
    # Write results to environment at end of model iteration:
    environment = results
    # Call print_environment() to check environment list:
    print_environment()
    
    # Plot environment as pixel plot:
    plt.imshow(np.asarray(environment), interpolation='nearest', cmap='hot')
    # Add colorbar to plot:
    plt.colorbar()
    # Define limits of colorbar as 0-5 for consistency:
    plt.clim(0, 5)
    # Title:
    plt.title('Improved Model - Time Step: ' + str(step))
    # X-axis label@
    plt.xlabel('x')
    # Y-axis label:
    plt.ylabel('y')
    # Get current figure:
    fig = plt.gcf()
    # Save figure:
    plt.savefig(('figures/improved' + str(step) + '.png'), dpi=600, bbox_inches='tight')
    # Clear figure for next iteration:
    fig.clear()
    
    # Stopping condition:
    total = 0
    # Find total sum of environment (not including edges):
    for h in range(1, height - 1): 
        for w in range(1, width - 1): 
            total += environment[h][w]
    # If the total sum of environment (not including edges) is 0,
    # then the model run is complete and no more iterations are required.
    if (total == 0):
        # Print statement to tell user that model run has stopped and
        # at which iteration:
        print("ends at iteration ", step)
        # Break out of model iteration loop:
        break

