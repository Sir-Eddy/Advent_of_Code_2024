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
    for i in range(len(array_a)):
        total_tmp = 0
        for j in range(len(array_b)):
            if array_a[i] == array_b[j]:
                total_tmp += 1
        total += total_tmp * array_a[i]
    print(total)
    


if __name__ == "__main__":
    __main__()