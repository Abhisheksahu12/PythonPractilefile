def readData(read, write, char):

    fread = open(read, 'rt')
    fwrite = open(write, 'wt')

    i = 1
    temp = ""
    for x in fread:
        temp += x
        if i % 2 != 0:
            fwrite.write(x)
        i += 1
    print("Given character appeared", temp.count(char), "times.")
    fread.close()
    fwrite.close()


readData("FILE1.txt", "FILE2.txt", "a")
