def CheckTime(time):
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print("The days, hours, minutes and seconds (d:h:m:s) are as follows:\n%d:%d:%d:%d" % (day, hour, minutes, seconds))

CheckTime(float(input("Enter the input in seconds:")))