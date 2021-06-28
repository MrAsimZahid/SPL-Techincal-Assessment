import argparse
from collections import deque

class Solution:
    def rotLeft(self, a):
        """
        int a[n]: the array to rotate

        Returns
        int a'[n]: the rotated array

        Reference: https://docs.python.org/3/library/collections.html#collections.deque
        """
        a = deque(a)
        a.reverse()
        return list(a)
        

if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-a", "--array", help = "The array to rotate")
    
    # Read arguments from command line
    args = parser.parse_args()
    array = args.array

    # Call function
    sol = Solution()
    result = sol.rotLeft(array.split(','))
    print(result)