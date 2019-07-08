

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.elements = [None]*size


# Double the size of the given array
def resize_array(arr):
    new_arr = [None]*(arr.size*2)
    for i in range(arr.count):
        new_arr[i] = arr.elements[i]
    arr.size = (arr.size*2)
    arr.elements = new_arr


# Return an element of a given array at a given index
def array_read(arr, index):
    # Throw an error if array is out of the current count
    # Your code here
    if index < 0 or index >= arr.size:
        raise Exception("Index out of bounds error")
        return

    return arr.elements[index]


# Insert an element in a given array at a given index
def array_insert(arr, elem, index):
    # Throw an error if array is out of the current count
    if arr.count > arr.size:
        raise Exception("X")
        return
    # Resize the array if the number of elements is over capacity
    if arr.count == arr.size:
        resize_array(arr)
    # Move the elements to create a space at 'index'
    # Think about where to start!
    for i in range(arr.count, index, -1):
        arr.elements[i] = arr.elements[i-1]

    arr.elements[index] = elem
    arr.count += 1
    return None

    # Add the new element to the array and update the count


# Add an element to the end of the given array
def array_append(arr, elem):

    # Hint, this can be done with one line of code
    # (Without using a built in function)

    # Your code here
    array_insert(arr, elem, arr.count)


# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove(arr, value):
    # Your code here
    for i in range(arr.count):
        if arr.elements[i] == value:
            for j in range(i+1, arr.count):
                arr.elements[j-1] = arr.elements[j]
            arr.elements[arr.count-1] = None
            arr.count -= 1
            break
        i += 1
    else:
        raise Exception("Value not found error")
    return None


# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
def array_pop(arr, index):
    # Throw an error if array is out of the current count
    # Your code here
    if index < 0 or index > arr.count:
        raise Exception("Index out of bounds exception")
        return None

    val = arr.elements[index]
    for j in range(index+1, arr.count):
        arr.elements[j-1] = arr.elements[j]
    arr.elements[arr.count-1] = None
    arr.count -= 1
    return val


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.count):
        string += str(array.elements[i])
        if i < array.count - 1:
            string += ", "

    string += "]"
    print(string)


# # Testing
arr = array(1)

array_insert(arr, "STRING1", 0)
array_print(arr)
array_pop(arr, 0)
array_print(arr)
array_insert(arr, "STRING1", 0)
array_append(arr, "STRING4")
array_insert(arr, "STRING2", 1)
array_insert(arr, "STRING3", 2)
array_print(arr)
