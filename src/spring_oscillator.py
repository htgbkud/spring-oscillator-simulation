import numpy as np
import matplotlib.pyplot as plt

# system parameters
m = 1.0      # mass
k = 4.0      # spring constant
dt = 0.001   # time step
t = np.arange(0, 10, dt)

# massives 
x = np.zeros(len(t))
v = np.zeros(len(t))

# enitial condition
x[0] = 0.1   # initial offset
v[0] = 0.0

# simulation
for i in range(len(t) - 1):
    a = -k / m * x[i]
    v[i + 1] = v[i] + a * dt
    x[i + 1] = x[i] + v[i + 1] * dt
# graph 
plt.plot(t, x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("Колебания пружинного маятника")
plt.show()

if __name__ == "__main__":
    main()
