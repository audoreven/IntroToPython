from tkinter import *  # Import tkinter


class WidgetsDemo:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Display File")  # Set a title

        # Add a button, a check button, and a radio button to frame1
        frame1 = Frame(window)  # Create and add a frame to window
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text="Bold",
                              variable=self.v1, command=self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text="Red", bg="red",
                            variable=self.v2, value=1,
                            command=self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text="Yellow",
                               bg="yellow", variable=self.v2, value=2,
                               command=self.processRadiobutton)
        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

        # Add a button, a check button, and a radio button to frame1
        frame2 = Frame(window)  # Create and add a frame to window
        frame2.pack()
        label = Label(frame2, text="Enter the file name to load: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable=self.name)
        btGetName = Button(frame2, text="Get File",
                           command=self.processButton)
        # message = Message(frame2, text="It is a widgets demo")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        # message.grid(row=1, column=4)

        # Add a text
        self.text = Text(window)  # Create a text add to the window
        self.text.pack()

        """
        self.text.insert(END,
                         "Tip\nThe best way to learn Tkinter is to read ")
        self.text.insert(END,
                         "these carefully designed examples and use them ")
        self.text.insert(END, "to create your applications.")
        """

        window.mainloop()  # Create an event loop

    def processCheckbutton(self):
        print("check button is "
              + ("checked " if self.v1.get() == 1 else "unchecked"))

    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow")
              + " is selected ")

    def processButton(self):
        self.text.delete('1.0', END)
        # print("File name: " + self.name.get())
        try:
            file = open(self.name.get(), "r")
            lines = file.read()
            for l in lines:
                self.text.insert(END, l)
        except FileNotFoundError:
            self.text.insert(END, "File does not exist. Please try again. \n")


WidgetsDemo()  # Create GUI