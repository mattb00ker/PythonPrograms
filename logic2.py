student_score = 91
total_marks = 100

def percentage(score, total):
    perc = score/total*100
    print(perc)
    return(perc)

def grade(student_score, total_marks):
    perc = percentage(student_score, total_marks)

    if (perc >= 90):
        print("Grade 9")
    elif(perc >= 80 and perc < 90):
        print("Grade 8")
    elif(perc >= 70 and perc < 80):
        print("Grade 7")
    elif(perc >= 60 and perc < 70):
        print("Grade 6")
    elif(perc >= 50 and perc < 60):
        print("Grade 5")
    elif(perc >= 40 and perc < 50):
        print("Grade 4")
    elif(perc >= 30 and perc < 40):
        print("Grade 3")
    elif(perc >= 20 and perc < 30):
        print("Grade 2")
    elif(perc >= 10 and perc < 20):
        print("Grade 1")
    else:
        print("Let's move on...")

grade(student_score, total_marks)

