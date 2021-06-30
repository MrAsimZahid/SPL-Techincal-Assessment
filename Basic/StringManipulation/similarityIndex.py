import argparse
import difflib

class Solution:
    """
    SimilarityIndexGenome has the following parameter(s):
        string a[n]: first genome
        string b[n]: second genmoe

    Returns
       double a'

    """
    # Jacard index could be used here too.
    def similarityIndex(self, str1, str2):
        return difflib.SequenceMatcher(None, str1, str2).ratio()

if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-s1", "--string1", help = "Input string 1")
    parser.add_argument("-s2", "--string2", help = "Input string 2")
    
    # Read arguments from command line
    args = parser.parse_args()
    str1 = args.string1
    str2 = args.string2

    # Call function
    sol = Solution()
    result = sol.similarityIndex(str1, str2) #('ATATGTATG', 'ATATATATG')
    print(result)