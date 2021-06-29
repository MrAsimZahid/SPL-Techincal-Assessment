import argparse

class Solution:
    def compareStrings(self, str1, str2):
        """
        str a: Input string 1
        str b: Input string 2

        Returns
        bool: 1 or 0
        """
        str1 = set(str1)
        str2 = set(str2)
        result = str1.intersection(str2)
        if result is None:
            return 0
        else:
            return 1

if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-a", "--string1", type=str, help = "Input string 1")
    parser.add_argument("-b", "--string2", type=str, help = "Input string 2")
    
    # Read arguments from command line
    args = parser.parse_args()
    str1 = args.string1
    str2 = args.string2

    # Call function
    sol = Solution()
    result = sol.compareStrings(str1, str2)
    print(result)