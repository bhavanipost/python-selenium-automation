#4*[Not required]. Solve Amazon interview question:
#Create a function that will take a string as an input and return the 1st unique letter of a string.
#“Google” => “l”
#“Amazon” => “m”
#If there are no unique letters, return an empty string: “xoxoxo” => “”.
#How would you test it? How would you handle edge cases?

# def unique(string: str):
#     string = string.lower()
#     for l in string:
#         if string.count(l) == 1:
#             return l
# print(unique('google'))


# def unique(string: str):
#     string = string.lower():
#     #d = {'g' : 2, '0' : 2, 'l' = 1, 'e' = 1}
#     d = {}
#     for letter in string:
#         if letter not in d:
#             d[letter] = 1
#         else:
#             d[letter] += 1
#         print(d)
#
#         for k, v in d.items():
#             if v == 1:return k
# print(unique('google'))


def unique(string: str):
    # Google => google
    string = string.lower()  # google

    d = {}
    for letter in string: # O(n)
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

    # print(d) # d = {'g': 2, 'o': 2, 'l': 1, 'e': 1}

    for k, v in d.items(): # O(n)
        if v == 1:
            return k
    return ''
    # O(n)

print(unique('google'))
print(unique('Google'))
print(unique(''))
print(unique('amazon'))
