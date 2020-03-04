# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        index = i
        smallest_index = index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j



        # TO-DO: swap
        swap = arr[smallest_index]
        arr[smallest_index] = arr[index]
        arr[index] = swap



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_occurred = True
    while swap_occurred:
        swap_occurred = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap_occurred = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr