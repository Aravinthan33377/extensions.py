a = input("Enter your filename with it's extension : " )
if (a.__contains__(".py")):
    print("This is a python file")
elif (a.__contains__(".mp4")):
    print("This is a video file")
elif (a.__contains__(".pdf")):
    print("This is a document")
else:
    print("This file format is not available!!!. lot more formats will be available on next version.")
