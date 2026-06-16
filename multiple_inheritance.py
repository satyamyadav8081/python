class Human :
    def eat(self):
        print("I can eating")

class male:
    def flirt(self):
        print("i can flirt")

class Boy(Human,male):
    pass

boy_1=Boy()
boy_1.flirt()


