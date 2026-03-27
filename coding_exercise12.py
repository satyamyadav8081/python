text="welcome to jenny's lectures"
splited_text=text.split("e")
print(splited_text)


import random

names=input("enter everbody's nae seperated by comma:")
names_list=names.split(",")
#print(names_list)
length=len(names_list)
random_choice=random.randint(0,length-1)
print(f"{names_list[random_choice]} will pay the bill")