import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
with open("samples.txt", "r") as file:
    data = file.read().splitlines()

# Convert data to a list of floats
data = [float(sample) for sample in data]

# Calculate the average
average = np.mean(data)
print("Average: " + str(average))
threshold = average * 0.002
print("Threshold: " + str(threshold))

# Detect peaks
positive_peaks = []
negative_peaks = []
for i in range(1, len(data)-1):
    if data[i] > average + threshold and data[i-1] <= average - threshold:
        positive_peaks.append(i)
    if len(negative_peaks) < len(positive_peaks):
        if data[i] < average + threshold and data[i-1] >= average - threshold:
            negative_peaks.append(i)
            #print("Negative Peaks: " + str(len(negative_peaks)))
            #print("Positive Peaks: " + str(len(positive_peaks)))
"""
for i in range(len(positive_peaks)):
    if((positive_peaks[i]-negative_peaks[i]) < 1.00):
        #del positive_peaks[i]
        print("Positive Peak removed: " + str(i))
"""
print("Positive Peaks: " + str(positive_peaks))
print("Negative Peaks: " + str(negative_peaks))

# Calculate time between peaks
time_between_peaks = []
for i in range(min(len(positive_peaks), len(negative_peaks))):
    time_between_peak = (negative_peaks[i] - positive_peaks[i]) / 10  # Assuming 10 samples recorded per second
    print("Time Between Peaks: " + str(time_between_peaks))

    if time_between_peak > 3:
        print("No respiration")
    elif time_between_peak < 1:
        print("Distorted wave")
    else:
        time_between_peaks.append(time_between_peak)

print("Time Between Peaks: " + str(time_between_peaks))

# Count peaks per second
peaks_per_second = len(positive_peaks) / (len(data) / 10)  # Assuming 10 samples recorded per second
print("Peaks per Second: " + str(peaks_per_second))

# Plot values and graph
plt.subplot(2, 1, 1)
plt.plot(data)
plt.title("Sample Values")

plt.subplot(2, 1, 2)
plt.plot(data, color='black')
plt.title("Time Between Peaks")
plt.ylabel("Time (s)")
plt.xlabel("Peak Index")

if time_between_peaks[1] <= 3.00:
    print("ok")

for i in range(min(len(positive_peaks), len(negative_peaks))):
    time_between_peak = (negative_peaks[i] - positive_peaks[i]) / 10  # Assuming 10 samples recorded per second
    if time_between_peak < 3:
        plt.plot(positive_peaks[i], data[positive_peaks[i]], 'ro')  # 'ro' for red circle marker
        plt.plot(negative_peaks[i], data[negative_peaks[i]], 'bo')  # 'bo' for blue circle marker
"""
for i in range(min(len(positive_peaks), len(negative_peaks))):
    #if 1.00 <= time_between_peaks[i] <= 3.00:
        plt.plot(positive_peaks[i], data[positive_peaks[i]], 'ro')  # 'ro' for red circle marker
        plt.plot(negative_peaks[i], data[negative_peaks[i]], 'bo')  # 'bo' for blue circle marker
    elif time_between_peaks[i] > 3:
        plt.text(positive_peaks[i], data[positive_peaks[i]], "No respiration", verticalalignment='bottom')
    else:
        plt.text(positive_peaks[i], data[positive_peaks[i]], "Distorted wave", verticalalignment='bottom')
"""
plt.axvspan(positive_peaks[1], negative_peaks[1], color='yellow', alpha=0)

plt.show()
