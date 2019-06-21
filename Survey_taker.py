import json
with open("finished_survey.txt", "r+") as a:
    data = json.load(a)
final = {}

for x in data:
    questions = x.split(',')
    print(str(questions[0]))
    direct= input("Write your answer to the question here: ")
    final[x]= direct

with open('Answered_survey.txt','w') as json_file:
     json.dump(final, json_file)
print("Thank you for taking your time and answering this survey.")
