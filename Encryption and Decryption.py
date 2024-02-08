import random
import string
str=input("Enter a string: ")
key=int(input("Enter a key(the number of string you want to encrypt or decrypt till): "))
str1=str.split(" ")
print("Do you want to encrypt or decrypt the string?")
print("Input 1 for encrypt and 2 for decrypt")
choice=int(input("Enter your choice: "))
special_characters="@#$%&*!?/;:"
if choice==1:
  nwords=[]
  for word in str1:
    if(len(word)>=3):
      r1=''.join(random.choices(string.ascii_lowercase+string.digits+special_characters, k=key))
      r2=''.join(random.choices(string.ascii_lowercase+string.digits+special_characters, k=key))
      strnew=r1+word[1:]+word[0]+r2
      nwords.append(strnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
elif choice==2:
  nwords=[]
  for word in str1:
    if(len(word)>=key):
      strnew=word[key:-key]
      strnew=strnew[-1]+strnew[:-1]
      nwords.append(strnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))