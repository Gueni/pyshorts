
data_set  = [0,6,12,3,88,77,15,17,69]
target    = 15
def iterartive_binary_search(data_set,target):
    low  = 0
    high = len(data_set)-1

    while (low <= high):
        mid = (low+high)//2
        if target== data_set[mid]:
            return True
        elif target < data_set[mid]:
            high = mid -1
        elif target > data_set[mid]:
            low  = mid +1
    return False

print(iterartive_binary_search(data_set,target))