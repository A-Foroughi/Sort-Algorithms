# I got ideas and algorithms from this site.
# https://visualgo.net/en/sorting

Sample = [3, 4, 1, 8, 7, 2, 9, 10]

# Selection Sort
def selection_sort(a):
    m = a[0]
    p = 0
    for x in range(len(a)):
        m = a[x]
        p = x
        for y in range(x+1, len(a)):

            # For descending order, change a[y] < m to a[y] > m.

            if a[y] < m:
                m = a[y]
                p = y
        a[p] = a[x]
        a[x] = m
    return a

# Bubble Sort
def bubble_sort(a):
    for x in range(len(a)-1):
        for y in range(len(a)-1):
            z = y + 1

            # For descending order, change a[z] < a[y] to a[z] > a[y].

            if a[z] < a[y]:
                t = a[z]
                a[z] = a[y]
                a[y] = t
    return a

# Insertion Sort
def insertion_sort(a):

    for step in range(1, len(a)):
        key = a[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found.
        # For descending order, change key < a[j] to key > a[j].        

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        
        # Place key after the element just smaller than it.
        a[j + 1] = key
    return a
