# 5. Google's
"""Return first index of each occurance of substring in the string

Substring = ‘baby’
String= ’cryingbaby baby’

output (6, 11)
"""

def first_indices(input_string, substring):
    result = []
    start = 0
    while start < len(input_string) - len(substring):
        a = input_string.find(substring, start)
        result.append(a)
        start = a + len(substring)-1
    print(result)


sub = 'baby'
string_a = 'cryingbaby baby'
new_sub = "child"
first_indices(string_a, sub)