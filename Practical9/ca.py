# -*- coding: utf-8 -*-
"""
Anne Harding, 14/03/2019
GEOG5790 - Practical 9 (Cellular Automata)
Cellular automation of simple fire model.
"""

# Import modules:
import matplotlib

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

# Start modelling:
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
# ----------------------------------------------------------

# Improving the model:

# Create a second results environment:
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

for step in range(number_of_iterations):
    for h in range(1, height - 1):
        for w in range(1, width - 1):
            fire = False
            if (environment[h-1][w-1] < fuel_amount): fire = True 
            if (environment[h-1][w] < fuel_amount): fire = True 
            if (environment[h-1][w+1] < fuel_amount): fire = True 
            if (environment[h][w-1] < fuel_amount): fire = True 
            if (environment[h][w] < fuel_amount): fire = True 
            if (environment[h][w+1] < fuel_amount): fire = True
            if (environment[h+1][w-1] < fuel_amount): fire = True 
            if (environment[h+1][w] < fuel_amount): fire = True 
            if (environment[h+1][w+1] < fuel_amount): fire = True 
            if (fire == True) & (environment[h][w] > 0): 
                results[h][w] -= 1
    environment = results
    print_environment() 
    # Add a stopping condition:
    total = 0
    for h in range(1, height - 1): 
        for w in range(1, width - 1): 
            total += environment[h][w]
    if (total == 0):
        print("ends at iteration ", step)
        break
