try:
    file1 = open("test.txt", "r")
    read_content = file1.read()
    print(read_content)

finally:

    file1.close()

