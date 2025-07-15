import matplotlib.pyplot as plt

r = 0
x0 = 0.5
N = 100

x = [x0]

for i in range(N):
    x.append(r * x[i] * (1 - x[i]))

print(x)

plt.plot(x)

plt.show()
