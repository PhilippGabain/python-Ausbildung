def sum_subsequence(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


def create_subsequence(arr, startIndex, length):
    subsequence = []
    for i in range(startIndex, startIndex + length):
        subsequence.append(arr[i])
    return subsequence


def firstPositiveNumber(arr):
    for i in arr:
        if i > 0:
            return arr.index(i)
    return None


def max_sequence(arr):
    max_subsequence = []
    startIndex = firstPositiveNumber(arr)
    if startIndex is None:
        return max(arr)
    for i in range(startIndex, len(arr)):
        for j in range(len(arr) + 1 - i):
            subsequence = create_subsequence(arr, i, j)
            if sum_subsequence(subsequence) > sum_subsequence(max_subsequence):
                max_subsequence = subsequence
    return sum_subsequence(max_subsequence)


sequence = [1,2,-4,4,5]
print(max_sequence(sequence))