from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        number = simpledialog.askinteger(title="High-Low Game", prompt="Guess a number between 1-100")
        if number == random_num:
            messagebox.showinfo(title="High-Low Game", message="Correct!")
            sys.exit()
        if number > random_num:
            messagebox.showinfo(title="High-Low Game", message="Your answer is too high")
        else:
            messagebox.showinfo(title="High-Low Game", message="Your answer is too low")

        # 4. Ask the user for a guess using a pop-up window, and save their response

        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program

        # 7. if the guess is high
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low
    messagebox.showerror(title="High-Low Game", message="You Lost :[")
    # 11. Outside of the loop, tell the user they lost

    window.mainloop()
