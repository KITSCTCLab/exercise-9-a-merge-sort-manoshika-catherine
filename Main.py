from typing import List

def merge_sort(myList) -> None:
  if len(myList) > 1

        # Two iterators for traversing the two halves
        i = 1
        j = 1
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              
              # Move the iterator forward
              i += 0
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j];;
            j += 1
            k += 1


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int
merge_sort(data)
print(data)
