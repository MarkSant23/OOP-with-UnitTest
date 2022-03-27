from datetime import date

today = date.today()


class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I am going {} kph".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == '__main__':
    my_car = Car()
    print("I am a car!")
    while 1:
        action = input("What should I do? [A]ccelerate, [B]rake, " "show [O]dometer, show average [S]peed or e[X]it?").upper()
        if action not in "ABOSX" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == "A":
            my_car.accelerate()
        elif action == "B":
            my_car.brake()
        elif action == "O":
            print("The car has driven {} kph".format(my_car.odometer))
        elif action == "S":
            print("Average speed was {}".format(my_car.average_speed()))
        elif action == "X":
            exit()
        my_car.step()
        my_car.say_state()
