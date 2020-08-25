
from re import *

#pattern ='[abc]'
#pattern ='[a-z]'
#pattern ='[A-Z]'
#pattern ='[A-Za-z]'
#pattern ='[a-kA-Z]'
#pattern ='[^0-9]'
#pattern ='[^A-Za-z0-9]'
#pattern ='\s'(for space)
#pattern ='\d'(for digit)
#pattern ='\D' (Expect digits)
# pattern='\w'  check for all words
#pattern ='\W'    expect for words

matcher = finditer(pattern,"ab @kji^1Zj*efqbf^qV6+wfoncY_=1293anjHcb LjvEcO")
cont=0
for match in matcher:
    cont+=1

    print(match.start())
    print(match.group())

print("Count : ",cont)