# -*- coding: utf-8 -*-
"""
Anne Harding, 14/03/2019
GEOG5790 - Practical 9 (Cellular Automata)
Cellular automation of simple fire model.
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

# Create an empty environment list:
environment = []
# Loop through range height:
for h in range(height):
    # Create an empty row list:
    row = []
    # Loop through range width:
    for w in range(width):
        # Append fuel_amount to row list:
        row.append(fuel_amount)
    # Append row to environment list:
    environment.append(row)

# Function to check the environment:
def print_environment():
    for h in range(height):
        for w in range(width):
            print(environment[h][w], end=" ")
        print("")
    print("")
    
# Call print_environment() to check environment:
print_environment()
# ----------------------------------------------------------

# Start fire at location [fire_start_y, fire_start_x]:
# Simulate by reducing the amount of fuel available by 1:
environment[fire_start_y][fire_start_x] -= 1
# Call print_environment() to check environment:
print_environment() 
# ----------------------------------------------------------
# Loop through number_of_iterations:
for step in range(number_of_iterations):
    # Loop through height with variable h:
    for h in range(1, height - 1):
        # Loop through width with variable w:
        for w in range(1, width - 1):
            # Default fire to False:
            fire = False
            # Check values around environment[h][w] for fire:
            if (environment[h-1][w-1] < fuel_amount): fire = True 
            if (environment[h-1][w] < fuel_amount): fire = True 
            if (environment[h-1][w+1] < fuel_amount): fire = True 
            if (environment[h][w-1] < fuel_amount): fire = True 
            if (environment[h][w] < fuel_amount): fire = True 
            if (environment[h][w+1] < fuel_amount): fire = True
            if (environment[h+1][w-1] < fuel_amount): fire = True 
            if (environment[h+1][w] < fuel_amount): fire = True 
            if (environment[h+1][w+1] < fuel_amount): fire = True 
            # If fire found, and value in [h][w] > 1, reduce value by 1:
            if (fire == True) & (environment[h][w] > 0):
                environment[h][w] -= 1
    
    # Call print_environment() to check environment at each iteration:
    print_environment()
    
    # Plot environment as pixel plot:
    plt.imshow(np.asarray(environment), interpolation='nearest', cmap='hot')
    # Add colorbar to plot:
    plt.colorbar()
    # Define limits of colorbar as 0-5 for consistency:
    plt.clim(0, 5)
    # Title:
    plt.title('Simple Model - Time Step: ' + str(step))
    # X-axis label@
    plt.xlabel('x')
    # Y-axis label:
    plt.ylabel('y')
    # Get current figure:
    fig = plt.gcf()
    # Save figure:
    plt.savefig(('figures/simple' + str(step) + '.png'), dpi=600, bbox_inches='tight')
    # Clear figure for next iteration:
    fig.clear()
