
import json

def there_is_another():
    while True:
        ask_again= input("Would you like to ask another question? Please input either 'Yes' or 'No': ")
        ask_again= ask_again.lower()
        if ask_again== "yes":
            return True
        elif ask_again=="no":
            return False


def questions():
    survey=[]
    ask_more= True
    while ask_more:
        a=input("What question would you like to ask?: ")
        survey.append(a)
        ask_more= there_is_another()

    with open('finished_survey.txt','w') as json_file:
        json.dump(survey, json_file)



if __name__=='__main__':
    questions()
