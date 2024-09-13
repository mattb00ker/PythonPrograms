student_score = 80
total_marks = 100
target = 7

def percentage(score, total):
    perc = score/total*100
    print(perc)
    return(perc)

def grade(student_score, total_marks, target):
    perc = percentage(student_score, total_marks)

    if (perc >= 90 and 9 - target  >= -1):
        print("Grade 9")
    elif(perc >= 80 and 8 - target >= -1):
        print("Grade 8")
    elif(perc >= 70 and 7 - target >= -1):
        print("Grade 7")
    elif(perc >= 60 and 6 - target >= -1):
        print("Grade 6")
    elif(perc >= 50 and 5 - target >= -1):
        print("Grade 5")
    elif(perc >= 40 and 4 - target >= -1):
        print("Grade 4")
    elif(perc >= 30 and 3 - target >= -1):
        print("Grade 3")
    elif(perc >= 20 and 2 - target >= -1):
        print("Grade 2")
    elif(perc >= 10 and 1 - target >= -1):
        print("Grade 1")
    else:
        print("You'll need to try the test again")


grade(student_score, total_marks, target)

