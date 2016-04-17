# utils-python
Simple python utilities and data types

## Setup
``python setup.py install``

## Usage
````
from myutils import adt
nums = [9,8,7,6]
heap = adt.Heap(nums)
heap.push(2)
val = heap.pop()
print nums
````
