# quicksort

import random


def qsort(l: list) -> list:
    if len(l) <= 1:
        return l
    else:
        # Choose a pivot (usually the first element)
        pivot = l[0]
        # Elements smaller than the pivot
        less_than_pivot = [x for x in l[1:] if x <= pivot]
        # Elements greater than the pivot
        greater_than_pivot = [x for x in l[1:] if x > pivot]
        # Recursively apply quicksort to the partitions and combine
        return qsort(less_than_pivot) + [pivot] + qsort(greater_than_pivot)


# main
if __name__ == "__main__":

    # Generate a list of 10,000 random integers between 1 and 100,000
    random_numbers = [random.randint(1, 100000) for _ in range(10000)]

    # print(random_numbers)
    # unsorted_list = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = qsort(random_numbers)
    print("Sorted List:", sorted_list)
