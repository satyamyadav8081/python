#def add(*numbers,name): # 1,2,3,4,56,8
    #c=0
    #print(numbers)
    #print(name)
    #for i in numbers:
        #c += i
    #print(f"sum is {c}")

#add(1,2,name="satyam")
#add(6,5,6)
#add(1,2,3,4,56,8)        
def info_person(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)
info_person(1,2, name="ram",age=30,dept="CSE")
info_person(1,2,3, name="shyam",dept="CSE")        