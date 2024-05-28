str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

if len(str1) != len(str2):
    print("Not Anagrams")
else:
    if sorted(str1) == sorted(str2):
        print("Strings are Anagrams")
    else:
        print("Not Anagrams")
