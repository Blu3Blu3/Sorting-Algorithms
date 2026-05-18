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

# Split an array in two and returns the halves.
#   - arr (int[]): The array to bisect.
def merge_split(arr):
    # Gotta love Python for making arrays easier to work with :)
    split_index = (int) (len(arr)/2)
    return [arr[:split_index], arr[split_index:]]

# Merge two arrays into a sorted array that is then returned, plus how many operations it took.
#   - arr1 (int[]): The first array to pull elements from.
#   - arr2 (int[]): The second array to pull elements from.
def merge_merge(arr1, arr2):
    a = 0
    b = 0
    ret = []
    while (a < len(arr1)) or (b < len(arr2)):
        # If arr1's elements are already in, add from arr2.
        if a >= len(arr1):
            ret.append(arr2[b])
            b += 1
        # If arr2's elements are already in, add from arr1.
        elif b >= len(arr2):
            ret.append(arr1[a])
            a += 1
        # Otherwise, do the comparison as normal.
        elif (arr1[a] <= arr2[b]):
            ret.append(arr1[a])
            a += 1
        else:
            ret.append(arr2[b])
            b += 1
    # In all honesty, I'm not sure if each insertion is counted as an operation or the whole "merge" function is one operation...
    # I'll just leave this implementation here for now.
    return [ret, len(ret)]
            
# Run Merge Sort on an array and returns the sorted version, plus how many iterations it took.
#   - arr (int[]): The array to be sorted.
def merge_sort(arr):
    ops = 0
    # If the array is just one element or empty, return it.
    if len(arr) <= 1:
        #print(f"Single: {arr}")
        return [arr, 1]
    # Otherwise, perform Merge Sort recursively.
    else:
        # Split the array first...
        halves = merge_split(arr)
        ops += 1
        
        # Perform Merge Sort on the left and right halves created from the split...
        #print(f"Halves: {halves}")
        left_results = merge_sort(halves[0])
        left = left_results[0]
        ops += left_results[1]
        right_results = merge_sort(halves[1])
        right = right_results[0]
        ops += right_results[1]
        
        # And return the merged array made from the halves.
        results = merge_merge(left, right)
        ops += results[1]
        return [results[0], ops]
        

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
              f"Sort applied ({big_rand_results[b][1]} operations): {big_rand_results[b][0]}",
              sep="\n")
        
    print("\nAll done!\n")
    
if __name__ == "__main__":
    run_tests(sort_algo = merge_sort, size_big = 1000, lower_rand = -10, lower_big_rand = -100)
