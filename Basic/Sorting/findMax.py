import argparse

class Solution:
    def findMax(self, a):
        """
        int a[n]: the array to rotate

        Returns
        int n: maximum nummber
        """
        # if we use aroundPivot method we can use "aroundPivot[-1]"
        return max(a)


if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-a", "--array", help = "The input array")
    
    # Read arguments from command line
    args = parser.parse_args()
    array = args.array
    array = array.split(',')
    array = [map(int, array)]

    # Call function
    sol = Solution()
    result = sol.findMax(array)
    print(result)