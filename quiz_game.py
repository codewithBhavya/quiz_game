print("welcome to the python quiz game")
print("Note : if your spelling is wrong then the answer will be considered incorrect")
total_questions = 10
# user_score = 0
question = str(input("what is the full form of PHP \n"))
correct_ans = "personal home page"
if question == correct_ans:
    user_score_1 = 1
    print("Congrats! you are absolutely correct ")
else:
    user_score_1 = 0
    print("You are wrong! try again")
question = str(input("what is the name of the founder of java \n"))
correct_ans = "james gosling"
if question == correct_ans:
    user_score_2 = 1
    print("Congrats! you are absolutely correct")
else:
    user_score_2 = 0
    print("You are wrong! try again")
question = str(input("what is the another name of java \n"))
correct_ans = "oak"
if question == correct_ans:
    user_score_3 = 1
    print("Congrats! you are absolutely correct")
else:
    user_score_3 = 0
    print("You are wrong! try again")
question = str(input("what is the full form of GUI \n"))
correct_ans = "graphical user interface"
if question == correct_ans:
    user_score_4 = 1
    print("Congrats! you are absolutely correct")
else:
    user_score_4 = 0
    print("You are wrong! try again")
question = str(input("what is the full form of CLI \n"))
correct_ans = "command line interface"
if question == correct_ans:
    user_score_5 = 1
    print("Congrats! you are absolutely correct")
else:
    user_score_5 = 0
    print("You are wrong! try again")
question = str(input("What do the letters HTML, a markup language used to create web pages, stand for? \n"))
correct_ans = "hypertext markup language"
if question == correct_ans:
    user_score_6 = 1
    print("Congrats! you are absolutely correct")
else:
    user_score_6 = 0
    print("You are wrong! try again")
question = str(input("Fonts that contain small decorative lines at the end of a stroke are known as what? \n"))
correct_ans = "serif fonts"
if question == correct_ans:
    user_score_7 = 1
    print("Congrats! you are absolutely correct")
else:
    user_score_7 = 0
    print("You are wrong! try again")
question = str(input("The companies HP, Microsoft and Apple were all started in a what? \n"))
correct_ans = "garage"
if question == correct_ans:
    user_score_8 = 1
    print("Congrats! you are absolutely correct")
else:
    user_score_8 = 0
    print("You are wrong! try again")
question = str(input("In database programming, SQL is an acronym for what? \n"))
correct_ans = "structured query language"
if question == correct_ans:
    user_score_9 = 1
    print("Congrats! you are absolutely correct")
else:
    user_score_9 = 0
    print("You are wrong! try again")
question = str(input("In a website browser address bar what does www stand for? \n"))
correct_ans = "world wide web"
if question == correct_ans:
    user_score_10 = 1
    print("Congrats! you are absolutely correct")
else:
    user_score_10 = 0
    print("You are wrong! try again")
# user_score_0 = str(user_score)
# print("your total score is: ")
user_score = user_score_1 + user_score_2 + user_score_3 + user_score_4 + user_score_5 + user_score_6 + user_score_7 + user_score_8 + user_score_9 + user_score_10
user_score_str = str(user_score)
print("your score is "+user_score_str)
accuracy_percentage = str(user_score/total_questions*100)
print("Your Accuracy Percentage is " + accuracy_percentage)