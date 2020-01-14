# Referecnce problem : https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
class leftRotation:
    def __init__(self):
        self.input_array = [1,2,3,4,5]
        self.length = 5
        self.rotate = 2
        self.rotated_array = []

    # processing arrays and adding rotations as per required
    def processRotation(self): 
        temp_array = []
        # looping through x range
        for x in range(self.rotate):
            if x < self.rotate:
                temp_array.append(self.input_array[0])
                del self.input_array[0]
        
        self.rotated_array  = self.input_array + temp_array
        # returning rotated array
        return self.rotated_array



rotation = leftRotation()
rotation.processRotation()