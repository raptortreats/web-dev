import numpy as np

data = [12, 23, 4, 97, 1]
print("mean:", np.mean(data))
print("median:", np.median(data))
print("25th percentile:", np.percentile(data, 25))
print("75th percentile:", np.percentile(data, 75))
print("standard deviation:", np.std(data))
print("variance:", np.var(data))
