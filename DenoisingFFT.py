import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size': 18})

# Create a simple signal with two frequencies

dt = 0.001
t = np.arange(0, 1, dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)    # Sum of the two frequencies
f_clean = f
f = f + 2.5*np.random.randn(len(t))     # Noise addition to the signal

plt.plot(t, f, color='c', linewidth=1.5, label='Noisy')
plt.plot(t, f_clean, color='k', linewidth=2, label='Clean')
plt.xlim(t[0], t[-1])
plt.legend()

n = len(t)
fhat = np.fft.fft(f, n)     # fast fourier transform
PSD = fhat * np.conj(fhat) / n      # power spectrum (pow per freq)
freq = (1/(dt*n)) * np.arange(n)    # axis of freqs in Hz
L = np.arange(1, np.floor(n/2), dtype='int')    # Only plot the first half of frequencies in the vector

fig, axs = plt.subplots(2, 1)

plt.sca(axs[0])
plt.plot(t, f, color='c', linewidth=1.5, label='Noisy')
plt.plot(t, f_clean, color='k', linewidth=2, label='Clean')
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(freq[L], PSD[L], color='c', linewidth=2, label='Noisy')
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()

# Use the PSD to filter out noise

indices = PSD > 100     # Find all freqs with larger power
PSDclean = PSD * indices    # zero out all other frequencies
fhat = indices * fhat   # Zero out all small fourier coefficients
ffilt = np.fft.ifft(fhat)   # Inverse fft in order to arrive at the filtered time signal

fig, axs = plt.subplots(3, 1)

plt.sca(axs[0])
plt.plot(t, f, color='c', linewidth=1.5, label='Noisy')
plt.plot(t, f_clean, color='k', linewidth=2, label='Clean')
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(t, ffilt, color='k', linewidth=2, label='Filtered')
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[2])
plt.plot(freq[L], PSD[L], color='c', linewidth=1.5, label='Noisy')
plt.plot(freq[L], PSDclean[L], color='k', linewidth=2, label='Filtered')
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()

plt.show()
