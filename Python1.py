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
print(s == s[::-1])

# Vowel Removal
print(s.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', ''))

# Word Reversal
print(' '.join(reversed(s[::-1].split(' '))))

# Strictly Increasing
print(nums == list(set(nums)))

# Negative Flattening
print([0 if n < 0 else n for n in nums])

# Digit Sum
print([n for n in range(100) if (n % 10 + n // 10) % 5 == 0])

# Climate Change
# sort years before last n years and n years (but reversed) separately and combine them respectfully
temps = sorted(temps[:len(temps) - n]) + sorted(temps[len(temps) - n:len(temps)], reverse=True)
# just in case wanted to know the last 0 years...
if n == 0:
    print(n)
for x in range(1, n + 1):
    # just in case the last n years is all the temps... last 140 years of all 140 temps
    if n == len(temps):
        print(n)
        break

    # temps[len(temps) - n - 1] is the highest temp of the years before last n years
    if temps[len(temps) - n - 1 + x] < temps[len(temps) - n - 1]:
        print(x-1)
        break
