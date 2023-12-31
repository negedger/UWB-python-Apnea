import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks

# Read samples from file
samples = []
time_interval = 0.1  # Assuming a time interval of 0.1 seconds between samples
samples_per_sec = 10
with open("samplex.txt", "r") as file:
    for line in file:
        sample = line.strip().split(',')  # Adjust the delimiter if needed
        samples.append(float(sample[0]))  # Assuming the first value is the y-coordinate

# print("Original samples:", samples)

# Apply Savitzky-Golay filter for smoothing
smoothed_samples = savgol_filter(samples, window_length=11, polyorder=3)

# print("Smoothed samples:", smoothed_samples)

# Find peaks and valleys in the smoothed data
peaks, _ = find_peaks(smoothed_samples)
valleys, _ = find_peaks(-smoothed_samples)

# print("Peaks:", peaks)
# print("Valleys:", valleys)

# Group each peak between two valleys
groups = []
for i in range(len(valleys) - 1):
    valley1 = valleys[i]
    valley2 = valleys[i + 1]
    peaks_between_valleys = [peak for peak in peaks if valley1 < peak < valley2]
    if len(peaks_between_valleys) > 0:
        groups.append((valley1, valley2, peaks_between_valleys))

# print("Groups:", groups)

groups2 = []
for j in groups:
    # print("j" + str(j [0]))
    if (j[2] - j[0]) > 7:
        groups2.append(j)

# print("groups2", groups2)

# enter apnea and hpopnea periods in seconds
apnea_period = 10
hypopnea_period = 2.1

peak_diff = []
peak_diff_groups = []
hypopnea_group = []

for k in range(len(groups2) - 1):
    peak_d = groups2[k + 1][2][0] - groups2[k][2][0]
    peak_diff.append(peak_d)
    if peak_diff[k] > apnea_period * samples_per_sec:
        # print("peak_differnce groups are : " + str(k))
        peak_diff_groups.append(k)

for k in range(len(groups2) - 1):
    peak_d = groups2[k + 1][2][0] - groups2[k][2][0]
    peak_diff.append(peak_d)
    if peak_diff[k] < hypopnea_period * samples_per_sec:
        hypopnea_group.append(k)

no_of_seconds = len(samples) / 10
no_of_minutes = no_of_seconds / 60
breath_rate_seconds = (len(groups2)) / no_of_minutes
no_of_apnea = len(peak_diff_groups)
no_of_hypopnea = len(hypopnea_group)
no_of_hours = no_of_minutes / 60
AHI_index = (no_of_apnea + no_of_hypopnea) / no_of_hours

print("no_of_minutes data sampled : " + str(no_of_minutes) + " minutes")
print("Breathing rate : " + str(int(breath_rate_seconds)) + " breaths per minute")
print("no of apnea episodes : " + str(no_of_apnea))
print("no of hypopnea episodes : " + str(no_of_hypopnea))
print("no_of_minutes : " + str(no_of_minutes))
print("no_of_hours : " + str(no_of_hours))
print("AHI index : " + str(AHI_index))

if AHI_index < 5.00:
    print("Apnea Severity : Normal")
elif 5 <= AHI_index < 15:
    print("Apnea Severity : Mild")
elif 15 <= AHI_index < 30:
    print("Apnea Severity : Moderate")
elif AHI_index >= 30:
    print("Apnea Severity : Severe")

#'''
# Create separate subplots for each plot
fig, axs = plt.subplots(3, 1, figsize=(10, 20))

# Plot original samples with peaks and valleys
axs[0].plot(samples)
axs[0].set_ylabel('Amplitude')
axs[0].set_title('Original Samples')
axs[0].legend()

# Plot smoothed samples
axs[1].plot(smoothed_samples, color='red', linewidth=2)
axs[1].set_ylabel('Amplitude')
axs[1].set_title('Smoothed Samples')
axs[1].scatter(peaks, [samples[i] for i in peaks], color='blue', label='Peaks')
axs[1].scatter(valleys, [samples[i] for i in valleys], color='green', label='Valleys')

# Plot groups of peaks and valleys
axs[2].plot(smoothed_samples, color='black')
for group in groups2:
    valley1, valley2, peaks_between_valleys = group
    axs[2].plot([valley1, valley2], [samples[valley1], samples[valley2]], color='green', linewidth=2)
    for peak in peaks_between_valleys:
        axs[2].plot([peak, peak], [samples[valley1], samples[peak]], color='orange', linewidth=2)
axs[2].set_xlabel('Sample Index')
axs[2].set_ylabel('Amplitude')
axs[2].set_title('Groups of Peaks and Valleys')

plt.tight_layout()
plt.show()
#'''
