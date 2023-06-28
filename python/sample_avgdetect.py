import matplotlib.pyplot as plt

# Read data from the file
with open("samples.txt", "r") as file:
    data = file.read().splitlines()

# Convert data to a list of floats
data = [float(sample) for sample in data]

# Calculate the average
average = sum(data) / len(data)
print("average: "+str(average))
threshold = average * 0.002
print("threshold: "+str(threshold))

# Detect peaks
peaks = []
peaks2 = []
for i in range(1, len(data)-1):

    if data[i] > average + threshold and data[i-1] <= average - threshold:
        peaks.append(i)
    if len(peaks2) < len(peaks):
        if data[i] < average + threshold and data[i-1] >= average - threshold:
            peaks2.append(i)
            print("peaks2: " + str(len(peaks2)))
            print("peaks: " + str(len(peaks)))
    #print("i: "+str(i))

print("peaks: "+str(peaks))
print("peaks2: "+str(peaks2))

# Count peaks per second
peaks_per_second = len(peaks) / (len(data) / 10)  # Assuming 10 samples recorded per second
print("peaks_per_second: "+str(peaks_per_second))


# Plot values and graph
plt.subplot(1, 1, 1)
plt.plot(data)
plt.title("Sample Values")

plt.subplot(2, 1, 2)
plt.plot(data,color='black')
plt.title("Time Between Peaks")

for peak in peaks:
    plt.plot(peak, data[peak], 'ro')  # 'ro' for red circle marker

for peak in peaks2:
    plt.plot(peak, data[peak], 'bo')  # 'ro' for red circle marker
plt.show()
