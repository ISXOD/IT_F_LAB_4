import matplotlib.pyplot as plt
import math
E = 10
C = 0.1
L = 1
a = 0
t_mass = []
q_mass = []
w0 = math.sqrt(1/C*L)
Ce = E/(L*w0*w0)
for i in range(4000):
    t = i/1000
    q = Ce*(1-math.cos(w0*t))
    t_mass.append(t)
    q_mass.append(q)
plt.title("Зависимость q(t)")
plt.xlabel("t")
plt.ylabel("q(t)")
plt.plot(t_mass, q_mass)
plt.plot([0, t_mass[-1]], [0, 0])
plt.show()