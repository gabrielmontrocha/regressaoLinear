import pandas as pd
import matplotlib.pyplot as plt

i = [1, 2, 3, 4, 5, 6, 7]
nCiclos = [1, 10, 100, 1000, 10000, 100000, 1000000]
tensaoMPa = [1100, 1000, 925, 800, 625, 550, 420]
data = { "N° de Ciclos":nCiclos, "Tensão, MPa":tensaoMPa}
fadiga = pd.DataFrame(data = data, index=i)
fadiga.sort_values("Tensão, MPa", ascending=False, inplace=True)

nCiclos = fadiga["N° de Ciclos"]
tensaoMPa = fadiga["Tensão, MPa"]
n = len(fadiga)


def regressao_simples(x, y, n):
    sum_x = sum(x)
    sum_x2 = sum((x**2))
    sum_y = sum(y)
    sum_y2 = sum((y**2))
    sum_x_y = sum(y*x)

    b0 = (sum_y*sum_x2 - (sum_x*sum_x_y))/ ((n*sum_x2) - (sum_x**2))

    b1 = ((n*sum_x_y) - (sum_x*sum_y))/ ((n*sum_x2) - sum_x**2)
    print("y = {} + {}x  ".format(b0,b1))
    return b0,b1

b0, b1  = regressao_simples(nCiclos,tensaoMPa, n)

plt.scatter(nCiclos, tensaoMPa)

plt.xlabel('N° de Ciclos')
plt.ylabel('Tensão')
plt.title('Gráfico de Dispersão')

plt.ticklabel_format(style='plain')

plt.show()

