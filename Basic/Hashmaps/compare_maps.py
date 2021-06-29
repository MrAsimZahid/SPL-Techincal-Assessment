import argparse

class Solution:
    def compareMaps(self, map1, map2):
        """
        dict x: hashmap1
        dict b: hashmap2

        Returns
        bool: 1 or 0
        """
        if map1 == map2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-x", "--map1", help = "Input map 1")
    parser.add_argument("-b", "--map2", help = "Input map 2")
    
    # Read arguments from command line
    args = parser.parse_args()
    hash1 = args.map1
    hash2 = args.map2

    # Call function
    sol = Solution()
    result = sol.compareMaps(hash1, hash2) # ({'a':1,'b':2,'d':3}, {'c':3,'b':2,'a':1})
    print(result)