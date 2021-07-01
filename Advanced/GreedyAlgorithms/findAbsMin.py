import argparse

class Solution:
    def findAbsMin(self, arr):
        """
        int a[n]: the array of elements

        Returns
        int a': Minimum Absolute Difference
        """
        # apply greedy algorithm
        final_min = arr[0] + arr[1] + arr[2]
        for i in range(arr):
            for j in range(arr):
                min_abs = abs(i - j)
                if min_abs < final_min:
                    final_min = min_abs
        return final_min


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
    result = sol.findAbsMin(array)
    print(result)