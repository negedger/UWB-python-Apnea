import numpy as np
import matplotlib.pyplot as plt

# Read the samples from the file
samples = np.loadtxt('samples.txt')

# Perform FFT on the samples
fft_result = np.fft.fft(samples)
fft_result = np.roll(fft_result, -2)  # Shift the array to remove the first two samples
# Get the magnitude spectrum
magnitude_spectrum = np.abs(fft_result)

# Get the corresponding frequency values
sampling_rate = 100 # Assuming a sampling rate of 1 (you can adjust this according to your data)
frequency_values = np.fft.fftfreq(len(samples), d=1/sampling_rate)

# Plot the FFT
plt.plot(frequency_values, magnitude_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('FFT Spectrum')
plt.grid(True)
plt.show()
