"""
mes = input("qué mes usar? ")
"""
mes = "enero"
rank = open("./rank/" + mes + ".txt", "r+")
L = []

for i in rank:
    li = i.rstrip("\n")
    l = li.split()
    l[1] = int(l[1])
    L.append(l)

rank.close()
p = int(len(L))

for k in range(0, p):
    z = k + 1
    w = p - 1 - k
    x = p - k - 2
    while L[w][1] > L[x][1]:
        x = x - 1
    L.insert(x, L[w])
    L.remove(L[w + 1])
    
print(L)

""" antiguo ordenamiento
for k in range(0, p):
    z = 0
    while L[k][1] < L[z][1]:
        z = z + 1
    L.insert(z, L[k])
    L.remove(L[k])
print(L)
"""

""" sobreescritura de datos
with open("./rank/" + mes + ".txt", "w+") as rank:
    for z in range(0, p):
        x = str(L[z])
        rank.write(x)
        rank.write("\n")
"""