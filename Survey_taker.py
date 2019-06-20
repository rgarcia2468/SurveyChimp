import json
survey= open("finished_survey.txt", "r+")
a= survey.read()
b = json.loads(a)
dict = {}
for x in b:
    questions= x.split(',')
    print(str(questions[0]))
    for y in questions:
        direct= input("Write your answer to the Question below: ")
        dict[y]= direct

with open('Answered_survey.txt','w') as json_file:
     json.dump(dict, json_file)
print("Thank you for taking your time and answering this survey.")
