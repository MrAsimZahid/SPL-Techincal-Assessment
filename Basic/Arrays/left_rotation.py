import argparse
from collections import deque


class Solution:
    def rotLeft(self, a, d):
        """
        int a[n]: the array to rotate
        int d: the number of rotations

        Returns
        int a'[n]: the rotated array

        Reference: https://docs.python.org/3/library/collections.html#collections.deque
        """
        a = deque(a)
        if len(array) is d:
            return [reversed(a)]
        a.rotate(-int(d))
        return list(a)


if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-a", "--array", help = "The array to rotate")
    parser.add_argument("-d", "--rotation", type=int, help = "The number of rotations")
    
    # Read arguments from command line
    args = parser.parse_args()
    array = args.array
    rotation = len(array.split(','))
    rotation = args.rotation

    # Call function
    sol = Solution()
    result = sol.rotLeft(array.split(','), rotation)
    print(result)