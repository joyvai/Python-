from datetime import datetime

def main():
    now = datetime.now()
    print now.strftime("%Y")
    # print now.strftime("%c")
    # print now.strftime("%x")
    print now.strftime("%I:%M:%S %p") 
if __name__ == "__main__":
    main()
