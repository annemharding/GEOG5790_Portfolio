# -*- coding: utf-8 -*-
"""
Anne Harding, 14/03/2019
GEOG5790 - Practical 9 (Cellular Automata)
Cellular automation of improved fire model.
"""

# Import modules:
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import csv
import time

# Close all open figures in Spyder:
plt.close('all')

# Variables:
number_of_iterations = 10
width = 50 
height = 50 
fuel_amount = 5

# Define array for fire starting locations:
fire_loc = ([10, 10], [35,35])      # Can add other locations to this, as necessary:
# Print fire_loc to manually check structure:
# print(fire_loc)

# ----------------------------------------------------------

# Create environment list to store fuel_amount in each cell:
environment = []
# Create fire_grid list to have True/False as to whether each cell is on fire:
fire_grid = []

for h in range(height):
    row = []
    fire_grid_row = []
    for w in range(width):
        row.append(fuel_amount)
        fire_grid_row.append(False)
    environment.append(row)
    fire_grid.append(fire_grid_row)
    
# Function to check environment list:
def print_array(array):
    for h in range(height):
        for w in range(width):
            print(array[h][w], end=" ")
        print("")
    print("")

# Print statement to check newly-created environment:
# print_array(environment)

# ----------------------------------------------------------
# Define figure:
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# ----------------------------------------------------------

# Start fire in locations defined in fire_loc:
for loc in fire_loc:
    print(loc)
    # Reduce fuel_amount in that cell by 1:
    environment[loc[0]][loc[1]] -= 1
    # Set fire_grid cell to True:
    fire_grid[loc[0]][loc[1]] = True
    
# Print statement to check environment once fire has started:
print_array(environment) 

# ----------------------------------------------------------
# Define carry-on variable to tell model iteration loop when to continue
# and when to stop:
carry_on = True

# Model iterations function:
def update(frame_number):
    '''
    Function to iterate through fire model.
    '''
    
    # Assign carry_on function as a global variable so that it can be
    # used within the function:
    global carry_on
    
    # Clear figure for next iteration:
    fig.clear()
    
    # If carry_on = True, then continue iterating through model:
    if True:
        if (carry_on):
            # Loop through iterations of model run:
            for step in range(number_of_iterations):
                # Create fire_grid2 list to store temporary results of model iteration:
                fire_grid2 = []
                for h in range(height):
                    fire_grid2_row = []
                    for w in range(width):
                        fire_grid2_row.append(False)
                    fire_grid2.append(fire_grid2_row)    
                
                # Loop through cells in world:
                for h in range(1, height - 1):
                    for w in range(1, width - 1):
                        # Check if a fire has started in that cell:
                        fire = fire_grid[h][w]
                        # If cell is on fire:
                        if (fire):
                            fire_grid2[h][w] = True
                            # Loop through neighbouring cells:
                            for dh in range(-1,2):
                                ddh = h + dh
                                # Print statement to check loop is working properly:
                                #print("ddh: ", ddh)
                                for dw in range(-1,2):
                                    ddw = w + dw
                                    # Print statement to check loop is working properly:
                                    #print("ddw: ", ddw)
                                    # If the cell has fuel, then set fire_grid2 value to True:
                                    if (environment[ddh][ddw] > 0):
                                        fire_grid2[ddh][ddw] = True
                            '''
                            # These lines are simplified in the loop through
                            # neighbouring cells above:
                            if (environment[h-1][w-1] > 0):
                                #print("Set on fire", h-1, w-1)
                                fire_grid2[h-1][w-1] = True
                            if (environment[h-1][w] > 0):
                                fire_grid2[h-1][w] = True 
                            if (environment[h-1][w+1] > 0):
                                fire_grid2[h-1][w+1] = True 
                            if (environment[h][w-1] > 0):
                                fire_grid2[h][w-1]  = True 
                            if (environment[h][w] > 0):
                                fire_grid2[h][w] = True 
                            if (environment[h][w+1] > 0):
                                fire_grid2[h][w+1] = True
                            if (environment[h+1][w-1] > 0):
                                fire_grid2[h+1][w-1] = True 
                            if (environment[h+1][w] > 0):
                                fire_grid2[h+1][w]  = True 
                            if (environment[h+1][w+1] > 0):
                                fire_grid2[h+1][w+1] = True
                            '''
                # Loop through cells in world:            
                for h in range(1, height - 1):
                    for w in range(1, width - 1):
                        # Check if a fire has started in that cell:
                        fire = fire_grid2[h][w]
                        # If cell is on fire::
                        if (fire):
                            # Reduce fuel_amount in that cell by 1:
                            environment[h][w] -= 1
                        '''
                        # Previous way of writing results out:
                        # Write output to a results file to wait until all the cells have
                        # finished processing:
                        if (fire == True) & (environment[h][w] > 0): 
                            results[h][w] -= 1
                        environment = results
                    '''
                
                # Write temporary fire grid (fire_grid2) to permanent (fire_grid):
                for h in range(len(fire_grid)):
                    for w in range(len(fire_grid[0])):
                        fire_grid[h][w] = fire_grid2[h][w]
                
                # Loop through environment grid. If there is no fuel left
                # in a cell, then the fire in that cell is extinguished.
                # Write to fire_grid:
                for h in range(1, height - 1):
                    for w in range(1, width - 1):
                        if (environment[h][w] == 0):
                            fire_grid[h][w] = False
            
            # Stopping condition:
            total = 0
            # Find total sum of environment (not including edges):
            for h in range(1, height - 1): 
                for w in range(1, width - 1): 
                    total += environment[h][w]
            # If the total sum of environment (not including edges) is 0,
            # then the model run is complete and no more iterations are required.
            if (total == 0):
                # Break out of model iteration loop by setting carry_on = False:
                carry_on = False
                # Print statement to tell user that model run has stopped and
                # at which iteration:
                print("Model run ends at iteration ", step, ".")
            
            # Add 1 second time delay between model iterations to slow down animation:
            # time.sleep(1)
            
    # Plot environment from model iteration:
    plt.xlim(0, len(environment))
    plt.ylim(0, len(environment[0]))
    plt.imshow(environment)
           
    '''
    # Save plot from each time step as an individual .png file:
    plt.xlim(0, len(environment))
    plt.ylim(0, len(environment[0]))
    # Plot environment as pixel plot:
    # plt.imshow(np.asarray(environment), interpolation='nearest', cmap='hot')
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
    '''

def gen_function(b = [0]):
    '''
    Function to generate matplotlib animation of fire model.
    '''
    a = 0
    global carry_on
    while  (a < number_of_iterations) & (carry_on): 
        yield a			#: Returns control and waits next call.
        a = a + 1
# ----------------------------------------------------------

# Check update function is working:
# update(10)
        
# Define animation:
animation = anim.FuncAnimation(fig, update, frames=gen_function, interval=1000, repeat=False)
# Write animation to screen:
plt.show()

print("Writing output data to file.")
file = 'data/dataout.csv'
with open(file, 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=' ')
    for row in environment:
        writer.writerow(row)
        
# Call print_environment() to check environment list:
print("Check environment variable after use in function.")
print_array(environment)  