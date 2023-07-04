import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import savgol_filter

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

samples = []

def animate(i):
    with open("samplex.txt", "r") as file:
        for line in file:
            sample = line.strip().split(',')  # Adjust the delimiter if needed
            samples.append(float(sample[0]))  # Assuming the first value is the y-coordinate

    xar = []
    yar = []
    smoothed_samples = savgol_filter(samples, window_length=11, polyorder=3)

    window_size = 200
    start_index = max(0, i - window_size + 1)
    end_index = i + 1

    for index, eachLine in enumerate(samples[start_index:end_index]):
        if (eachLine) > 1:
            xar.append(index + start_index)  # Use the index as x-axis
            yar.append(float(eachLine))  # Use the sample data as y-axis

    ax1.clear()
    ax1.plot(xar, yar)
    ax1.set_ylabel("Samples")

    smoothed_xar = list(range(start_index, end_index))
    ax2.clear()
    ax2.plot(smoothed_xar, smoothed_samples[start_index:end_index])
    ax2.set_ylabel("Smoothed Samples")
    ax2.set_xlabel("Index")

ani = animation.FuncAnimation(fig, animate, frames=len(open("samples.txt", "r").readlines()), interval=1, repeat=False)
plt.show()
