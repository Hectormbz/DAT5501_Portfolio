import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import perf_counter
# read data

csv_path = r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\asset prices\HistoricalData_1760959707604.csv"
df = pd.read_csv(csv_path)

# Ensure 'Close/Last' is float
df['Close/Last'] = df['Close/Last'].str.replace('$','').astype(float)
#creates list of daily price changes
dailyChanges = df['Close/Last'].diff().dropna().to_numpy()
print(dailyChanges)
# n values to test sorting time
ns = np.arange(7, 366)
# Time the sorting
times = []
for n in ns:
    sample = dailyChanges[:n].astype(float)  # view of first n daily changes
    sample = np.array(sample) #make sample numpy array
    t0 = perf_counter()
    np.sort(sample)
    t1 = perf_counter()
    t = t1 - t0
    times.append(t)

#make lists into numpy arrays
ns = np.array(ns)
times = np.array(times)

# get n log n
nlog = (ns * np.log2(ns))/1000000000


# Plot results
plt.figure(figsize=(8,5))
plt.plot(ns, times, label='Measured sort time (s)', marker='o', markersize=4)
plt.plot(ns, nlog, label='n·log2(n)', linestyle='--')
plt.xlabel('n (number of ΔP elements sorted)')
plt.ylabel('Time (seconds)')
plt.title('Sorting time T vs n  — compare with n·log n')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
