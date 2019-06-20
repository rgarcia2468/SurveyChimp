
import json
def questions():
    #counter= 0
    #dict =
    survey= []
    while True:

        a=input("What question would you like to ask ?: ")
        b= input("Would you like to ask another question? Input 'Yes' or'No': ")
        #counter+=1
        #dict[counter]= a
        survey.append(a)


        if b== "Yes":
            pass

        elif b=="No":
            print("Your survey is now complete.")
            break
        else:
            while True:
                if b!= "No" or b!= "Yes":
                    come_on=input("Please input either 'Yes' or 'No': ")
                    if come_on == "Yes":
                        break
                    elif come_on=="No":
                        print("Your survey is now complete.")
                        break
                    else:
                        pass
            if come_on== "Yes":
                pass
            else:
                break






    with open('finished_survey.txt','w') as json_file:
         json.dump(survey, json_file)

if __name__=='__main__':
    questions()
