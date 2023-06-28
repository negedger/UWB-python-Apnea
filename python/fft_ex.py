import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of sample points
N = 600
# Sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# Plotting the input sample
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(x, y)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Amplitude')
axs[0].set_title('Input Sample')

# Plotting the Fourier Transform
axs[1].plot(xf, 2.0/N * np.abs(yf[:N//2]))
axs[1].set_xlabel('Frequency')
axs[1].set_ylabel('Amplitude')
axs[1].set_title('Fourier Transform')

plt.tight_layout()
plt.show()
