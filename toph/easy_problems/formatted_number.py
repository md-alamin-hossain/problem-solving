"""
Read an integer variable and print it in which the digits are separated into groups of three by commas.

Input
The input will contain an integer $A$ ($0 \le A < 200000000$).

Output
Print the formatted number.

Sample
Input	Output
1171123
1,171,123
"""

a = int(input())

x = "{:,}".format(a)
print(x)