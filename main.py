import time
import threading
from tkinter import *

# To center the window on the screen (This is a little Mixin)
class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.geometry(f"{w}x{h}+{x}+{y}")  

# Generating the main screen
class MainWidow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Program 4 - Dining philosophers problem")
        self.resizable(0, 0) 
        self.geometry("1000x600")
        self.config(relief="sunken", bd=10, background="white")
        self.center()
        self.Build()
        self.Execute()

    # Creating interfaces
    def Build(self):
        # To contain other widgets
        mainFrame = Frame(self)
        mainFrame.grid(row=0, column=0)

        # To contain the philosophers
        philosophersFrame = Frame(self)
        philosophersFrame.grid(row=0, column=0)
        self.philosophersImage = PhotoImage(file="./Assets/philosophers.png")
        labelOfPhilosophersImage = Label(philosophersFrame, image=self.philosophersImage)
        labelOfPhilosophersImage.grid(row=0, column=0)

        # To contain information
        informationFrame = Frame(self)
        informationFrame.grid(row=0, column=1, sticky=S+N+E+W)
        informationFrame.config(padx=80, pady=190)

        firstPhilosopherFrame = Frame(informationFrame)
        firstPhilosopherFrame.grid(row=0, column=0)
        firstPhilosopherFrame.config(padx=10, pady=10)
        firstPhilosopherName = Label(firstPhilosopherFrame, text="Philosopher 1: Rene Descartes: ")
        firstPhilosopherName.grid(row=0, column=0)
        self.firstPhilosopherStatus = Label(firstPhilosopherFrame, text="Thinking")
        self.firstPhilosopherStatus.grid(row=0, column=1)
        self.firstPhilosopherStatus.config(background="orange")

        secondPhilosopherFrame = Frame(informationFrame)
        secondPhilosopherFrame.grid(row=1, column=0)
        secondPhilosopherFrame.config(padx=10, pady=10)
        secondPhilosopherName = Label(secondPhilosopherFrame, text="Philosopher 2: Nietzsche: ")
        secondPhilosopherName.grid(row=0, column=0)
        self.secondPhilosopherStatus = Label(secondPhilosopherFrame, text="Thinking")
        self.secondPhilosopherStatus.grid(row=0, column=1)
        self.secondPhilosopherStatus.config(background="orange")

        thirdPhilosopherFrame = Frame(informationFrame)
        thirdPhilosopherFrame.grid(row=2, column=0)
        thirdPhilosopherFrame.config(padx=10, pady=10)
        thirdPhilosopherName = Label(thirdPhilosopherFrame, text="Philosopher 3: Spinoza: ")
        thirdPhilosopherName.grid(row=0, column=0)
        self.thirdPhilosopherStatus = Label(thirdPhilosopherFrame, text="Thinking")
        self.thirdPhilosopherStatus.grid(row=0, column=1)
        self.thirdPhilosopherStatus.config(background="orange")

        fourthPhilosopherFrame = Frame(informationFrame)
        fourthPhilosopherFrame.grid(row=3, column=0)
        fourthPhilosopherFrame.config(padx=10, pady=10)
        fourthPhilosopherName = Label(fourthPhilosopherFrame, text="Philosopher 4: Kierkegaard: ")
        fourthPhilosopherName.grid(row=0, column=0)
        self.fourthPhilosopherStatus = Label(fourthPhilosopherFrame, text="Thinking")
        self.fourthPhilosopherStatus.grid(row=0, column=1)
        self.fourthPhilosopherStatus.config(background="orange")

        fifthPhilosopherFrame = Frame(informationFrame)
        fifthPhilosopherFrame.grid(row=4, column=0)
        fifthPhilosopherFrame.config(padx=10, pady=10)
        fifthPhilosopherName = Label(fifthPhilosopherFrame, text="Philosopher 5: Karl Marx: ")
        fifthPhilosopherName.grid(row=0, column=0)
        self.fifthPhilosopherStatus = Label(fifthPhilosopherFrame, text="Thinking")
        self.fifthPhilosopherStatus.grid(row=0, column=1)
        self.fifthPhilosopherStatus.config(background="orange")

    # To execute program logic
    def Execute(self):
        # Creating a chair
        chair = Chair()

        # Its labels
        labels = [self.firstPhilosopherStatus, self.secondPhilosopherStatus, self.thirdPhilosopherStatus, self.fourthPhilosopherStatus, self.fifthPhilosopherStatus]
        
        # Creating Chopsticks
        chopsticks: list[Chopstick] = [Chopstick(x) for x in range(5)]

        # Creating Philosophers
        philosophers: list[Philosopher] = [Philosopher(x, chopsticks[x], chopsticks[(x+1)%5], chair, labels[x]) for x in range(5)]
        
        # Feeding the philosophers
        for x in range(5):
            philosophers[x].start()

