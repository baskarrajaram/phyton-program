def reverseString(s):
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)
input_str = "hello"
reversed_str = reverseString(input_str)
print(reversed_str) 
