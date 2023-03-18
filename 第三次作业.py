import matplotlib.pyplot as plt
import numpy as np

x=np.array([i for i in range(2001)])
m=1-1/np.exp((x/300))
h=1/np.exp(x/1000)

fig=plt.figure(figsize=(12,12))

plt.subplot(221)
plt.xlabel('$t/(10^{-3}ms)$')
plt.ylabel('$h/h_0$')
plt.plot(x,h)
# plt.xticks([0,1000])
# plt.yticks([])

plt.subplot(222)
plt.xlabel('$t/(10^{-3}ms)$')
plt.ylabel('$m/m_0$')
plt.plot(x,m)

plt.subplot(223)
plt.xlabel('$t/(10^{-3}ms)$')
plt.ylabel('$(m/m_0)^3$')
plt.plot(x,m**3)


plt.subplot(224)
plt.xlabel('$t/(10^{-3}ms)$')
plt.ylabel('$(m/m_0)^3(h/h_0)$')
plt.plot(x,(m**3)*h)
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])

plt.show()