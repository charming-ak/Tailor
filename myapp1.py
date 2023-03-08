def add(*nums):
    result = 0
    value = 0
    for x in nums:
        result+=x
        value+=x
    return result,value
anil,z=add(21,5,71,25,37)
print(anil,z)


