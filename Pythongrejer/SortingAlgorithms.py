data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

# Sortera data naivt, dvs använda brute force-metoder. Selection sort och insertion sort använder hela data-settet, t sk fr Merge sort och Quick sort som tillämpar divide and conquer på datan.

# SELECTION SORT
# Replaced Bubble sort. Both have O(n^2) but selection sort performs fewer exchanges.

for scanIndex in range(0, len(data)):
    minIndex = scanIndex

    for compIndex in range(scanIndex + 1, len(data)):
        if data[compIndex] < data[minIndex]:
            minIndex = compIndex

    if minIndex != scanIndex:
        data[scanIndex], data[minIndex] = \
            data[minIndex], data[scanIndex]
        print(data)

# Detta ger:
# [1, 5, 7, 4, 2, 8, 9, 10, 6, 3]
# [1, 2, 7, 4, 5, 8, 9, 10, 6, 3]
# [1, 2, 3, 4, 5, 8, 9, 10, 6, 7]
# [1, 2, 3, 4, 5, 6, 9, 10, 8, 7]
# [1, 2, 3, 4, 5, 6, 7, 10, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# INSERTION SORT (Best case är O(n). Ex när hela setet redan är sorterat. Worst case är om hela setet är ordnat i reverse order, då blir det O(n^2))

for scanIndex in range(1, len(data)):
    temp = data[scanIndex]

    minIndex = scanIndex

    while minIndex > 0 and temp < data[minIndex - 1]:
        data[minIndex] = data[minIndex - 1]
        minIndex -= 1

    data[minIndex] = temp
    print(data)

# Detta ger:
# [5, 9, 7, 4, 2, 8, 1, 10, 6, 3]
# [5, 7, 9, 4, 2, 8, 1, 10, 6, 3]
# [4, 5, 7, 9, 2, 8, 1, 10, 6, 3]
# [2, 4, 5, 7, 9, 8, 1, 10, 6, 3]
# [2, 4, 5, 7, 8, 9, 1, 10, 6, 3]
# [1, 2, 4, 5, 7, 8, 9, 10, 6, 3]
# [1, 2, 4, 5, 7, 8, 9, 10, 6, 3]
# [1, 2, 4, 5, 6, 7, 8, 9, 10, 3]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Smarter techniques:
# MERGE SORT
# Applies divide and conquer. Worst case O(n log n), så snabbare än de två föregående.
# Denna första funktion delar elementen REKURSIVT och sätter ihop dem igen.


def mergeSort(list):
    # Determine whether the list is broken into
    # individual pieces.
    if len(list) < 2:
        return list

    # Find the middle of the list.
    middle = len(list)//2

    # Break the list into two pieces.
    left = mergeSort(list[:middle])  # rekursion
    right = mergeSort(list[middle:])  # rekursion

    # Merge the two sorted pieces into a larger piece.
    print("Left side: ", left)
    print("Right side: ", right)
    merged = merge(left, right)
    print("Merged ", merged)
    return merged

# Andra funktionen sätter ihop de två sidorna ITERATIVT.


def merge(left, right):
    # When the left side or the right side is empty,
    # it means that this is an individual item and is
    # already sorted.
    if not len(left):
        return left
    if not len(right):
        return right

    # Define variables used to merge the two pieces.
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    # Keep working until all of the items are merged.
    while (len(result) < totalLen):

        # Perform the required comparisons and merge
        # the pieces according to value.
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

        # When the left side or the right side is longer,
        # add the remaining elements to the result.
        if leftIndex == len(left) or \
                rightIndex == len(right):
            result.extend(left[leftIndex:]
                          or right[rightIndex:])
            break

    return result


mergeSort(data)

# Detta ger:
# Left side:  [9]
# Right side:  [5]
# Merged  [5, 9]
# Left side:  [4]
# Right side:  [2]
# Merged  [2, 4]
# Left side:  [7]
# Right side:  [2, 4]
# Merged  [2, 4, 7]
# Left side:  [5, 9]
# Right side:  [2, 4, 7]
# Merged  [2, 4, 5, 7, 9]
# Left side:  [8]
# Right side:  [1]
# Merged  [1, 8]
# Left side:  [6]
# Right side:  [3]
# Merged  [3, 6]
# Left side:  [10]
# Right side:  [3, 6]
# Merged  [3, 6, 10]
# Left side:  [1, 8]
# Right side:  [3, 6, 10]
# Merged  [1, 3, 6, 8, 10]
# Left side:  [2, 4, 5, 7, 9]
# Right side:  [1, 3, 6, 8, 10]
# Merged  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# QUICK SORT
# Delar datan med en pivot point. Söker iterativt efter element som är på fel plats och swappar dem. När detta inte längre går, bryts loopen och en ny pivot sätts. Den rekursiva  delen nedan hanterar vänstra och högra sidan.


def partition(data, left, right):
    pivot = data[left]
    lIndex = left + 1
    rIndex = right

    while True:  # the iterative part.
        while lIndex <= rIndex and data[lIndex] <= pivot:
            lIndex += 1
        while rIndex >= lIndex and data[rIndex] >= pivot:
            rIndex -= 1
        if rIndex <= lIndex:
            break
        data[lIndex], data[rIndex] = \
            data[rIndex], data[lIndex]
        print(data)

    data[left], data[rIndex] = data[rIndex], data[left]
    print(data)
    return rIndex


def quickSort(data, left, right):  # the recursive part
    if right <= left:
        return
    else:
        pivot = partition(data, left, right)
        quickSort(data, left, pivot-1)
        quickSort(data, pivot+1, right)

    return data


quickSort(data, 0, len(data)-1)

# Detta ger:
# [9, 5, 7, 4, 2, 8, 1, 3, 6, 10]
# [6, 5, 7, 4, 2, 8, 1, 3, 9, 10]
# [6, 5, 3, 4, 2, 8, 1, 7, 9, 10]
# [6, 5, 3, 4, 2, 1, 8, 7, 9, 10]
# [1, 5, 3, 4, 2, 6, 8, 7, 9, 10]
# [1, 5, 3, 4, 2, 6, 8, 7, 9, 10]
# [1, 2, 3, 4, 5, 6, 8, 7, 9, 10]
# [1, 2, 3, 4, 5, 6, 8, 7, 9, 10]
# [1, 2, 3, 4, 5, 6, 8, 7, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
