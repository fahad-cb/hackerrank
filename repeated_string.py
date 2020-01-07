string = 'aba'
number = 10

# function to calculate number of a in formatted sting 
#reference problem : https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def repeated_string(string,number):
    string_length = len(string)
    remainder = number % string_length
    divided_by = number / string_length
    # counting a in fresh string 
    if string_length > 0:
        count = 0
        for index,value in enumerate(string):
            if (value == 'a'):
                count += 1
    # now multiplying divided  by a counts
    final_count = count * divided_by
    # checking if remainder is there to add remaining A's
    if remainder != 0:
        for index,value in enumerate(string):
            if index < remainder:
                if value == 'a':
                    final_count += 1

    return final_count

print repeated_string(string,number)