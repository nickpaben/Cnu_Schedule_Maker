from tkinter import *
import os


class ErrorMessage:

    def __init__(self, message):
        self.root = Tk()
        self.root.configure(width=280, height=160, background='#E6E6D7')
        self.root.title("Error")
        self.counter = 0
        self.iterations = 0
        while self.counter < len(message):
            if self.counter+43 < len(message):
                space_search = 43
                while message[self.counter + space_search] != " " and space_search > 0:
                    space_search -= 1
                if space_search != 0:
                    space_search += 1
                    self.message = Label(self.root, text=message[self.counter:self.counter+space_search],
                                         background='#E6E6D7')
                    self.counter += space_search

                else:
                    space_search = 43
                    self.message = Label(self.root, text=message[self.counter:self.counter+space_search]+'-',
                                         background='#E6E6D7')
                    self.counter += space_search
            else:
                self.message = Label(self.root, text=message[self.counter:], background='#E6E6D7')
                self.counter += 43
            self.message.place(x=0, y=self.iterations*20)
            self.iterations += 1
        self.root.mainloop()


class OldSchedule:

    def __init__(self):

        self.root = Tk()
        self.root.configure(width=550, height=750)
        self.root.title("Final Exam Schedule 2020")
        canvas = Canvas(self.root, width=550, height=750)
        canvas.place(x=0, y=0)
        img = PhotoImage(file="Data\spring_2020_exam_schedule.png")
        canvas.create_image(0, 0, anchor=NW, image=img)

        self.root.mainloop()


class AddInformation:

    def __init__(self):
        self.root = Tk()
        self.root.configure(width=350, height=250)
        self.root.title("Add_Information")
        self.root.config(background='#E6E6D7', )


if __name__ == "__main__":
    OldSchedule()
    ErrorMessage("I am the Glob-glo-gab-galab The shwabble-dabble-wabble-gabble flibba blabba blab I'm full of shwibbly"
                 " liber-kind I am the yeast of thoughts and minds"
                 "  Shwabble dabble glibble glabble schribble shwap glab Dibble dabble shribble shrabbl"
                 "e glibbi-glap shwap Shwabble dabble glibble glabble shwibble shwap-dap Dibble dabble shribble shrabbl"
                 "e glibbi-shwap glab Oooh, ha ha ha, mmm, splendid Simply delicious Ooooohm, ha haa ha ha "
                 " I am the Glob-glo-gab-galab The "
                 "shwabble-dabble-wabble-gabble flibba blabba blab I'm full of shwibbly liber-kind I am the yeast of "
                 "thoughts and minds Shwabble dabble "
                 "glibble glabble schribble shwap glab Dibble dabble shribble shrabble glibbi-glap shwap Shwabble "
                 "dabble glibble glabble shwibble shwap-dap Dibble dabble shribble shrabble glibbi-shwap glab  "
                 "Ahhh, Splendid WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
                 "iiiiiiiiiiiiii@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
