#initializing variables
total_steps = 8
steps = "UDDDUDUU"

# this definition is used to count number of valleys a user has passed on the basis of string provided
def count_valleys(total_steps,steps):
    level = 0
    valleys = 0
    iteration = 0
    # iterating over the array
    for i,step in enumerate(steps):
        # counting iteration
        iteration +=1
        # checking sea level if up 
        if step == "U":
            level += 1 
        # checking sea level if up 
        else:
            #counting valleys here if user at sea level and stepping down
            if level == 0 and iteration != total_steps:
                valleys +=1
            level -= 1   
    # returning valleys count at the end
    return valleys

print count_valleys(total_steps,steps)
