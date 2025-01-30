def twoSum(nums, target):
    storeComp = {}
    for index, num in enumerate(nums):
        compNum = target - num
        if num in storeComp:
            return [storeComp[num], index]
        storeComp[compNum] = index
    return []

### ********** Test Cases **********

## Basic Case
nums = [2, 7, 11, 15] 
target = 9
output = [0, 1]
if not output == twoSum(nums, target):
    print('1')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Negative Numbers
nums = [-3, 4, 3, 90]
target = 0
output = [0, 2]
if not output == twoSum(nums, target):
    print('2')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Same Element Used Twice
nums = [3, 3]
target = 6
output = [0, 1]
if not output == twoSum(nums, target):
    print('3')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Multiple Pairs
input = nums = [1, 2, 3, 4, 5]
target = 6
output = [1, 3]
if not output == twoSum(nums, target):
    print('4')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Large Numbers
input = nums = [1000000, 500000, 1500000]
target = 2000000
output = [1, 2]
if not output == twoSum(nums, target):
    print('5')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Zero as Target
input = nums = [0, 4, 3, 0]
target = 0
output = [0, 3]
if not output == twoSum(nums, target):
    print('6')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Single Pair
input = nums = [1, 5, 3, 8]
target = 9
output = [0, 3]
if not output == twoSum(nums, target):
    print('7')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## All Negative Numbers
input = nums = [-1, -2, -3, -5]
target = -6
output = [0, 3]
if not output == twoSum(nums, target):
    print('8')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Large Array
input = nums = [1] * 100000 + [2]
target = 3
output = [99999, 100000]
if not output == twoSum(nums, target):
    print('9')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## No Solution (for testing purposes)
input = nums = [1, 2, 3]
target = 7
output = []
if not output == twoSum(nums, target):
    print('10')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Floating Point Numbers
input = nums = [1.5, 2.5, 3.5]
target = 4.0
output = [0, 1]
if not output == twoSum(nums, target):
    print('11')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Mixed Positive and Negative
input = nums = [1, -1, 2, -2]
target = 0
output = [0, 1]
if not output == twoSum(nums, target):
    print('12')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Identical Elements
input = nums = [5, 5, 5, 5]
target = 10
output = [0, 1]
if not output == twoSum(nums, target):
    print('13')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Target is the Sum of Two Largest
input = nums = [1, 2, 3, 4, 5]
target = 9
output = [3, 4]
if not output == twoSum(nums, target):
    print('14')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Target is the Sum of Two Smallest
input = nums = [1, 2, 3, 4, 5]
target = 3
output = [0, 1]
if not output == twoSum(nums, target):
    print('15')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Target is Negative
input = nums = [-1, -2, -3, -4]
target = -3
output = [0, 1]
if not output == twoSum(nums, target):
    print('16')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Target is Zero
input = nums = [1, -1, 2, -2]
target = 0
output = [0, 1]
if not output == twoSum(nums, target):
    print('17')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Two Large Numbers
input = nums = [100, 200, 300, 400]
target = 500
output = [1, 2]
if not output == twoSum(nums, target):
    print('18')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## Target is the Sum of First and Last
input = nums = [10, 20, 30, 50]
target = 60
output = [0, 3]
if not output == twoSum(nums, target):
    print('19')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()

## All Elements Same
input = nums = [7, 7, 7, 7]
target = 14
output = [0, 1]
if not output == twoSum(nums, target):
    print('20')
    print('CAL: ' + str(twoSum(nums, target)))
    print('Should Be: ' + str(output))
    print()