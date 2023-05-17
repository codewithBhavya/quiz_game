import random
questions = {
    "What is the full form of PHP": "personal home page",
    "what is the name of the founder of java": "james gosling",
    "what is the another name of java": "oak",
    "what is the full form of GUI": "graphical user interface",
    "what is the full form of CLI": "command line interface",
    "What do the letters HTML, a markup language used to create web pages, stand for?": "hypertext markup language",
    "Fonts that contain small decorative lines at the end of a stroke are known as what?": "serif fonts",
    "The companies HP, Microsoft and Apple were all started in a what?": "garage",
    "In database programming, SQL is an acronym for what?": "structured query language",
    "In a website browser address bar what does “www” stand for?": "world wide web",
    "Regarding data storage, what does the acronym SSD stand for?": "solid state drive",
    "What does DNS stand for?": "domain name system",
    "What is the name of the first spreadsheet program?": "visicalc",
    "what does url stand for?": "uniform resource locator",
    "what does ISP stand for": "internet service provider",
    "What does the acronym “lol” stand for when used in phone texts and on the internet?": "laugh out loud",
    "HTML and CSS are computer languages used to create what?": "website",
    "In a photo editing program, what do the letters RGB stand for?": "red green and blue",
    "In 1975 an engineer created the first electronic camera while working for what company?": "kodak",
    "Created in 2009, what was the first decentralized cryptocurrency?": "bitcoin",
    "What does the acronym USB stand for when referring to a computer port?": "universal serial bus",
    "Mark Zuckerberg was one of the founders of which social networking site?": "facebook",
    "who is the founder of Facebook": "mark zuckerberg",
    "On which popular website do users send tweets?": "twitter",
    "What do the letters CPU stand for when referring to the “brains” of a computer?": "central processing unit",
    "What was the first publicly traded U.S. company to reach a $1 trillion market cap?": "apple",
    "A modulator-demodulator is a hardware device better known as what?": "modem",
    "To celebrate its 30th birthday in 2010, Google placed a playable version of what arcade game on its homepage?": "pacman",
    "What is the smallest unit of measurement in a computer?": "bit",
    "What is the name of the operating system developed by Apple Inc.?": "macos"
}
score = 0 
random_questions = random.sample(list(questions.keys()),10)
for question in random_questions:
    print(question)
    user_response = input("your answer :")
    correct_response = questions[question]
    if user_response == correct_response:
        score +=1
        print("Congrats! you are absolutely correct")
    else:
        print("You are wrong! try again")
score_concatenate = str(score)
print("your score is " + score_concatenate)
percentage_score = str(score/10*100)
print("Your score in the form of percentage is " + percentage_score)
# code is successful till here
