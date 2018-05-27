"""
This program will provide a GUI to calculate
convert Fahrenheit to celcius and vice versa
"""

import tkinter
import tkinter.messagebox

class Temperature:

    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create the three frames
        self.temp_frame = tkinter.Frame(self.main_window)
        self.result_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets to the temp frame
        self.temp_label = tkinter.Label(self.temp_frame,
                                        text='Enter the temperature to convert:')
        self.temp_entry = tkinter.Entry(self.temp_frame, width=10)
        self.temp_label.pack(side='left')
        self.temp_entry.pack(side='left')

        # # Create and pack the widgets for results output
        # self.result1_label = tkinter.Label(self.result_frame,text='Fahrenheit')
        # self.fahren = tkinter.StringVar() # To update fahren_label
        # self.fahren_label = tkinter.Label(self.result_frame,textvariable=self.fahren)
        #
        # self.result2_label = tkinter.Label(self.result_frame, text='Celcius')
        # self.celciu = tkinter.StringVar() # To update the celciu_label
        # self.celciu_label = tkinter.Label(self.result_frame, textvariable=self.celciu)
        #
        # self.result1_label.pack(side='left')
        # self.fahren_label.pack(side='left')
        # self.result2_label.pack(side='left')
        # self.celciu_label.pack(side='left')

        # Create and pack the button widgets
        self.fahren_button = tkinter.Button(self.button_frame,
                                            text='Fahrenheit',
                                            command=self.calc_fahren)
        self.celciu_button = tkinter.Button(self.button_frame,
                                            text='Celcius',
                                            command=self.calc_celciu)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.fahren_button.pack(side='left')
        self.celciu_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.temp_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()

        # Start the main loop
        tkinter.mainloop()

    # The calc_fahren method is the callback function for
    # for the fahren_button widget

    def calc_fahren(self):
        # Get the variables to be used for calculating
        self.temp_cel = float(self.temp_entry.get())

        # Calculate the fahrenheit temperature
        self.fahrenheit = 9/5 * self.temp_cel  + 32

        # Display the reults in an info dialog box
        tkinter.messagebox.showinfo('Results', str(self.temp_cel) +
                                    ' degrees celcius is equal to ' +
                                    str(self.fahrenheit) + ' degrees fahrenheit')

        # # Update the main label
        # self.fahren.set(self.fahrenheit)
        # self.celciu.set(self.temp_cel)

    def calc_celciu(self):
        # Get the variables to be used for calculating
        self.temp_fah = float(self.temp_entry.get())

        # Calculate the celcius temperature
        self.celcius = (self.temp_fah - 32) * 5/9

        # Display the reults in an info dialog box
        tkinter.messagebox.showinfo('Results', str(self.temp_fah) +
                                    ' degrees fahrenheit is equal to ' +
                                    str(self.celcius) + ' degrees celcius')

        # # Update the main label
        # self.celciu.set(self.celcius)
        # self.fahren.set(self.temp_fah)
        #
# Create an instance of the Temperature class.
temp_conversion = Temperature()
        
