arr_len = 7
arr = [0,0,1,0,0,1,0]

# this method finds out the jumping on the clouds 
#reference problem : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def jumping_on_clouds(arr,arr_len):
    position = 0
    jumps = 0
    # looping through array
    for index,value in enumerate(arr):
        # checking to by pass the indexes which are already covered by position
        if position == index:
            next_index = index +1
            second_next_index = index + 2
            # checking with the length of next index 
            if next_index < arr_len:
                if arr[next_index] == 0:
                    position += 1
                    jumps += 1
                    # checking with the length of second next index 
                    if second_next_index < arr_len:
                        if arr[second_next_index] == 0:
                            position +=1
                        else:
                            position +=2
                            jumps += 1
                    else:
                        continue
                else:
                    position +=2
                    jumps += 1
            else:
                continue
        else:
            continue
    # finaling returning the jumps
    return jumps
                    
                    

    
print jumping_on_clouds(arr,arr_len)
    