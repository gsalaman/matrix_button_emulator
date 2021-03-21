from Tkinter import *

class ButtonEmulator():
  def __init__(self):
    self.window = Tk()
    self.window.title("Matrix Button Emulator")
    self.create_widgets()

  def create_widgets(self):
    self.buttons = [[None for _ in range(8)] for _ in range(8)]

    for i in range(8):
      for j in range(8):
        self.buttons[i][j] = Button(self.window, 
                                text=str(i)+","+str(j), 
                                command=lambda i=i, j=j:self.button_press(self.buttons[i][j]))

        self.buttons[i][j].grid(row=i, column=j)

  def button_press(self, button):
    print("press: "+button["text"])


######################################################
# Main
######################################################
my_window = ButtonEmulator()
my_window.window.mainloop()

