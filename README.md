# Quiz Game

This is a simple quiz game implemented in Python using the Tkinter library for the GUI and Pygame for sound effects. The game presents a series of multiple-choice questions to the user and provides feedback on their answers. At the end of the quiz, the user's score is displayed.

## Requirements

To run this code, you need to have the following libraries installed:

- `random`
- `tkinter`
- `pygame`
- `inputimeout`

You can install the required libraries using the following command:

```
pip install random tkinter pygame inputimeout
```

## How to Use

1. Import the required libraries:

```python
import random
import tkinter as tk
from tkinter import messagebox
import pygame
from inputimeout import inputimeout, TimeoutOccurred
```

2. Set up the quiz questions and hints:

```python
questions = {
    "What is the full form of PHP": "personal home page",
    ...
}

questions_hint = {
    "What is the full form of PHP": "It's a recursive acronym that refers to its primary purpose.",
    ...
}
```

3. Initialize variables:

```python
score = 0
timer = 10
random_questions = random.sample(list(questions.keys()), 10)
pygame.mixer.init()
```

4. Define the `submit_answer` function to handle user input:

```python
def submit_answer():
    global score
    question = questions_list[current_question_idx]
    user_response = answer_entry.get()
    correct_response = questions[question]
    
    if user_response.lower() == correct_response:
        sound_file = "assets/correct_sound.mp3"
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        score += 1
        messagebox.showinfo("Correct", "Congrats! You are absolutely correct")
    else:
        sound_file = "assets/wrong_sound.wav"
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        messagebox.showinfo("Incorrect", "You are wrong! Try again")
        
        hint_user_input = messagebox.askquestion("Hint", "Do you want a hint for this question?")
        hint = questions_hint.get(question)
        if hint_user_input.lower() == "yes":
            messagebox.showinfo("Hint", hint)

    next_question()
```

5. Define the `next_question` function to move to the next question:

```python
def next_question():
    global current_question_idx
    current_question_idx += 1

    if current_question_idx < len(questions_list):
        question_label.config(text=questions_list[current_question_idx])
        answer_entry.delete(0, tk.END)
    else:
        finish_quiz()
```

6. Define the `finish_quiz` function to display the final score:

```python
def finish_quiz():
    score_concatenate = str(score)
    percentage_score = str(score/10 * 100)
    messagebox.showinfo("Quiz Complete", f"Your score is {score_concatenate}\nYour score in the form of percentage is {percentage_score}%")
    root.destroy()
```

7. Create the GUI using Tkinter:

```python
root = tk.Tk()
root.title("Python Quiz Game")
question_label = tk.Label(root, text=random_questions[0])
question_label.pack()
answer_entry = tk.Entry(root)
answer_entry.pack()
submit_button = tk.Button(root, text="Submit", command=submit_answer)
submit_button.pack()
current_question_idx = 0
questions_list = random_questions
root.mainloop()
```

8. Run the code and enjoy the quiz game!

Please note that the code assumes the presence of sound files ("correct_sound.mp3" and "wrong_sound.wav") in an "assets" folder. You need to make sure that the sound files are available in the correct location or modify the code to use different sound files if desired.

Feel free to modify the code to suit your needs and add more questions to the quiz by updating the `questions` and `questions_hint` dictionaries.
