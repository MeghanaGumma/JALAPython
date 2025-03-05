import re

s="Hello123"
match=re.match(r'\w+\d+', s)
print(bool(match))
