def main():
    # open a file for writing and create it if it doesn't exist
    # f = open('textfile.txt','w+')
    f = open('textfile.txt' ,"r")
    if f.mode == "r":
        contents = f.read()
        print contents
    # write some lines of data to the file
    # for i in range(10):
    #     f.write("This is line %d\r\n" % (i+1))

    f.close()
if __name__ == "__main__":
    main()
