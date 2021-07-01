import argparse

class Solution:
    def calMean(self, arr):
        """
        calMean has the following parameter(s):
        int a[n]: the array of elements

        Returns
        int a': Mean of the elements
        """
        len_arr = len(arr)
        if (len_arr == 1):
            return arr[len_arr - 1]
        else:
            return ((calMean(arr[:len(arr)-1]) * (len_arr - 1) + arr[len_arr - 1]) / len_arr)

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
    result = sol.calMean(array)
    print(result)