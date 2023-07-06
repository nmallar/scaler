# Given a number A, find if it is COLORFUL number or not.
# If number A is a COLORFUL number return 1 else, return 0.
# What is a COLORFUL Number:
# A number can be broken into different consecutive sequence of digits. 
# The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245. 
# This number is a COLORFUL number, since the product of every consecutive sequence of digits is different
# Example 1 :23
# Possible Sub-sequences: [2, 3, 23] where
#  2 -> 2 
#  3 -> 3
#  23 -> 6  (product of digits)
#  This number is a COLORFUL number since product of every digit of a sub-sequence are different. 
 
#  Example 2 :  236
#  Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
#  2 -> 2 
#  3 -> 3
#  6 -> 6
#  23 -> 6  (product of digits)
#  36 -> 18  (product of digits)
#  236 -> 36  (product of digits)
#  This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same. 

