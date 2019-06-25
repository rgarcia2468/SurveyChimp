import json
with open("finished_survey.txt", "r+") as a:
    data = json.load(a)
final = {}

for x in data:
    questions = x.split(',')
    for y in questions:
        if y[0] == "O":
            print(str(y[1:]))
            direct= input("Write your answer to the question here: ")
            final[y[1:]]= direct
        else:
            question = y[1:]
            question= question.split("_")
            #top = the question, ans1 = answer choice 1, ans2= answer choice2 ...
            print("{top}\n A.{ans1}\n B.{ans2}\n C.{ans3}\n D.{ans4}".format(top =question[0],ans1= question[1],ans2= question[2],ans3= question[3],ans4=question[4]))
            multiple_choice= input("Enter your Answer choice here:")
            final[question[0]]=multiple_choice

with open('Answered_survey.txt','w') as json_file:
     json.dump(final, json_file)
print("Thank you for taking your time and answering this survey.")
