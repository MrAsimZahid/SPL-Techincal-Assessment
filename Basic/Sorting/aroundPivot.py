import argparse

class Solution:
    """
    DistributeArray has the following parameter(s):
        int[n] a: Array of integers
        int b: pivot

    Returns
        int[n] a'

    took code fro @Usman-Alii and 
    """
    def partition(arr, low, high, pivot):                   #In addition to partition function I am giving pivot point to the it so i can distibute array around desired pivot point
        i = (low-1)         # index of smaller element       
        for j in range(low, high):
    
            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
    
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
    
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)


    def quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
    
            # pi is partitioning index, arr[pi] is now
            # at right place
            pi = partition(arr, low, high,arr[high])
                
            quickSort(arr, low, pi-1)                       #sort elements before
            quickSort(arr, pi+1, high)                      # sort elements after partition


    def aroundPivot(self, arr, pivot):
        n = len(arr) - 1                                        #higher index of array
        indexOfPivot = partition(arr, 0, n, pivot)              #getting the index of pivot element after distributing array around it
        quickSort(arr, 0, indexOfPivot - 1)                     #sort the elements before pivot point
        quickSort(arr, indexOfPivot + 1, n)                     #sort elements after pivot point
        return arr



if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-a", "--array", help = "The array to rotate")
    parser.add_argument("-b", "--pivot", type=int, help = "pivot integer")
    
    # Read arguments from command line
    args = parser.parse_args()
    array = args.array
    array = array.split(',')
    array = [map(int, array)]
    pivot = args.pivot

    # Call function
    sol = Solution()
    result = sol.aroundPivot(array, pivot)
    print(result)