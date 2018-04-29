from string import ascii_uppercase as asc
from itertools import product as d
import re
print("Playfair Cypher: Enter your key and plain text :")
key=input()
text=input()
#key="hmarepasskey"
#text="iskidetailmenhamnhijaengy"
t=lambda x: x.upper().replace('J','I')
s=[]
for _ in t(key+asc):
 if _ not in s and _ in asc:
  s.append(_)
m=[s[i:i+5] for i in range(0,len(s),5)]
enc={row[i]+row[j]:row[(i+1)%5]+row[(j+1)%5] for row in m for i,j in d(range(5),repeat=2) if i!=j}
enc.update({col[i]+col[j]:col[(i+1)%5]+col[(j+1)%5] for col in zip(*m) for i,j in d(range(5),repeat=2) if i!=j})
enc.update({m[i1][j1]+m[i2][j2]:m[i1][j2]+m[i2][j1] for i1,j1,i2,j2 in d(range(5),repeat=4) if i1!=i2 and j1!=j2})
dec = dict((v, key) for key, v in enc.items())

#encoding
l=re.findall(r'(.)(?:(?!\1)(.))?',''.join([_ for _ in t(text) if _ in asc]))
encoded=''.join(enc[a+(b if b else 'X')] for a,b in l)

#decoding
f=re.findall(r'(.)(?:(?!\1)(.))?',''.join([_ for _ in t(encoded) if _ in asc]))
decoded=''.join(dec[a+(b if b else 'X')] for a,b in f)

print("\n_____________________\n\nEncoded: ",encoded,"\nDecoded: ",decoded)


