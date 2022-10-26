# ===========================================================
#                        my solution
# ===========================================================
def backward_string(val: str) -> str:
    # your code here
    return val [::-1]


print("Example:")
print(backward_string("val"))

assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")




# ===========================================================
#                     Best "Clear" Solution
# ===========================================================
backward_string = lambda val: val[::-1]

if __name__ == "__main__":
    assert backward_string("val") == "lav"
    assert backward_string("") == ""
    assert backward_string("ohho") == "ohho"
    assert backward_string("123456789") == "987654321"
    

    
    
    

# ===========================================================
#                     Best "Creative" Solution
# =========================================================== 
from operator import itemgetter
backward_string = itemgetter(slice(None, None, -1))

if __name__ == "__main__":
    assert backward_string("val") == "lav"
    assert backward_string("") == ""
    assert backward_string("ohho") == "ohho"
    assert backward_string("123456789") == "987654321"
    
    
    
    
# ===========================================================
#                     Best "Speedy" Solution
# =========================================================== 
def backward_string(val: str) -> str:
    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    
    
    
    
    
    
