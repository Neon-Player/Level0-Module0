from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    pointScore=0
    # ASK A QUESTION AND CHECK THE ANSWER
    #      // 2.  Ask the user a question 
    question1 = simpledialog.askstring(title="Quiz Game", prompt="What is Barbie's full name?\nCapitalize")
    #      // 3.  Use an if statement to check if their answer is correct
    if question1 == "Barbara Milicent Roberts":
        messagebox.showinfo(title="Quiz Game", message="Correct!\n +1")
        pointScore += 1
    else:
        messagebox.showerror(title="Quiz Game", message="Incorrect\n -1")
        pointScore -= 1

    #       // 4.  if the user's answer was correct, add one to their score

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    question2 = simpledialog.askstring(title="Quiz Game", prompt="What is the answer to life?")
    if question2 == "42":
        messagebox.showinfo(title="Quiz Game", message="Correct!!\n +1")
        pointScore += 1
    else:
        messagebox.showerror(title="Quiz Game", message="Incorrect\n -1")
        pointScore -= 1
    # After all the questions have been asked, tell the user their final score
    str(pointScore)
    print(pointScore)
    # remember to convert your variable to a string using the str() function

    # Run the window's .mainloop() method
    window.mainloop()
