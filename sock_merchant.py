# given arrays and length
n = 9
ar = [10,20,20,10,10,30,50,10,20]

# this function finds the maximum number of pairs of given arr
def sock_merchant(n,ar):
    remaining_arr = []
    prev_val = 0
    count = 0
    # looping through array
    for i in ar:
        # checking if current value is already in remaining arr to create a pair
        if i in remaining_arr:
            count+=1
            index = remaining_arr.index(i)
            #popping out the pair
            remaining_arr.pop(index)
        else:
            #appending in remaining arr
            remaining_arr.append(i)
    return count

# printing the count of pairs   
print sock_merchant(n,ar)