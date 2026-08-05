class Counting:
    def count_vowel(self,str):
        count=0
        str=str.lower()
        str=str.replace(" ","")

        for i in str:
            if str in "aeiou":
                count+=1
            else:
                continue


        return count
    
str=input()
ans=Counting()
result=ans.count_vowel(str)
print(result)