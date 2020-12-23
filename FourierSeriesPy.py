import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

plt.rcParams['figure.figsize'] = [8, 8]
plt.rcParams.update({'font.size': 18})

# Define Domain
dx = 0.001
L = np.pi
x = L * np.arange(-1+dx, 1+dx, dx)
n = len(x)
nquart = int(np.floor(n/4))

# Definition of hat function (in this case im defining a hat funtion)
f = np.zeros_like(x)
f[nquart:2*nquart] = (4/n)*np.arange(1, nquart+1) # positive slope
f[2*nquart:3*nquart] = np.ones(nquart) - (4/n)*np.arange(0, nquart) # negative slope

fig, ax = plt.subplots()
ax.plot(x, f, '-', color='k', LineWidth=2)

# Computation of the fourier series (this is an approximation for the limit has been set to 20 iterations)
name = "Accent"
cmap = get_cmap('tab10')
colors = cmap.colors
ax.set_prop_cycle(color=colors)

A0 = np.sum(f * np.ones_like(x)) * dx
fFS = A0/2

A = np.zeros(20)
B = np.zeros(20)
for k in range(20):
    A[k] = np.sum(f * np.cos(np.pi * (k+1) * x / L)) * dx # inner product a(k)
    B[k] = np.sum(f * np.sin(np.pi * (k+1) * x / L)) * dx # inner product b(k)
    fFS = fFS + A[k] * np.cos((k+1)*np.pi*x/L) + B[k]*np.sin((k+1)*np.pi*x/L)
    ax.plot(x, fFS, '-')

# Amplitudes and reconstruction error rate

fFS = (A0/2) * np.ones_like(f)
kmax = 100
A = np.zeros(kmax)
B = np.zeros(kmax)
ERR = np.zeros(kmax)

A[0] = A0/2
ERR[0] = np.linalg.norm(f-fFS)/np.linalg.norm(f)

for k in range(1, kmax):
    A[k] = np.sum(f * np.cos(np.pi * k * x / L)) * dx
    B[k] = np.sum(f * np.sin(np.pi * k * x / L)) * dx
    fFS += A[k] * np.cos(np.pi * k * x / L) + B[k] * np.sin(k * np.pi * x / L)
    ERR[k] = np.linalg.norm(f-fFS)/np.linalg.norm(f)

thresh = np.median(ERR) * np.sqrt(kmax) * (4/np.sqrt(3))
r = np.max(np.where(ERR > thresh))

fig, axs = plt.subplots(2, 1)
axs[0].semilogy(np.arange(kmax), A, color='k', LineWidth=2)
axs[0].semilogy(r, A[r], 'o', color='b', MarkerSize=10)
plt.sca(axs[0])
plt.title('Fourier Coefficients')

axs[1].semilogy(np.arange(kmax), ERR, color='k', LineWidth=2)
axs[1].semilogy(r, ERR[r], 'o', color='b', MarkerSize=10)
plt.sca(axs[1])
plt.title('Error')
plt.show()
