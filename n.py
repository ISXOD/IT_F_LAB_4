import matplotlib.pyplot as plt
import math
E = 10
C = 0.0001
L = 1
a = 0
t_mass = []
I_mass = []
w0 = math.sqrt(1/C*L)
Ce = E/(L*w0*w0)
Q0 = -Ce
for i in range(1000):
    t = i/1000
    I = -1*Q0*w0*math.sin(w0*t+a)
    t_mass.append(t)
    I_mass.append(I)

plt.plot(t_mass, I_mass)
plt.plot([0, t_mass[-1]], [0, 0])
plt.show()