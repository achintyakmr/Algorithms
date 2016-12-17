#!/usr/bin/env python

"""Peak_Finder.py: Finds if a peak exists in a 1D or 2D array and returns it"""

__author__ = "Achintya Kumar"


def peak1d(list_a):
    """Returns a peak in a 1D array with complexity O(log n)"""
    start = 0
    end = len(list_a)
    while(True):
        mid = (start + end)//2
        if mid > 0 and list_a[mid] < list_a[mid - 1]:
            end = mid
        elif mid < len(list_a) - 1 and [mid] < list_a[mid + 1]:
            start = mid
        else:
            return [list_a[mid], mid]


def peak2d(list_a):
    """Returns a peak in a 2D array with complexity O(n log m)"""
    start = 0
    end = len(list_a[0])
    while(True):
        j = (start + end)//2
        col_max = peak1d([row[j] for row in list_a])
        if j > 0 and col_max[0] < list_a[col_max[1]][j - 1]:
            end = j
        elif j < end - 1 and col_max[0] < list_a[col_max[1]][j + 1]:
            start = j
        else:
            return [col_max[0], col_max[1], j]


def main():
    list_test_a = [6, 85, 45, 21, 7, 84, 36, 12, 4, 45, 6, 7, 2, 9, 1]
    result = peak1d(list_test_a)
    print("The peak value is: {} at index {}".format(result[0], result[1]))
    list_test_b = [[5, 21, 65, 78, 45], [7, 45, 89, 23, 79],
                   [45, 19, 82, 35, 47], [56, 27, 53, 46, 55]]
    result = peak2d(list_test_b)
    print("The peak value is: {} at index ({}, {})"
          .format(result[0], result[1], result[2]))


if __name__ == "__main__":
    main()
