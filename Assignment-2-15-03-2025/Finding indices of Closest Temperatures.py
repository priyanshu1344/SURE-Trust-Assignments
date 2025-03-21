#Question 3: Finding indices of Closest Temperatures 
#Imagine you work for a weather station, and you have a list of temperatures recorded throughout the day. Your job is to find which two temperatures in the list are the most similar (closest in value). Once you find the two closest temperatures, you need to tell their positions (indices) in the list.


def closest_temperatures(arr):
    sorted_indices = sorted(range(len(arr)), key=lambda i: arr[i]) 
    min_diff = float("inf")
    result = (0, 0)

    for i in range(len(sorted_indices) - 1):
        diff = arr[sorted_indices[i + 1]] - arr[sorted_indices[i]]
        if diff < min_diff:
            min_diff = diff
            result = (sorted_indices[i], sorted_indices[i + 1])

    return list(result)

temps = list(map(int, input("Enter temperatures separated by spaces: ").split()))
print("Indices of closest temperatures:", closest_temperatures(temps))
