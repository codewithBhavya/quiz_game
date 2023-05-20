import random
import pygame
print("welcome to the python quiz game")
print("Note : if your spelling is wrong then the answer will be considered incorrect")
pygame.mixer.init()
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
questions_hint = {
    "What is the full form of PHP": "It's a recursive acronym that refers to its primary purpose.",
    "what is the name of the founder of java": "His first name is the same as a popular Indonesian island.",
    "what is the another name of java": "It shares its name with a popular caffeinated beverage.",
    "what is the full form of GUI": "It refers to the graphical representation of a user interface.",
    "what is the full form of CLI": "It refers to a text-based interface for interacting with a computer's operating system.",
    "What do the letters HTML, a markup language used to create web pages, stand for?": "It describes the structure and content of web pages.",
    "Fonts that contain small decorative lines at the end of a stroke are known as what?": "These lines are often seen in calligraphy and can add elegance or flair to the text.",
    "The companies HP, Microsoft and Apple were all started in a what?": "It refers to a specific location or environment where entrepreneurs and innovators bring their ideas to life.",
    "In database programming, SQL is an acronym for what?": "It describes the language used to communicate with and manipulate relational databases.",
    "In a website browser address bar what does “www” stand for?": "It stands for a common prefix used to identify a specific type of web resource.",
    "Regarding data storage, what does the acronym SSD stand for?": "It refers to a type of storage device that has no moving parts.",
    "What does DNS stand for?": "It is a vital component of the internet that translates domain names into numerical IP addresses.",
    "What is the name of the first spreadsheet program?": "It shares its name with a mathematical grid used for calculations and organizing data.",
    "what does url stand for?": "It describes the address used to locate and access resources on the web.",
    "what does ISP stand for": "It refers to the company or organization that provides internet access to users.",
    "What does the acronym “lol” stand for when used in phone texts and on the internet?": "It is an expression used to indicate laughter or amusement in a casual online conversation.",
    "HTML and CSS are computer languages used to create what?": "They are essential for designing and building the visual and structural elements of a certain type of digital content.",
    "In a photo editing program, what do the letters RGB stand for?": "It refers to the primary colors used to create a wide range of colors on digital displays.",
    "In 1975 an engineer created the first electronic camera while working for what company?": "This company is well-known for its innovation and technological advancements in the field of electronics and consumer products.",
    "Created in 2009, what was the first decentralized cryptocurrency?": "It was introduced by an anonymous person or group using the pseudonym Satoshi Nakamoto.",
    "What does the acronym USB stand for when referring to a computer port?": "It describes a widely used standard for connecting various devices to computers.",
    "Mark Zuckerberg was one of the founders of which social networking site?": "This platform's name refers to the compilation of individual profiles and connections.",
    "who is the founder of Facebook": "He is an American entrepreneur and philanthropist, known for his involvement in various controversies surrounding Facebook.",
    "On which popular website do users send tweets?": "It is a platform characterized by short, concise messages limited to 280 characters.",
    "What do the letters CPU stand for when referring to the “brains” of a computer?": "It is often considered the central processing unit and is responsible for executing instructions and performing calculations in a computer.",
    "What was the first publicly traded U.S. company to reach a $1 trillion market cap?": "It is a technology company known for its groundbreaking products, including iPhones, iPads, and Mac computers.",
    "A modulator-demodulator is a hardware device better known as what?": "It is commonly used to establish internet connections over telephone lines.",
    "To celebrate its 30th birthday in 2010, Google placed a playable version of what arcade game on its homepage?": "It is a classic game where players control a little yellow character trying to eat dots and avoid ghosts.",
    "What is the smallest unit of measurement in a computer?": "It is the fundamental building block of digital information and is represented by a binary digit.",
    "What is the name of the operating system developed by Apple Inc.?": "Its name is inspired by a type of fruit commonly associated with knowledge or enlightenment."
}
score = 0 
random_questions = random.sample(list(questions.keys()),10)
for question in random_questions:
    print(question)
    user_response = input("your answer :")
    correct_response = questions[question]
    if user_response == correct_response:
        sound_file = "correct_sound.mp3"
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        score +=1
        print("Congrats! you are absolutely correct")
    else:
        sound_file = "wrong_sound.mp3"
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        print("You are wrong! try again")
        hint_user_input = input("Do you want a hint for this condition (Yes/No)")
        hint_user_choice = str(hint_user_input)
        hint = questions_hint.get(question)
        if hint_user_input == "yes":
            print({hint})
        else:
            print("Ok please continue with the next question")
score_concatenate = str(score)
print("your score is " + score_concatenate)
percentage_score = str(score/10*100)
print("Your score in the form of percentage is " + percentage_score + "%")
