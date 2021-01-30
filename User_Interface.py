from File_Managment import *
from tkinter import *
from Final import *
import os
import numpy as np
# from PIL import Image
import popup


class UserInterface:

    course_list = 'ScheduleOfClasses2020f.csv'

    def __init__(self, path=os.path.join('Data', course_list)):
        self.list_of_finals = []
        self.colors = ['#ff6f6f', '#7e96ff', '#66ff66', '#ffff4d', '#c387ff', '#ff954f', '#5ac891',
                       '#00d1d1', '#d1d1d1', '#9dec00', '#4b87c3', '#ff44ff', '#a3ffd1']
        self.color_counter = 0  # max of 12 used for the 13 element list of colors in previous line
        self.x = 1000
        self.y = 750
        self.path = path
        self.root = Tk()
        self.root.title("Final Schedule Maker")
        self.root.geometry('{}x{}'.format(self.x, self.y))
        self.root.configure(background='#102840')
        # im_temp = Image.open(os.path.join("Data", "cnu_logopng.png"))
        # im_temp = im_temp.resize((124, 124), Image.ANTIALIAS)
        # im_temp.save(os.path.join("Data", "cnu_logopng.png"), "ppm")
        self.photo = PhotoImage(file=os.path.join("Data", "cnu_logopng.png"))
        self.button_qwer = Button(self.root, image=self.photo, command=self.show_schedule)
        self.button_qwer.place(x=873, y=0)
        self.border = PhotoImage(file=os.path.join("Data", "cnuTopBorder.PNG"))
        self.border_image = Label(self.root, image=self.border, highlightbackground='#E6E6D7')
        self.border_image.place(x=0, y=120)
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenu = Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.submenu)
        self.submenu.add_command(label='New', command=self.new)
        self.submenu.add_command(label='Open', command=self.open_file)
        self.submenu.add_command(label='Save As', command=self.save_as)
        self.submenu.add_command(label='Save', command=self.save)
        self.add_submenu = Menu(self.menu)
        self.menu.add_cascade(label='Add', menu=self.add_submenu)
        self.add_submenu.add_command(label='Add final Manually', command=self.manual_add_final)
        self.add_submenu.add_command(label='Add info to a final', command=self.add_final_information)
        self.remove_submenu = Menu(self.menu)
        self.menu.add_cascade(label="Remove", menu=self.remove_submenu)
        self.remove_submenu.add_command(label='Remove a Final', command=self.remove_final_menu)

        self.enter_crn_label = Label(self.root, text='Enter with crn:', background='#102840', foreground
                                     ='#ffffff')
        self.enter_crn_label.place(x=15, y=10)
        self.crn_box = Entry(self.root, width=10, bg='#E6E6D7', highlightbackground='#102840')
        self.crn_box.bind('<Return>', self.crn_add)
        self.crn_box.place(x=100, y=12)
        self.crn_entry = Button(self.root, text='Enter', bg='#E6E6D7', highlightbackground='#E6E6D7', command=self.crn_add)
        self.crn_entry.place(x=170, y=10)

        self.class_add_button = Button(self.root, text='Add Final by Class Information', command=self.information_add,
                                       bg='#E6E6D7', highlightbackground='#E6E6D7', width=26)
        self.class_add_button.place(x=15, y=45)
        self.home_view_tab = Button(self.root, text='Home View', bg='#bbc0b9', highlightbackground='#bbc0b9',
                                    command=self.draw_main_canvas, width=33, state=DISABLED)
        self.advanced_view_tab = Button(self.root, text='Advanced View', bg='#E6E6D7',
                                        highlightbackground='#E6E6D7', command=self.draw_advanced_canvas, width=33,
                                        state=NORMAL)
        self.home_view_tab.place(x=0, y=94)
        self.advanced_view_tab.place(x=238, y=94)

        self.generate_study_times_button = Button(self.root, text='Generate Suggested\nStudy Times', bg='#E6E6D7',
                                                  highlightbackground='#E6E6D7', command=self.generate_study_times,
                                                  height=2)
        self.generate_study_times_button.place(x=714, y=5)
        self.study_times_disclaimer = Label(self.root, text='Only Viewable in Advanced View\n(only generate after '
                                                            'entering all classes\nand all their subsequent '
                                                            'information\nfor the most helpful suggestions)',
                                            fg='#ffffff', background='#102840')
        self.study_times_disclaimer.place(x=662, y=45)

        self.schedule = Canvas(self.root, bg='#E6E6D7', width=self.x, height=(self.y - (self.y // 5.75)),
                               highlightbackground='#E6E6D7')
        self.schedule.place(x=-2, y=(self.y // 5.75))
        self.draw_main_canvas()

        self.root.mainloop()



    def show_schedule(self):
        popup.OldSchedule()

    def new(self):
        pass

    def information_add(self):
        pass

    def open_file(self):
        pass

    def save_as(self):
        pass

    def save(self):
        pass

    def manual_add_final(self):
        pass

    def add_final_information(self, final_index):
        pass

    def remove_final_menu(self):
        pass

    def crn_add(self, useless='ooga booga'):

        crn = self.crn_box.get()
        self.crn_box.delete(0, END)
        if check_crn_valid(crn):
            new_final = Final(crn)
            conflict = False
            for finals in self.list_of_finals:
                if finals == new_final:
                    conflict = True
                    popup.ErrorMessage("You have a finals scheduling conflict with the classes {} and {}. Contact a "
                                       "teacher from one of these classes to get your final time changed".format(
                                        finals.get_name().upper(), new_final.get_name().upper()))
            if not conflict:
                self.list_of_finals.append(new_final)
                new_final.set_color(self.colors[self.color_counter])
                self.color_counter += 1
                if self.color_counter > 12:
                    self.color_counter = 0
                new_final.set_home_view_coordinates(self.draw_final_Home_view(new_final.get_final_position(),
                                                                              new_final.get_color(),
                                                                              len(self.list_of_finals) - 1))

        else:
            popup.ErrorMessage(crn + " is an Invalid Crn")

    def draw_final_Home_view(self, pos, color, final_index):
        if pos[0] == 'M':
            x1 = 121
            x2 = 299

        elif pos[0] == 'T':
            x1 = 301
            x2 = 479

        elif pos[0] == 'R':
            x1 = 481
            x2 = 659

        elif pos[0] == 'F':
            x1 = 661
            x2 = 839

        else:
            x1 = 841
            x2 = 1000

        if pos[1] == '1':
            y1 = 16
            y2 = 124

        elif pos[1] == '2':
            y1 = 126
            y2 = 249

        elif pos[1] == '3':
            y1 = 251
            y2 = 374

        elif pos[1] == '4':
            y1 = 376
            y2 = 499

        else:
            y1 = 501
            y2 = 619

        name = self.list_of_finals[final_index].get_name()
        self.draw_final_home_view_label([x1+1, y1+1, x2, y2], color, 25, name,
                                        final_index)
        self.schedule.create_rectangle(x1, y1, x2, y2, fill=color)

        return [x1, y1, x2, y2]

    def draw_final_home_view_label(self, coordinates_list, color, chars_per_line, text, index):
        counter = 0
        iterations = 0
        while counter < len(text):
            if counter+chars_per_line < len(text):
                space_search = chars_per_line - 1
                while text[counter+space_search] != " " and space_search > 0:
                    space_search -= 1
                if space_search != 0:
                    space_search += 1
                    self.class_label = Label(self.schedule, text=text[counter:counter+space_search], background=color)
                    counter += space_search
                else:
                    space_search = chars_per_line - 1
                    self.class_label = Label(self.schedule, text=text[counter:counter+space_search] + '-',
                                             background=color)
                    counter += space_search
            else:
                self.class_label = Label(self.schedule, text=text[counter:], background=color)
                counter += chars_per_line
            self.class_label.place(x=coordinates_list[0], y=coordinates_list[1]+(iterations*20))
            iterations += 1
        self.add_info_button = Button(self.schedule, text='Add Information', command=
                                      self.add_final_information(index))
        self.add_info_button.place(x=coordinates_list[0]+5, y=coordinates_list[1]+(iterations*20))

    def redraw_main_view_finals(self):
        for finals in self.list_of_finals:
            pos_array = finals.get_home_view_coordinates()
            self.schedule.create_rectangle(pos_array[0], pos_array[1], pos_array[2], pos_array[3], fill=finals.get_color())

    def generate_study_times(self):
        pass

    def test(self):
        if self.counter > len(self.colors) - 1:
            self.counter = 0
        self.schedule.create_rectangle(50, 50, 150, 150, fill=self.colors[self.counter])
        self.counter += 1

    def draw_main_canvas(self):

        self.schedule.delete('all')
        self.schedule.pack_forget()
        self.redraw_main_view_finals()
        self.advanced_view_tab.configure(bg='#E6E6D7', highlightbackground='#E6E6D7', state=NORMAL)
        self.home_view_tab.configure(bg='#bbc0b9', highlightbackground='#bbc0b9', state=DISABLED)
        self.schedule.label = Label(self.schedule, text='Time', background='#E6E6D7')
        self.schedule.label.place(x=43, y=-6)
        self.schedule.label = Label(self.schedule, text='Monday', background='#E6E6D7')
        self.schedule.label.place(x=184, y=-6)
        self.schedule.label = Label(self.schedule, text='Tuesday', background='#E6E6D7')
        self.schedule.label.place(x=366, y=-6)
        self.schedule.label = Label(self.schedule, text='Thursday', background='#E6E6D7')
        self.schedule.label.place(x=540, y=-6)
        self.schedule.label = Label(self.schedule, text='Friday', background='#E6E6D7')
        self.schedule.label.place(x=729, y=-6)
        self.schedule.label = Label(self.schedule, text='Saturday', background='#E6E6D7')
        self.schedule.label.place(x=898, y=-6)
        self.schedule.create_line(120, -5, 120, 625)
        self.schedule.create_line(300, -5, 300, 625)
        self.schedule.create_line(480, -5, 480, 625)
        self.schedule.create_line(660, -5, 660, 625)
        self.schedule.create_line(840, -5, 840, 625)
        self.schedule.create_line(1001, -5, 1001, 625)
        self.schedule.create_line(0, 125, 1000, 125)
        self.schedule.create_line(0, 250, 1000, 250)
        self.schedule.create_line(0, 375, 1000, 375)
        self.schedule.create_line(0, 500, 1000, 500)
        self.schedule.create_line(0, 15, 1000, 15)
        self.schedule.time_label = Label(self.schedule, background='#E6E6D7', text="8:00am - 10:30am\n"
                                                                                   "P.1")
        self.schedule.time_label.place(x=8, y=50)
        self.schedule.time_label = Label(self.schedule, background='#E6E6D7', text="11:00am - 1:30pm\n"
                                                                                   "P.2")
        self.schedule.time_label.place(x=8, y=170)
        self.schedule.time_label = Label(self.schedule, background='#E6E6D7', text="2:00pm - 4:30pm\n"
                                                                                   "P.3")
        self.schedule.time_label.place(x=8, y=295)
        self.schedule.time_label = Label(self.schedule, background='#E6E6D7', text="5:00pm - 7:30pm\n"
                                                                                   "P.4")
        self.schedule.time_label.place(x=8, y=420)
        self.schedule.time_label = Label(self.schedule, background='#E6E6D7', text="8:00pm - 10:30pm\n"
                                                                                   "P.5")
        self.schedule.time_label.place(x=8, y=540)

    def draw_advanced_canvas(self):
        self.schedule.pack_forget()
        self.advanced_view_tab.configure(bg='#bbc0b9', highlightbackground='#bbc0b9', state=DISABLED)
        self.home_view_tab.configure(bg='#E6E6D7', highlightbackground='#E6E6D7', state=NORMAL)
        self.schedule.delete("all")
        self.schedule.cover_label = Label(self.schedule, background='#E6E6D7', width=1000)
        self.schedule.cover_label.place(x=0, y=-6)
        scroll_y = Scrollbar(self.root, orient="vertical", command=self.schedule.yview)
        scroll_y.pack(side=RIGHT, fill=None)
        self.schedule.create_line(0, 15, 1000, 15)
        self.schedule.configure(height=2000, yscrollcommand=scroll_y.set, scrollregion=self.schedule.bbox("all"))

    def on_mousewheel(self, event):
        self.schedule.yview_scroll(-1 * (event.delta // 120), "units")

    def calc_study_blocks(self):
        list_of_confidance, list_of_desired_grades, list_of_grades_needed, list_of_credit_hours = [], [], [], []
        # collects data in the 4 lists instantiated before this
        for finals in self.list_of_finals:
            list_of_confidance.append(finals.get_confidance())
            list_of_desired_grades.append(finals.get_desired_grade())
            list_of_grades_needed.append(finals.get_grade_needed())
            list_of_credit_hours.append(finals.get_credit_hours())
        mean_confidence = np.mean(list_of_confidance)
        if mean_confidence > 6.5:
            shift = True
        else:
            shift = False
        mean_grade_desired = np.mean(list_of_desired_grades)
        # 5 is the expected mean confidence and 60 is the starting number of study blocks
        blocks_multiplier = (((5 / mean_confidence) * 60) / len(self.list_of_finals))
        #  Calculates the number of blocks to add based on the shift, confidence and grade desired/grade needed
        # with set_num_blocks(int((-5 * (3/list_of_credit_hours[grade])) + blocks_multiplier) done for each iteration
        # with -5 being the changing variable depending on confidence and grade needed ranging from -5 to 17
        # this is iterated through for every final in the list
        if shift:
            for grade in range(len(list_of_grades_needed)):
                if list_of_grades_needed[grade] - 1 <= mean_grade_desired:

                    if list_of_confidance[grade] > 8:
                        self.list_of_finals[grade].set_num_blocks(
                            int((-5 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                    elif list_of_confidance[grade] < 6:
                        self.list_of_finals[grade].set_num_blocks(
                            int((10 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                    else:
                        self.list_of_finals[grade].set_num_blocks(
                            int((2 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                else:

                    if list_of_confidance[grade] > 8:
                        self.list_of_finals[grade].set_num_blocks(
                            int((-2 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                    elif list_of_confidance[grade] < 6:
                        self.list_of_finals[grade].set_num_blocks(
                            int((17 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                    else:
                        self.list_of_finals[grade].set_num_blocks(
                            int((5 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

        else:
            for grade in range(len(list_of_grades_needed)):
                if list_of_grades_needed[grade] <= mean_grade_desired:

                    if list_of_confidance[grade] > 6:
                        self.list_of_finals[grade].set_num_blocks(
                            int((-5 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                    elif list_of_confidance[grade] < 4:
                        self.list_of_finals[grade].set_num_blocks(
                            int((10 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                    else:
                        self.list_of_finals[grade].set_num_blocks(
                            int((2 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                else:

                    if list_of_confidance[grade] > 8:
                        self.list_of_finals[grade].set_num_blocks(
                            int((-2 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                    elif list_of_confidance[grade] < 6:
                        self.list_of_finals[grade].set_num_blocks(
                            int((17 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))

                    else:
                        self.list_of_finals[grade].set_num_blocks(
                            int((5 * (3 / list_of_credit_hours[grade])) + blocks_multiplier))


if __name__ == "__main__":
    UserInterface()
