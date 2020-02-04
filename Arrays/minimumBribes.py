sample_input = [1,2,5,3,7,8,6,4]
sample_input2 = [2,1,5,3,4]
sample_input3 = [1,2,5,3,4,7,8,6]

[1,2,3,4,5,6,7,8]
[1,2,3,5,4,6,7,8]
[1,2,5,3,4,6,7,8]
[1,2,5,3,4,7,6,8]
[1,2,5,3,7,4,6,8]
[1,2,5,3,7,6,4,8]
[1,2,5,3,7,6,8,4]
[1,2,5,3,7,8,6,4]



n = 5 

def minimumBribes(inp_arr,n):
    minimumBribes = 0
    for i,val in enumerate(inp_arr):
        #print i,val
        expected_index = val-1 
        bribed_difference = expected_index - i
        print expected_index,i,val,bribed_difference


        if bribed_difference > 2:
            print "Too chaotic"
            return
        elif bribed_difference > 0:
            minimumBribes += bribed_difference
        else: 
            continue

    print  minimumBribes


minimumBribes(sample_input3,n)