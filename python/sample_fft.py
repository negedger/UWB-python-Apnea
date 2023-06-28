import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
N = 256
S = 1 #sample start
fs = 10
# Read samples from the text file
filename = 'samples.txt'
samples = np.loadtxt(filename)
samples = samples[S:N]

# Define the number of points for FFT

# Perform N-point FFT
fft_result = fft(samples, N)
fft_result = np.roll(fft_result, -2)  # Shift the array to remove the first two samples
fft_result = fft_result[:-2]  # Remove the last two samples
magnitude = np.abs(fft_result)

# Find the indices of the two highest peaks (excluding the DC component at index 0)
#top_indices = magnitude
top_indices = np.argsort(magnitude)[::-1][0:1]
max_position = np.argmax(magnitude)

#print(fft_result)

# Plot the input samples
plt.subplot(2, 1, 1)
plt.plot(samples)
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.title('Input Samples')
plt.grid(True)

# Plot the FFT result

frequency =np.empty(N)
resprate = np.empty(N)

for i in range(1, N):
    frequency[i] = i * fs / (N)
    resprate[i] = frequency[i] * 60

print("magnitude")
print(magnitude)
print("frequency")
print(frequency)
print("resprate")
print(resprate)


#frequency =np.abs(frequency)

plt.subplot(2, 1, 2)
#plt.plot(resprate[1:N-2], magnitude[1:N-2])  # Adjust the x-axis range to match the updated FFT result size
plt.plot(resprate[1:N-2], magnitude[1:N-2])  # Adjust the x-axis range to match the updated FFT result size

#plt.plot(magnitude)  # Adjust the x-axis range to match the updated FFT result size
plt.xlabel('resp rate')
plt.ylabel('Magnitude')
plt.title('FFT Result')
plt.grid(True)

# Mark the second highest peak
for idx in top_indices:
    plt.plot(idx, magnitude[idx], 'ro', label=f'Max Position {idx}')

#plt.plot(max_position, magnitude[max_position], 'ro', label='Max Position')

plt.legend()
plt.tight_layout()
plt.show()
