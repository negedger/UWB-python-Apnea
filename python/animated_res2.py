import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import savgol_filter, find_peaks

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

samples = []
with open("samplex.txt", "r") as file:
    for line in file:
        sample = line.strip().split(',')  # Adjust the delimiter if needed
        samples.append(float(sample[0]))  # Assuming the first value is the y-coordinate

xar = []
yar = []
smoothed_samples = savgol_filter(samples, window_length=11, polyorder=3)
peaks, _ = find_peaks(smoothed_samples)
valleys, _ = find_peaks(-smoothed_samples)
# Group each peak between two valleys
groups = []
for i in range(len(valleys) - 1):
    valley1 = valleys[i]
    valley2 = valleys[i + 1]
    peaks_between_valleys = [peak for peak in peaks if valley1 < peak < valley2]
    if len(peaks_between_valleys) > 0:
        groups.append((valley1, valley2, peaks_between_valleys))
groups2 = []
for j in groups:
    if (j[2] - j[0]) > 7:
        groups2.append(j)
print("Groups:", groups2[2])


def animate(i):
    xar = []
    yar = []
    smoothed_xar = []
    smoothed_yar = []
    window_size = 100
    start_index = max(0, i - window_size + 10)
    end_index = i + 50

    for index, eachLine in enumerate(samples[start_index:end_index]):
        if float(eachLine) > 1:
            xar.append(index + start_index)  # Use the index as x-axis
            yar.append(float(eachLine))  # Use the sample data as y-axis

    for index, eachLine in enumerate(smoothed_samples[start_index:end_index]):
        smoothed_xar.append(index + start_index)
        smoothed_yar.append(eachLine)

    # Sample data plot
    ax1.clear()
    ax1.plot(xar, yar)
    ax1.set_ylabel("Samples")

    # Smoothed sample data plot
    ax2.clear()
    ax2.plot(smoothed_xar, smoothed_yar, color='red', linewidth=2)
    ax2.set_ylabel("Smoothed Samples")
    ax2.set_xlabel("Index")

    # Scatter plot of peaks
    peak_x = [peak for peak in peaks if start_index <= peak < end_index]
    peak_y = [smoothed_samples[peak] for peak in peak_x]
    ax2.scatter(peak_x, peak_y, color='green', marker='o', label='Peaks')

    # Scatter plot of valleys
    valley_x = [valley for valley in valleys if start_index <= valley < end_index]
    valley_y = [smoothed_samples[valley] for valley in valley_x]
    ax2.plot(valley_x, valley_y, color='blue', marker='o', label='Valleys')
    ax2.legend()

    ax3.clear()
    ax3.plot(smoothed_xar, smoothed_yar, color='black', linewidth=2)
    ax3.set_ylabel("Smoothed Samples")
    ax3.set_xlabel("Index")

    # Plot valley_x and valley_y from groups2
    group_valley_x = [valley for valley in valley_x if valley in range(start_index, end_index) and valley in range(groups[i][0], groups[1][1])]
    group_valley_y = [smoothed_samples[valley] for valley in group_valley_x]
    ax3.plot(group_valley_x, group_valley_y, color='blue', marker='o', label='Group 2 Valleys')

    ax3.legend()


ani = animation.FuncAnimation(fig, animate, frames=len(samples), interval=1, repeat=False)
plt.show()
