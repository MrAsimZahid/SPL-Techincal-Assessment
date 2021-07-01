import argparse

class Solution:
    """
    Given an array of n elements return the array of maps with number keys
    mapped to the number of times they appeared in the array.

    Example:

        Input Array : [1,2,3,4,5,4,3,1]

        Output Array: [{1:2},{2:1},{3:2},{4:2},{5:1}]
    """
    def numberFrequency(self, nums):
        hashmap = {}
        result = []
        # Calculate fequencies 
        for index, value in enumerate(nums):
            if value in hashmap:
                hashmap.update({value : int(hashmap[value]) + 1})
            else:
                hashmap[value] = 1
        
        # Add maps into list
        for key, value in hashmap.items():
            result.append({key:value})

        return result

if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-a", "--array", help = "Input array")
    
    # Read arguments from command line
    args = parser.parse_args()
    array = array.split(',')
    array = [map(int, array)]
    array = args.array

    # Call function
    sol = Solution()
    result = sol.numberFrequency(array) # ([1,2,3,4,5,4,3,1])
    print(result)