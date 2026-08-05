class Encrpytion:

    def encrypt(self,s,k):
        result=""

        for ch in s:
            if ch.islower:
                result+=chr((ord(ch)-ord('a')+k)%26+ord('a'))
            if ch.isupper:
                result+=chr((ord(ch)-ord("A")+k)%26+ord("A"))
            else:
                result+=ch

        return result

    def decrypt(self,s,k):
        result=""

        for ch in s:
            if ch.islower:
                result+=chr((ord(ch)-ord('a')-k)%26+ord('a'))
            if ch.isupper:
                result+=chr((ord(ch)-ord("A")-k)%26+ord("A"))
            else:
                result+=ch

        return result
        

s=input()
k=int(input())

ans=Encrpytion()
result1=ans.encrypt(s,k)
result2=ans.decrypt(s,k)
print(result1)
print(result2)