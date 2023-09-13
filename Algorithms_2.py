#Task 1. Reverse a negative integer and keep the negative sign at the beginning.
#Example: -189 -> -981

def reverse_integer(n: int):
    string = str(n)
    return int("-" + string[:0:-1])


print(reverse_integer(-123))
print(reverse_integer(-124))


#Task 2. Write a function that takes two strings as input and returns True if they are anagrams of each other, and False otherwise.
#The strings can contain uppercase and lowercase letters, and should be ignored during the comparison.

def are_anagrams(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    if sorted(s1.lower()) == sorted(s2.lower()):
        return True
    else:
        return False

print(are_anagrams("cat", "act"))
print(are_anagrams("hEARt", "earth"))
print(are_anagrams("art", "arc"))



#Task 3. Given a sentence, reverse the order of characters in each word.

def reverse_words(sentence: str):
    list_of_words = sentence.split()
    print(list_of_words)
    empty_list = []
    for word in list_of_words:
        reversed_word = word[::-1]
        empty_list.append(reversed_word)
    print(empty_list)
    joined_words = " ".join(empty_list)

    return(joined_words)

sentence = "Welcome to the world of Python"
print(reverse_words(sentence))

#Task 4. Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.
#Examples:
#“312” should return “333122”
#“102” should return “122



def repeat_digits(s: str):
    result = ""

    for char in s:
        result += char * int(char)
    return (result)


print(repeat_digits("231"))

#Task 5. Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u) in a given string.
#“y” is not considered a vowel for this task. The input string is always in lowercase.

#Examples:
#“hello”     -->  “hll”
#“goodbye”   -->  “gdby”


def shortcut(s: str):
    result = ""
    for char in s:
        if( char not in ('a','e','i','o','u') ):
            result += char

    return(result)

print(shortcut("elephant"))