# Class related to eating utensil like a fork
class Chopstick:
    chopstickId: int
    lock = threading.Condition()
    isFree = True
    

    def __init__(self, chopstickId) -> None:
        self.chopstickId = chopstickId

    def TakeChopstick(self, philosopherId) -> None:
        with self.lock:
            while not self.isFree:
                self.lock.wait()
            print(f"The philosopher {philosopherId} has taken the chopstick {self.chopstickId}")
            #time.sleep(1)
            self.isFree = False
                

    def DropChopstick(self, philosopherId) -> None:
        with self.lock:
            self.isFree = True
            print(f"The philosopher {philosopherId} has dropped the chopstick {self.chopstickId}")
            #time.sleep(1)
            self.lock.notify()
        

# Solving this through monitors
class Chair:
    freeChairs = 4
    lock = threading.Condition()

    def TakeASeat(self, philosopherId):
        # Is there a free chair?
        with self.lock:
            while self.freeChairs == 0:
                self.lock.wait()
            print(f"The philosopher {philosopherId} has taken a seat")
            #time.sleep(1)
            self.freeChairs -= 1

    def VacateASeat(self, philosopherId):
        with self.lock:
            print(f"The philosopher {philosopherId} has vacated a seat")
            self.freeChairs += 1
            #time.sleep(1)
            self.lock.notify()

# Class representing a philosopher and his thread of execution
class Philosopher(threading.Thread):
    philosopherId: int
    leftChopstick: Chopstick
    rightChopstick: Chopstick
    chair: Chair
    label: Label

    def __init__(self, philosopherId: int, leftChopstick: Chopstick, rightChopstick: Chopstick, chair: Chair, label: Label) -> None:
        super().__init__()
        self.philosopherId = philosopherId
        self.leftChopstick = leftChopstick
        self.rightChopstick = rightChopstick
        self.chair = chair
        self.label = label

    # We need the Run() method due to we're extending the threading.Thread class
    def run(self):
        # Trying to eat
        while True:
            # Taking both Chopsticks 
            try:
                # When philosopher is eating
                self.chair.TakeASeat(self.philosopherId)
                self.leftChopstick.TakeChopstick(self.philosopherId)
                self.rightChopstick.TakeChopstick(self.philosopherId)
            except Exception as e:
                print(f"The philosopher {self.philosopherId} is thinking")
            else:
                print(f"The philosopher {self.philosopherId} is eating")
                self.label["text"] = " Eating "
                self.label.config(background="pink")
                time.sleep(1)
                # When philosopher is no longer eating
                self.rightChopstick.DropChopstick(self.philosopherId)
                self.leftChopstick.DropChopstick(self.philosopherId)
                self.chair.VacateASeat(self.philosopherId)
                self.label["text"] = "Thinking"
                self.label.config(background="orange")
                time.sleep(1)
            

# Running this
if __name__ == "__main__":
    app = MainWidow()
    app.mainloop()