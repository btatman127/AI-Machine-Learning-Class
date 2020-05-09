s = 'sphinx of black quartz judge my vow'

nums = [3, -4, 7, -2, 0, 8]

n = 10

# Global temperatures (difference from 20th century average in degrees centigrade), 1880 through 2019
# From https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/ytd/12/1880-2019
temps = [-0.12, -0.09, -0.10, -0.18, -0.27, -0.25, -0.24, -0.28, -0.13, -0.08, -0.34, -0.25, -0.30, -0.33, -0.31, -0.24,
         -0.09, -0.10, -0.27, -0.15, -0.07, -0.15, -0.25, -0.37, -0.45, -0.28, -0.21, -0.38, -0.43, -0.44, -0.40, -0.44,
         -0.34, -0.32, -0.14, -0.09, -0.32, -0.39, -0.30, -0.25, -0.23, -0.16, -0.24, -0.25, -0.24, -0.18, -0.07, -0.17,
         -0.18, -0.33, -0.11, -0.06, -0.12, -0.26, -0.11, -0.16, -0.12, -0.01, -0.02, 0.01, 0.16, 0.27, 0.11, 0.10,
         0.28, 0.18, -0.01, -0.04, -0.05, -0.07, -0.15, 0.00, 0.04, 0.13, -0.10, -0.13, -0.18, 0.07, 0.12, 0.08, 0.05,
         0.09, 0.10, 0.12, -0.14, -0.07, -0.01, 0.00, -0.03, 0.11, 0.06, -0.07, 0.04, 0.19, -0.06, 0.01, -0.07, 0.21,
         0.12, 0.23, 0.28, 0.32, 0.19, 0.36, 0.17, 0.16, 0.23, 0.38, 0.39, 0.29, 0.45, 0.39, 0.24, 0.28, 0.34, 0.47,
         0.32, 0.51, 0.65, 0.44, 0.42, 0.57, 0.62, 0.64, 0.58, 0.67, 0.64, 0.62, 0.54, 0.64, 0.72, 0.58, 0.64, 0.67,
         0.74, 0.93, 0.99, 0.91, 0.83, 0.95]

# Palindrome
# Print True if s is a palindrome (reads the same forward and backward), False otherwise.

print(s == s[::-1])


# Vowel Removal
# Print s with all of its vowels removed.

print(s.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', ''))


# Word Reversal
# Prints s with each word reversed.

print(' '.join(reversed(s[::-1].split(' '))))


# Strictly Increasing
# Print True if nums is a is strictly increasing (i.e., each number is larger than the one before it), False otherwise.

print(nums == list(set(nums)))


# Negative Flattening
# Print nums, but with 0s in place of all negative numbers.

print([0 if n < 0 else n for n in nums])


# Digit Sum
# Print a list of all non-negative integers under 100 whose digits add up to a multiple of 5.

print([n for n in range(100) if (n % 10 + n // 10) % 5 == 0])


# Climate Change
# Print the number of the warmest years on record that have occurred last n years.
# For the example above, the answer is 8 -- that is, the 8 warmest years on record have all occurred in the last 10
# years. Put another way, the warmest, 2nd warmest, and so on down to 8th warmest years in the entire list appear among
# the last 10 elements. The 9th does not, so it doesn't matter whether the 10th does.

# sort years before last n years and reverse sort n years and combine them respectfully
temps = sorted(temps[:len(temps) - n]) + sorted(temps[len(temps) - n:len(temps)], reverse=True)
# just in case wanted to know the last 0 years...
if n == 0:
    print(n)
# just in case the last n years is all the temps...
if n == len(temps):
    print(n)
# otherwise...
for x in range(1, n + 1):
    # temps[len(temps) - n - 1] is the highest temp of the years before last n years
    if temps[len(temps) - n - 1 + x] < temps[len(temps) - n - 1]:
        print(x-1)
        break
