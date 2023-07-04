import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    pullData = open("samples.txt", "r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []

    window_size = 200
    start_index = max(0, i - window_size + 1)
    end_index = i + 1

    for index, eachLine in enumerate(dataArray[start_index:end_index]):
        if len(eachLine) > 1:
            xar.append(index + start_index)  # Use the index as x-axis
            yar.append(float(eachLine))  # Use the sample data as y-axis

    ax1.clear()
    ax1.plot(xar, yar)

ani = animation.FuncAnimation(fig, animate, frames=len(open("samples.txt", "r").readlines()), interval=1, repeat=False)
plt.show()
