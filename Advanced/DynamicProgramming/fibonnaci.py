import argparse

class Solution:
    def fibonnaci(self, n):
        # Taking 1st two fibonacci nubers as 0 and 1
        f = [0, 1]
                
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
        return f[n]


if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-n", "--number", type=int, help = "Input array")

    
    # Read arguments from command line
    args = parser.parse_args()    
    num = args.number

    # Call function
    sol = Solution()
    result = sol.fibonnaci(num)
    print(result)