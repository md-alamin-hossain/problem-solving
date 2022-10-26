# ===========================================================
#                        my solution
# ===========================================================
def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False

print("Example:")
print(is_even(2))

assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")




# ===========================================================
#                     Best "Clear" Solution
# ===========================================================
def is_even(num: int) -> bool:
    return num & 1 == 0


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")




# ===========================================================
#                  Best "Creative" Solution
# ===========================================================
def is_even(num: int) -> bool:
    return bin(num)[-1]=='0'


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    
    
    
# ===========================================================
#                  Best "Speedy" Solution
# ===========================================================
def is_even(num: int) -> bool:
    # your code here
    return not(num & 1)

    # think it faster than num %2 

if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
    




