import_random

class Student:
    def __init__(self, name):
        self.name = name
        self. gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress +=0.12
        self.gladness -=3
    def to_sleep(self):
        print("I want sleep")
        self.gladness += 3
    def to_chill(self):
            print("Rest time")
            self.gladness += 5
            self.progress -= 0.1

    def is_alive(self):
        if self.progress <-0.5:
            print("Tebe vidrahovano!")
            self.alive = False
        elif self.gladness <=0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Extern")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")


    def live(self, day):
        day = "Day" + str(day) + "of" + self,name + "live"
        print(f"{day: =^50}")
        vipadkove = random.randint(1, 3)
    if vipadkove ==1:
        self.to_study()
    elif vipadkove== 2:
        self.to_sleep()
    elif vipadkove == 3:
        self.to_chill()
        self.end_of_day()
        self.is_alive()





