from Tkinter import *
import paho.mqtt.client as mqtt

class ButtonEmulator():
  def __init__(self):
    self.window = Tk()
    self.window.title("Matrix Button Emulator")
    self.create_widgets()
    self.client = mqtt.Client("Button_Emulator")
    # note we don't need "on_message" because we only publish.

    self.client.connect("mqttbroker")
    #self.client.connect("matrix-pi1.local")
    #self.client.connect("broker.hivemq.com")

  def create_widgets(self):
    self.buttons = [[None for _ in range(8)] for _ in range(8)]

    for i in range(8):
      for j in range(8):
        self.buttons[i][j] = Button(self.window, 
                                text=str(i)+","+str(j), 
                                command=lambda i=i, j=j:self.button_press(self.buttons[i][j]))

        self.buttons[i][j].grid(row=j, column=i)

  def button_press(self, button):
    self.client.publish("jumbotron/button/press", "P"+button["text"])
    print("press: "+button["text"])


######################################################
# Main
######################################################
my_window = ButtonEmulator()
my_window.window.mainloop()

