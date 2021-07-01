import argparse

class Solution:
    """
    int a[n]: the array of elements
    int b: Target Number

    Returns
    Array<Objects> a': Pairs
    """
    def twoSum(self, nums, target):
        hashmap = {}
        result = []
        for index, value in enumerate(nums):
            difference = target - value
            if difference in hashmap:
                result.append([difference, value])
            else:
                hashmap[value] = index
        return result

if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-a", "--array", help = "Input array")
    parser.add_argument("-t", "--target", type=int, help = "target sum")
    
    # Read arguments from command line
    args = parser.parse_args()
    array = args.array
    array = array.split(',')
    array = [map(int, array)]
    target = args.target

    # Call function
    sol = Solution()
    result = sol.twoSum(array, target)
    print(result)