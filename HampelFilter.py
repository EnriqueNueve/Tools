# Refrence: https://www.mathworks.com/help/dsp/ref/hampelfilter.html

# Import modules
import numpy as np

"""
HampelFilter: Smoothes timeseries by replacing outliers
              with window median value.
Inputs: 1. Flat np.array(x,)
        2. Odd integer declaring window size
        3. Float declaring std threshold for outliers
Outputs: 1. Updated np.array(x,) with replaced outliers
         2. List holding index of outliers from np.array(x,)
"""

def HampelFilter(data,l,std_threshold):
    outlier_index = []

    end = data.shape[0] # States last index to be evaluated
    step = int((l-1)/2) # Distance either way from center of window
    x = int((l-1)/2) # Intial center window index

    p_shift = np.zeros(l-1) # Shift array to evaluate intial elements
    data_shift = np.concatenate((p_shift,data),axis=0)

    while x != (end + step): # Run Hampel Filter over array
        window = data_shift[x - step: x + step + 1]
        mi = np.median(window)

        madi = []
        [madi.append(np.abs(window[i] - mi)) for i in range(len(window))]
        mad = np.median(np.array(madi))
        std = mad*1.4826

        if np.abs(data_shift[x]-mi) > std*std_threshold:
            outlier_index.append(x-l+1)
            data[x-l+1] = mi # Update array to windo median value

        x = x + 1
    return data, outlier_index

window_size = 5
std_threshold = 2

data = np.array([1,2,4,9,23,8,12,4,2])
data,outlier_index = HampelFilter(data,window_size,std_threshold)
print(data)
