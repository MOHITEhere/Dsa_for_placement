#convert lower to upper and upper to lower case 


class Convert:
    def convert_the_case(self,str):
        result=""
        for ch in str:
            if ch.islower():
                result+=ch.upper()
            elif ch.isupper():
                result+=ch.lower()
            else:
                result+=ch

        return result

    #pythonic way
    text_input = input("Enter text: ")
    print(text_input.swapcase()) 

str=input()
ans=Convert()
result=ans.convert_the_case(str)
print(result)