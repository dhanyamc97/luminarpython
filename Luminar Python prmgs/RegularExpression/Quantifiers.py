import re
#pattern ='a+'
#pattern='a*'
#pattern='a?'
#pattern='a{2}'
pattern='a{2,3}'

matcher = re.finditer(pattern,"aababababababaaababbbbbabaaaab")

count=0
for match in matcher:
    count+=1
    print(match.start())
    print(match.group())

print(count)
