path = input("give me your file path: ")

while True:
    try:
        for line in open(path, 'r'):
            print(line)
        break
    except:
        print("something went wrong! please ")
        path = input("give me your file path: ")
