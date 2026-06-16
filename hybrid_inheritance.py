class A:
    def dissplay(self):
        print("display from a class")
class b(A):
    def diplay(self):
        print("display from b class")
class c :
    def show(self):
        print("hii from c class")
class d(b,c):
    def display(self):
        print("display from d class")                        
d1=d()
d1.display()        
print(d.mro())