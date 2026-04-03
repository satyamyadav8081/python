student_data=[
    {
        "name":"ram",
        "roll_no":10,
        "age":20,
        "course":"python"
    }, 
    {
        "name":"mohan",
        "roll_no":20,
        "age":22,
        "course":"java",
    }
]
def add_new_student(name,rollno,age,course_opted):
    new_student={}
    new_student["name"]=name
    new_student["roll_no"]=rollno
    new_student["age"]=age
    new_student["course"]=course_opted
    student_data.append(new_student) 

add_new_student("shyam",22,18,"c++")
print(student_data)