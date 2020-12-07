import New_student.py_sql_file
from tkinter import *


# def add_new_std():
#     new_student_window = Tk()
#     new_student_window.title("Add New Student Data")
#     new_student_window.configure(bg="#425942")
#     new_student_window.geometry("1000x350")
#
#     # new_student_window main Label
#
#     new_student_window_label = Label(new_student_window, text="Add New Student Data", font=("Algerian", 20, "bold"),
#                                      fg="White", bg="#425942")
#     new_student_window_label.grid(row=0, column=2, pady=10, padx=10)
#
#     new_student_window_roll_no_label = Label(new_student_window, text="Roll Number: ", fg="White", bg="#425942",
#                                              font=("Bold", 14))
#     new_student_window_roll_no_label.grid(row=1, column=1, pady=10, padx=10, sticky='w')
#
#     new_student_window_roll_no_entry = Entry(new_student_window, bd=10, relief=SUNKEN, font=('arial', 10, 'bold'))
#     new_student_window_roll_no_entry.grid(row=1, column=2, pady=10, padx=10)
#
#     # new_student_window fall Label
#
#     new_student_window_fall_label = Label(new_student_window, text="Fall: ", fg="White", bg="#425942",
#                                              font=("Bold", 14))
#     new_student_window_fall_label.grid(row=1, column=3, pady=10, padx=10, sticky='w')
#
#     # new_student_window fall Text Entry Box
#
#     new_student_window_fall_entry = Entry(new_student_window, bd=10, relief=SUNKEN, font=('arial', 10, 'bold'))
#     new_student_window_fall_entry.grid(row=1, column=4, pady=10, padx=10)
#
#     # new_student_window Student First Name Label
#
#     new_student_window_first_name_label = Label(new_student_window, text="Student First Name:", fg="White",
#                                                 bg="#425942", font=("Bold", 14))
#     new_student_window_first_name_label.grid(row=2, column=1, pady=10, padx=10, sticky='w')
#
#     # new_student_window Student First Name Text Entry Box
#
#     new_student_window_first_name_entry = Entry(new_student_window, bd=10, relief=SUNKEN, font=('arial', 10, 'bold'))
#     new_student_window_first_name_entry.grid(row=2, column=2, pady=10, padx=10)
#
#     # new_student_window Student Last Name Label
#
#     new_student_window_last_name_label = Label(new_student_window, text="Student Last Name:", fg="White", bg="#425942",
#                                                font=("Bold", 14))
#     new_student_window_last_name_label.grid(row=2, column=3, pady=10, padx=10, sticky='w')
#
#     # new_student_window Student Last Name Text Entry Box
#
#     new_student_window_last_name_entry = Entry(new_student_window, bd=10, relief=SUNKEN, font=('arial', 10, 'bold'))
#     new_student_window_last_name_entry.grid(row=2, column=4, pady=10, padx=10)
#
#     # new_student_window Father Name Label
#
#     new_student_window_father_name_label = Label(new_student_window, text="Student Father Name:", fg="White",
#                                                  bg="#425942", font=("Bold", 14))
#     new_student_window_father_name_label.grid(row=3, column=1, pady=10, padx=10, sticky='w')
#
#     # new_student_window Father Name Text Entry Box
#
#     new_student_window_father_name_entry = Entry(new_student_window, bd=10, relief=SUNKEN, font=('arial', 10, 'bold'))
#     new_student_window_father_name_entry.grid(row=3, column=2, pady=10, padx=10)
#
#     # new_student_window Student CNIC Number Label
#
#     new_student_window_cnic_label = Label(new_student_window, text="CNIC Number: ", fg="White", bg="#425942",
#                                           font=("Bold", 14))
#     new_student_window_cnic_label.grid(row=3, column=3, pady=10, padx=10, sticky='w')
#
#     # new_student_window CNIC Number Text Entry Box
#
#     new_student_window_cnic_entry = Entry(new_student_window, bd=10, relief=SUNKEN, font=('arial', 10, 'bold'))
#     new_student_window_cnic_entry.grid(row=3, column=4, pady=10, padx=10)
#
#     # new_student_window Student Age Label
#
#     new_student_window_age_label = Label(new_student_window, text="Student Age: ", fg="White", bg="#425942",
#                                          font=("Bold", 14))
#     new_student_window_age_label.grid(row=4, column=1, pady=10, padx=10, sticky='w')
#
#     # new_student_window Student Age Text Entry Box
#
#     new_student_window_age_entry = Entry(new_student_window, bd=10, relief=SUNKEN, font=('arial', 10, 'bold'))
#     new_student_window_age_entry.grid(row=4, column=2, pady=10, padx=10)
#
#     # new_student_window Student address Number Label
#
#     new_student_window_address_label = Label(new_student_window, text="Student Address: ", fg="White", bg="#425942",
#                                              font=("Bold", 14))
#     new_student_window_address_label.grid(row=4, column=3, pady=10, padx=10, sticky='w')
#
#     # new_student_window Student Address Text Entry Box
#
#     new_student_window_address_entry = Entry(new_student_window, bd=10, relief=SUNKEN, font=('arial', 10, 'bold'))
#     new_student_window_address_entry.grid(row=4, column=4, pady=10, padx=10)
#
#     # new_student_window Student Father Number Label
#
#     new_student_window_student_father_number_label = Label(new_student_window, text="Student Father Number: ",
#                                                            fg="White", bg="#425942", font=("Bold", 14))
#     new_student_window_student_father_number_label.grid(row=4, column=3, pady=10, padx=10, sticky='w')
#
#     # new_student_window Student Father Number Text Entry Box
#
#     new_student_window_student_father_number_entry = Entry(new_student_window, bd=10, relief=SUNKEN,
#                                                            font=('arial', 10, 'bold'))
#     new_student_window_student_father_number_entry.grid(row=4, column=4, pady=10, padx=10)
#
#     # making Save button
#
#     button_save_data = Button(new_student_window, text="Save Data", font=("Bold", 15), height=1, width=10,
#
#                               # Get data
#
#                               command=lambda: [New_student.py_sql_file.add_data_into_table(new_student_window_fall_entry.get(),
#                                                new_student_window_roll_no_entry.get(),
#                                                new_student_window_first_name_entry.get(),
#                                                new_student_window_last_name_entry.get(),
#                                                new_student_window_father_name_entry.get(),
#                                                new_student_window_cnic_entry.get(),
#                                                new_student_window_age_entry.get(),
#                                                new_student_window_student_father_number_entry.get()),
#
#                                                # delete entry box data
#
#                                                new_student_window_fall_entry.delete('0', 'end'),
#                                                new_student_window_roll_no_entry.delete('0', 'end'),
#                                                new_student_window_first_name_entry.delete('0', 'end'),
#                                                new_student_window_last_name_entry.delete('0', 'end'),
#                                                new_student_window_father_name_entry.delete('0', 'end'),
#                                                new_student_window_cnic_entry.delete('0', 'end'),
#                                                new_student_window_age_entry.delete('0', 'end'),
#                                                new_student_window_student_father_number_entry.delete('0', 'end')
#                                                ])
#     button_save_data.grid(row=5, column=2, pady=10, padx=10)
#
#     #  making Quit Button and Function
#
#     def destroy():
#         new_student_window.destroy()
#
#     #  Making Quit Button
#
#     quit_button = Button(new_student_window, text="Quit", font=("Bold", 15), height=1, width=10,
#                          command=lambda: destroy())
#     quit_button.grid(row=5, column=3, pady=10, padx=10)
#
#     new_student_window.mainloop()


# add_new_std()