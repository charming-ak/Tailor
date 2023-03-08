print("exam results")
marks = 35
if marks==35:
    print("you have promoted marks:",marks)
elif marks>35:
    print("you passed the Exam!")
    if marks >75 and marks <=85:
        print("you got good marks:",marks)
    elif marks>85 and marks <=95:
        print("you got distinction marks:",marks)
    elif marks>95:
        print("you got the best marks:",marks)
    else:
        print("do well to get good,distinction,best marks",marks)
else:
    print("you failed the exam marks:",marks)