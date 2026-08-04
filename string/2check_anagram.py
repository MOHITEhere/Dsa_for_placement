#CHECK ANAGRAM OR NOT
# Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., 
# if they contain the same characters with the same frequencies.

# Examples:
# Input: s1 = “geeks”  s2 = “kseeg”
# Output: true
# Explanation: Both the string have same characters with same frequency. So, they are anagrams.

# Input: s1 = "allergy", s2 = "allergyy"
# Output: false
# Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character.
# Since the frequency of characters differs, the strings are not anagrams.

# Input: s1 = "listen", s2 = "lists"
# Output: false
# Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.

class Anagram:

    def check_anagram(self,str1,str2):
        if len(str1)!=len(str2):
            return False 

        hashmap={}
        for i in str1:
            hashmap[i]=hashmap.get(1,0)+1

        for j in str2:
            if j not in hashmap:
                return False 

            else:
                hashmap[j]-=1

        for value,items in hashmap.items():
            if value !=0:
                return False 


        return True

str1=input()
str2=input()
ans=Anagram()
result=ans.check_anagram(str1,str2)
print(result)