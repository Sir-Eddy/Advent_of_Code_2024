def readfile():
    with open('list2.txt', 'r') as f:
        return f.readlines()

def check_if_sorted(array):
    return array == sorted(array) or array == sorted(array, reverse=True)

def numcheck(array):
    for i in range(len(array) - 1):
        distance = abs(array[i + 1] - array[i])
        if distance < 1 or distance > 3:
            return False
    return True

def array_check_main():
    lines = readfile()
    total = 0
    for line in lines:
        temp_array = list(map(int, line.split()))
        if check_if_sorted(temp_array) and numcheck(temp_array):
            total += 1
        else:
            for i in range(len(temp_array)):
                retry_array = temp_array[:i] + temp_array[i+1:]
                if check_if_sorted(retry_array) and numcheck(retry_array):
                    total += 1
                    break
    print(total)

def __main__():
    array_check_main()

if __name__ == "__main__":
    __main__()