
a = input("What will your first question be?: ")
b =input("What will your second question be? :")
c = input("What will your third question be? :")
d = input("What will your fourth question be? :")



question_list = [
    (a),

    (b),

    (c),

    (d),
]

def questions():

    for each_question in question_list:
        print(each_question )
        get_answer = input()



if __name__ == '__main__':
    questions()
