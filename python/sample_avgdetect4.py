import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks

# Read samples from file
samples = []
time_interval = 0.1  # Assuming a time interval of 0.1 seconds between samples

with open("samples.txt", "r") as file:
    for line in file:
        sample = line.strip().split(',')  # Adjust the delimiter if needed
        samples.append(float(sample[0]))  # Assuming the first value is the y-coordinate

# Apply Savitzky-Golay filter for smoothing
smoothed_samples = savgol_filter(samples, window_length=11, polyorder=3)

# Find peaks and valleys in the smoothed data
peaks, _ = find_peaks(smoothed_samples)
valleys, _ = find_peaks(-smoothed_samples)

# Group each pair of peaks and valleys
pairs = []
for peak in peaks:
    closest_valley = min(valleys, key=lambda x: abs(x - peak))
    pairs.append((peak, closest_valley))
# Calculate time between peaks
time_between_peaks = []
absence_of_peak = []

for i in range(len(peaks) - 1):
    time_diff = (peaks[i + 1] - peaks[i]) * time_interval
    time_between_peaks.append(time_diff)
print("time_between_peaks: " + str(time_between_peaks))

# Plot the data
x_values = range(len(samples))

plt.plot(x_values, samples)
plt.plot(x_values, smoothed_samples, color='red', linewidth=2)
plt.xlabel('Sample Index')
plt.ylabel('Y-Value')
plt.title('Sample Plot with Smoothing')

# Plot peaks and valleys
if peaks.any():
    plt.scatter(peaks, [samples[i] for i in peaks], color='blue', label='Peaks')
if valleys.any():
    plt.scatter(valleys, [samples[i] for i in valleys], color='green', label='Valleys')

# Plot pairs of peaks and valleys
if pairs:
    for pair in pairs:
        peak_index, valley_index = pair
        plt.plot([peak_index, valley_index], [samples[peak_index], samples[valley_index]], color='orange', linewidth=2)

plt.legend()
plt.grid(True)
plt.show()
