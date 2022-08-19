######################################################################################################################
# Given a string s representing a roman numeral. Convert s into an integer.

# Problem Note

# s is guaranteed to be within the range from 1 to 3999.
# Roman numerals are represented by seven different symbols :
# SYMBOL       VALUE
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For instance, three is written as III in Roman numeral, just three ones added together.
# Eleven is written as, XI, which is simply X + I. The number fifty-six is written as LVI, which is just L + V + I.
# Roman numerals are usually written greatest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# We see that the one is before the five, so we subtract one from five to make it four.
# The same principle applies to the number forty, which is written as XL.
# There are six instances where subtraction is used:

# I is placed before V (5) and X (10) to form 4 and 9.
# X is placed before L (50) and C (100) to form 40 and 90.
# C is placed before D (500) and M (1000) to form 400 and 900.

# Example 1

# Input: "VII"
# Output: 7
# Explanation:
#       V+I+I = 5+1+1 = 7
#######################################################################################################################

def romanToInt(s: str) -> int:
    roman = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40,
             "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    i = 0
    num = 0
    N = len(s)

    while i < N:
        if i+1 < N and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num


if __name__ == "__main__":
    TC_list = ["LVII", "III", "CDXLIII"]
    print([romanToInt(TC) for TC in TC_list])
