import sys
import math

#Reference Problem : https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Input Sample Array
Array = [
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,2,4,4,0],
    [0,0,0,2,0,0],
    [0,0,1,2,4,0]
]

# class for calulating hourglass and and its sums
class HighestHourGlass:
    # initializing the Class
    def __init__(self,arg):
        self.input_arr = arg
        self.hoursum = []
        self.HighestHourGlassSum = -10000000000000000

    # processing the sum and saving
    def processHourGlasses(self):
        input_arr = self.input_arr
        for y in range(6):
            for x in range(6):
                if y +2 < 6 and x + 2 < 6:
                    a = input_arr[y][x]
                    b = input_arr[y][x+1]
                    c = input_arr[y][x+2]
                    d = input_arr[y+1][x+1]
                    e = input_arr[y+2][x]
                    f = input_arr[y+2][x+1]
                    g = input_arr[y+2][x+2]
                    tempsum =  a + b + c + d + e + f + g
                    if tempsum > self.HighestHourGlassSum:
                        self.HighestHourGlassSum = tempsum
             

Object = HighestHourGlass(Array)
Object.processHourGlasses()
print Object.HighestHourGlassSum

    

