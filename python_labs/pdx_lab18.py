# Lab 18: Peaks and Valleys, version 1
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    """returns location of peaks in data"""
    peaks_index = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            peaks_index.append(i)
    return peaks_index

def valleys(data):
    """returns location of valleys in data"""
    valleys_index = []
    for i in range(1, len(data) - 1):
        if data[i] < data[i - 1] and data[i] < data[i + 1]:
            valleys_index.append(i)
    return valleys_index

def peaks_and_valleys(data):
    """returns location of peaks and valleys sorted"""
    p_v_index = []
    p_v_index.extend(peaks(data) + valleys(data))
    return sorted(p_v_index)

print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
