class human:
    def eat (self):
        print("i can eat")
class male(human):
    def sleep(self):
        print("i can sleep whole day.")
class female(human):
    def work (self):
        print(" ican code") 
female_1=female()
female_1.eat()   
male_1=male()
male_1.sleep()     
