from collections import Counter

def makeAnagram(a, b):
    freq_a = Counter(a)
    freq_b = Counter(b)
    
    total_deletions = 0
    all_chars = set(freq_a.keys()).union(set(freq_b.keys()))
    
    for char in all_chars:
        total_deletions += abs(freq_a.get(char, 0) - freq_b.get(char, 0))

    return total_deletions

a = input("Enter the first string: ").strip().lower()
b = input("Enter the second string: ").strip().lower()

print("Minimum deletions required:", makeAnagram(a, b))
