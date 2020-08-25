# import re module

import re

matcher = re.finditer("ab","ababababababababbbbbabab")

count=0
for match in matcher:
    count+=1
    print(match.start())
    print(match.group())

print(count)
