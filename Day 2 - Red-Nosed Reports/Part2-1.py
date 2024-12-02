def readfile():
    with open('list2.txt', 'r') as f:
        return f.readlines()

def check_if_sorted(array):
    true_count1 = 0
    true_count2 = 0
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            true_count1 += 1
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            true_count2 += 1
    if true_count1 == len(array)-1 or true_count2 == len(array)-1:
        return True
    else:
        return False

def numcheck(array):
    distance = 0
    for i in range(0, len(array) - 1):
        if array[i + 1] > array[i]:
            distance = array[i + 1] - array[i]
        elif array[i] > array[i + 1]:
            distance = array[i] - array[i + 1]
        if distance < 1 or distance > 3:
            return False
    return True

def __main__():
    lines = readfile()
    total = 0
    sorted = False
    numbers_true = False
    debug_count = 0
    for line in lines:
        debug_count += 1
        temp_array = list(map(int, line.split()))
        sorted = check_if_sorted(temp_array)
        if sorted:
            numbers_true = numcheck(temp_array)
            if numbers_true:
                total += 1
    print(total)

        
    


if __name__ == "__main__":
    __main__()