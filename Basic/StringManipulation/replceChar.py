import argparse

class Solution:
    """
    Example:

        string name = 'We Are Your Technology Partners' and char x = ' '
        returns 'WeAreYourTechnologyPartners'
    """
    def replaceChar(self, string, cha):
        return string.replace(chr, "")

if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-s", "--string", help = "Input string")
    parser.add_argument("-c", "--char", type=int, help = "replacement character")
    
    # Read arguments from command line
    args = parser.parse_args()
    array = args.string
    pivot = args.char

    # Call function
    sol = Solution()
    result = sol.replaceChar(array, pivot)
    print(result)