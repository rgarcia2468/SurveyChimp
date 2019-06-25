class Question(Exception):
    def __init__(self, this):
        self.message = this


    a = input("What question would you like to ask today?: ")
    b = input("Would you like to ask another question? Input 'Yes' or 'No': ")

    try:
        if b=="Yes":
            raise Question("this")
    except:
        input("What question would you like to ask?: ")
        input("Would you like to ask another question? input 'Yes' or 'No': ")
    else:
        print("Your survey is now complete.")
