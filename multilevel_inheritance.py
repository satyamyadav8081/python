class human:
    def eat (self):
        print("I can eat")
    def work(self):
        print(" i can work")
class male(human):
    def sleep(self):
        print("i can sleep whole day")
class boy(male):
    def work (self):
        human.work(self)
        print("i can code")
boy_1=boy()
boy_1.work()        
