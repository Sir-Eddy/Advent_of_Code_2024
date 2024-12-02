def readfile():
    with open('list1.txt', 'r') as f:
        return f.readlines()

def __main__():
    lines = readfile()
    total = 0
    array_a = []
    array_b = []
    for line in lines:
        temp_array = list(map(int, line.split()))
        a = temp_array[0]
        array_a.append(a)
        b = temp_array[1]
        array_b.append(b)
    array_a.sort()
    array_b.sort()
    for i in range(len(array_a)):
        if array_a[i] < array_b[i]:
            total += array_b[i] - array_a[i]
        else:
            total += array_a[i] - array_b[i]
    print(total)
    


if __name__ == "__main__":
    __main__()