sample_input  = [1,2,5,3,7,8,6,4]
sample_input2 = [2,1,5,3,4]
sample_input3 = [1,2,5,3,4,7,8,6]


def minimumBribes(inp_arr,n):
    minimumBribes = 0
    
    for i,val in enumerate(inp_arr):
        #print i,val
        # expected_index = val-1 
        # bribed_difference = expected_index - i

        bribed_difference = 0;
        for index,value in enumerate(inp_arr[i+1:i+10]):
            #print(index,value)
            

            if val > value:
                bribed_difference+=1;
            
        
        if bribed_difference > 2:
            print("Too chaotic")
            return
        elif bribed_difference > 0:
            minimumBribes += bribed_difference
        else: 
            continue

    print(minimumBribes)


minimumBribes(sample_input,n)