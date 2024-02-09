import math

# Variables
'''
r Clasificación
RD Desviación de la clasificación
o Volatilidad
m Clasificacion Glicko 2
f Desviacion Glicko 2
P Cantidad de partidas
i,k Variables de itineración
J0 Datos del jugador
Ji Datos del contrincante
J Colección de datos
si Resultado de la partida
S Colección de resultados
g(h) Función de f
gi Función g(i)
E(m0, m, G) Función de m, mi, g(h)
Ei Función E(i)
vi Varianzas estimadas
V0 Colección de varianzas
V Sumatoria de varianzas
di Mejoras estimadas
d Colección de mejoras
D Sumatoria de mejoras
t Constante del sistema
e Tolerancia de convergenia
a,A,B,C Variables del proceso
F(x) Función de x
'''

# Proceso matemático
r = float(input("Clasificación: "))
RD = float(input("Desviación: "))
o = float(input("Volatilidad: "))
m = (r - 1500) / 173.7178
f = RD / 173.7178
J0 = [r, RD, o, m, f]
J = [J0]
S = []
V0 = []
d = []
P = int(input("Cuántas partidas? "))

for i in range(0, P):
    r = float(input("Clasificación " + str(i + 1) + ": "))
    RD = float(input("Desviación " + str(i + 1) + ": "))
    o = float(input("Volatilidad " + str(i + 1) + ": "))
    m = (r - 1500) / 173.7178
    f = RD / 173.7178
    Ji = [r, RD, o, m, f]
    J.append(Ji)

for i in range(P):
    si = int(input("Resultado " + str(i + 1) + ": "))
    S.append(si)


def g(h):
    return (1 + 3 * (h ** 2) / math.pi ** 2) ** -0.5


def E(m0, m, G):
    return (1 + math.exp(-G * (m0 - m))) ** -1


for i in range(P):
    gi = g(J[i + 1][4])
    Ei = E(J[0][3], J[i + 1][3], gi)
    vi = (gi ** 2 * Ei * (1 - Ei))
    V0.append(vi)

V = sum(V0) ** -1

for i in range(P):
    gi = g(J[i + 1][4])
    Ei = E(J[0][3], J[i + 1][3], gi)
    di = gi * (S[i] - Ei)
    d.append(di)

D = V * sum(d)

# Iteración
t = 0.5
e = 0.000001
a = math.log((J[0][2] ** 2), math.exp(1))
k = 1


def F(x):
    return ((math.exp(x) * (D ** 2 - J[0][4] ** 2 - V - math.exp(x))) / (2 * (J[0][4] ** 2 + V + math.exp(x)) ** 2)) - (
            x - a) / t ** 2


A = a

if D ** 2 > (J[0][4] ** 2 + V):
    B = math.log((D ** 2 - J[0][4] ** 2 - V), math.exp(1))
else:
    while F(a - k * t) < 0:
        k = k + 1
    B = a - k * t

FA = F(A)
FB = F(B)

while abs(B - A) > e:
    C = A + (A - B) * FA / (FB - FA)
    FC = F(C)
    if FC * FB < 0:
        A = B
        FA = FB
    else:
        FA = FA / 2
    B = C
    FB = FC

# Nuevos datos
o = math.exp(A / 2)
fn = (J[0][4] ** 2 + o ** 2) ** 0.5
f = ((1 / fn ** 2) + (1 / V)) ** -0.5
RD = (173.7178 * f)
m = J[0][3] + f ** 2 * sum(d)
r = 173.7178 * m + 1500
J0 = [r, RD, o, m, f]
print(J0)
