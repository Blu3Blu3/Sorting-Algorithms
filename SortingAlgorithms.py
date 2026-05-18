# Sorting Algorithms
# Love yourself <3
# Started: 5/7/2026
# Finished: -----
# Validated: -----
# Last updated: 5/14/2026
#   - Created a new program to hold and individually test multiple sorting algorithms

'''
Selection Sort
Love yourself <3
Started: 5/7/2026
Finished: 5/7/2026
Validated: 5/7/2026
Last updated: 5/14/2026
   - Moved console logs to separate functions
   - Reworked random tests to be more concise

Selection Sort works by splitting an array into a sorted part and unsorted part.
It repeatedly searches the unsorted part for the minimum element, then appends it to the sorted part.
Every iteration, it has to run through all the elements in the unsorted array.
Therefore, it's O(n^2) in all cases.

To make the Selection Sort algorithm:
1. Have an outer loop iterate over all n elements in array arr.
2. Have an inner loop iterate over all elements past the outer index (inclusive).
3. Find the minimum element in the inner loop's subarray.
4. Put it at the outer index.
5. Loops repeat until the array is fully sorted.
'''

# Run selection sort on an array and return the sorted version, plus how many iterations it took.
#   - arr (int[]): An array of ints to be sorted.
def selection_sort(arr):
    # Make a copy because I'm not sure if arr is passed by reference...
    ret = arr.copy()
    ops = 0
    for o in range(len(ret)):
        for i in range(o, len(ret)):
            if(ret[o] > ret[i]):
                temp = ret[o]
                ret[o] = ret[i]
                ret[i] = temp
                ops += 1
    return [ret, ops]

'''
Merge Sort
Wooooo
Started: 5/17/2026
Finished: -----
Validated: -----
Last updated: 5/17/2026
    - Started work on the functions

Merge Sort works by bisecting an array into subarrays, then bisecting those, repeatedly, until they are
one element long. From there, it undoes the splits by merging the subarrays together, picking elements
to add to the "merged" array from either subarray, depending on which is next in the order. This repeats
until the sorted version of the initial array emerges.

To make the Merge Sort algorithm:
1. Make a "split" function that cuts a given array in two, and returns the halves.
    a. It's fine to have a half with one more element in it, it'll get worked out later.
2. Make a "merge" function that takes two arrays and orders their elements in a new array.
    a. Have two counters 'a' and 'b', one to go over each array given.
    b. While both counters are < their array's length, compare arrA[a] and arrB[b], and append the lower
       of the two to the return array (or higher if sorting in descending order).
    c. Once done, return the merged array.
3. Make a "merge_sort" function that recursively splits a given array into its parts, then merges them
   back together.
    a. If the array is two elements only, call split() on it, call merge() on the halves, and return.
    b. Otherwise, call split(), then call merge_sort() on the halves. After this, have a merge() call to
       merge the resulting subarrays.
'''

# Splits an array in two and returns the halves.
#   - arr (int[]): The array to bisect.
def merge_split(arr):
    # Gotta love Python for making arrays easier to work with :)
    split_index = (int) (len(arr)/2)
    return [arr[:split_index], arr[split_index:]]

# Merges two arrays into a sorted array that is then returned.
#   - arr1 (int[]): The first array to pull elements from.
#   - arr2 (int[]): The second array to pull elements from.
def merge_merge(arr1, arr2):
    a = 0
    b = 0
    ret = []
    while (a < len(arr1)) or (b < len(arr2)):
        if (arr1[a] <= arr2[b]):
            ret.append(arr1[a])
            a += 1
        else:
            ret.append(arr2[b])
            b += 1

#####################################################

import random

seed = random.seed



# Make and return an array of "size" random ints.
# Default is an array of 10 ints in the range 1-10.
#   - size (int): Length/size of the resulting array.
#   - lower (int): Lower bound for the random ints.
#   - upper (int): Upper bound for the random ints.
def make_random_arr(size = 10, lower = 1, upper = 10):
    ret = []
    for a in range(size):
        ret.append(random.randint(lower, upper))
    return ret

# Run sorting algorithm tests for int array sorting algorithms.
# Features predefined arrays and random arrays, with size options.
#   - sort_algo (function): The sorting algorithm to use. Assumes it returns the sorted array "ret" and # of operations "ops" as [ret, ops].
#   - size (int): Length/size of the regular random arrays.
#   - size_big (int): Length/size of the "big" random arrays.
#   - num_rand (int): Amount of regular random arrays to generate.
#   - num_big_rand(int): Amount of "big" random arrays to generate.
#   - lower_rand (int): Lower bound for the ints in the regular random arrays.
#   - upper_rand (int): Upper bound for the ints in the regular random arrays.
#   - lower_big_rand (int): Lower bound for the ints in the "big" random arrays.
#   - upper_big_rand (int): Upper bound for the ints in the "big" random arrays.
def run_tests(sort_algo, size = 10, size_big = 100, num_rand = 5, num_big_rand = 1, lower_rand = 1, upper_rand = 10, lower_big_rand = 1, upper_big_rand = 100):
    # Create arrays for testing.
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    worst_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    unique_arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

    rands = []
    big_rands = []
    
    for a in range(num_rand):
        rands.append(make_random_arr(size, lower_rand, upper_rand))
    for b in range(num_big_rand):
        big_rands.append(make_random_arr(size_big, lower_big_rand, upper_big_rand))

    # Run the sorting algorithm on the arrays, and store the results.
    sorted_results = sort_algo(sorted_arr)
    worst_results = sort_algo(worst_arr)
    unique_results = sort_algo(unique_arr)

    print(sorted_results)
    print(worst_results)
    print(unique_results)

    rand_results = [sort_algo(r) for r in rands]
    big_rand_results = [sort_algo(b) for b in big_rands]
    
    print(f"Sorted array: {sorted_arr}",
          f"Sort applied ({sorted_results[1]} operations): {sorted_results[0]}\n",
          f"Worst-case array: {worst_arr}",
          f"Sort applied ({worst_results[1]} operations): {worst_results[0]}\n\n"
          f"Unique array: {unique_arr}",
          f"Sort applied ({unique_results[1]} operations): {unique_results[0]}\n",
          sep="\n")
    
    for r in range(len(rand_results)):
        print(f"Random array {r+1}: {rands[r]}",
              f"Sort applied ({rand_results[r][1]} operations): {rand_results[r][0]}\n",
              sep="\n")
        
    for b in range(len(big_rand_results)):
        print(f"Big random array {b+1}: {big_rands[b]}\n",
              f"Selection sort applied ({big_rand_results[b][1]} operations): {big_rand_results[b][0]}",
              sep="\n")
        
    print("All done!\n")
    
if __name__ == "__main__":
    run_tests(sort_algo = selection_sort)









