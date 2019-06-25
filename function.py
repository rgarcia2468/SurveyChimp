import json
survey= []
def there_is_another():
    while True:
        ask_again= input("Would you like to ask another question? Please input either 'Yes' or 'No': ")
        ask_again= ask_again.lower()
        if ask_again== "yes":
            return True
        elif ask_again=="no":
            return False
def multiple_choice():

    q1= input("Enter Your question: ")
    mca= input("Enter answer choice A: ")
    mcb = input("Enter answer choice B: ")
    mcc = input("Enter answer choice C: ")
    mcd = input("Enter answer choice D: ")
    all_of_it= 'M' + q1+"_"+mca+ "_"+mcb+ "_"+ mcc+"_"+mcd
    survey.append(all_of_it)
    with open('finished_survey.txt','w') as json_file:
        json.dump(survey, json_file)



def open_ended():


    a="O" + input("What question would you like to ask? : ")
    survey.append(a)
    #ask_more= there_is_another()

    with open('finished_survey.txt','w') as json_file:
        json.dump(survey, json_file)

def which_one():
    while True:
        question= input("What type of question would you like to ask? Input 'Open ended' or 'Multiple choice': " )
        question = question.lower()
        if question== "multiple choice":
            one = multiple_choice()
            break
        elif question== "open ended":
            two= open_ended()
            break
        else:
            pass

def questions():
    ask_more= True
    while ask_more:
        start= which_one()
        ask_more = there_is_another()
    print("Your survey is now complete.")


if __name__=='__main__':
    questions()
