#Question 4: Strange Sort: Alternating Smallest and Largest 
#In an amusement park ticket queue, visitors are sorted in a strange manner. The smallest number (representing the youngest visitor) stands first, followed by the oldest visitor. The next youngest visitor stands next, followed by the next oldest visitor, and so on. Write a Python program to sort a list of numbers in such a “strange sort,” where the first element is the smallest, the second is the largest, the third is the next smallest, and so on.



def strange_sort(arr):
    arr.sort()
    left, right = 0, len(arr) - 1
    result = []

    while left <= right:
        result.append(arr[left])
        left += 1
        if left <= right:
            result.append(arr[right])
            right -= 1

    return result

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Strange sorted list:", strange_sort(nums))
