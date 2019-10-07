import random

v = []
i = 0
j = 0
t = 10
cMaior = 0
cMenor = 0

while i < t:
    v.append(random.randint(0, 9))
    i += 1

for i in range(t-1):
    for j in range(t-i-1):
        if v[j] > v[j+1]:
            aux = v[j]
            v[j] = v[j+1]
            v[j+1] = aux

for i in range(t-1):
    menor = v[0]
    if v[i] == menor:
        cMenor += 1 

for i in range(t):
    maior = v[0]
    if v[i] > maior:
        maior = v[i]
       
for i in range(t):
    if v[i] == maior:
        cMaior += 1
        
print(v)
print("O menor número é",v[0],", ele se repete",cMenor,"vez(es)")
print("O maior número é",maior,", ele se repete",cMaior,"vez(es)")




