print("*************************************")
print("Welcome to My Quiz Game!!!")

question_bank=[
    {"text":"Who developed Python Programming Language?",
     "answer":"c"},
    {"text": "Which type of Programming does Python support?",
     "answer":"d"},
    {"text":"Is Python case sensitive when dealing with identifiers?",
     "answer":"b" }
]

options=[["a)Wick van Rossum","b) Rasmus Lerdorf","c) Guido van Rossum","d) Niene Stom"],
         ["a)object objectented programming","b) structured programming","c) functional programming","d) all of these"],
         ["a) no" ,"b) yes", "c) machine dependent", "d) none of the mentioned"],
]

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_bank)):
    print("********************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess=input("Enter your answer(a/b/c/d): ")
    is_correct=check_answer(guess,question_bank[question_num]["answer"])

    if is_correct:
        print("correct answer")
        score+=1
    else:
        print("incorrect answer")
        print(f"The correct answer is {question_bank[question_num]['answer']}")
    print(f"Your current score is {score}/{question_num+1}")
print(f"Your have given {score} correct answer")
print(f"Your score is {(score/len(question_bank))*100}%")