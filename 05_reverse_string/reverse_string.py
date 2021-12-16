def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]


print(reverse_string('awesome'))
print(reverse_string('sauce'))

# Method 2
v = 'awesome'
print("".join(reversed(v)))


# Method 3
def reverse_string3(phrase):
    output = ''
    for x in phrase:
        output = x + output
    return output
print("Method 3")
print(reverse_string3('awesome'))
print(reverse_string3('sauce'))
# Method 3 implementation
#  Time complexity: O(n)
#  Space complexity: not O(n), string is immutable.
#    using string concatenation, every time a string is concatenate, each string is allocated memory and then the combined string is allocated memory


# Method 4
def reverse_string4(phrase):
    output = []
    for x in range(len(phrase)-1, -1, -1):
        output.append(phrase[x])
    return ''.join(output)
# Method 4 implementation
#  Time complexity: O(n)
#  Space complexity: O(n)
#    python join() combine the string together once, allocate memory once for the whole reversed string
print("Method 4")
print(reverse_string4('awesome'))
print(reverse_string4('sauce'))


# Method 5
def reverse_string5(phrase):
    output = [None] * len(phrase)
    idx = len(phrase) - 1
    for x in phrase:
        output[idx] = x
        idx -= 1
    return ''.join(output)
# Method 5 implementation (similar to 4)
#  Time complexity: O(n)
#  Space complexity: O(n)
#    python join() combine the string together once, allocate memory once for the whole reversed string

print("Method 5")
print(reverse_string5('awesome'))
print(reverse_string5('sauce'))


