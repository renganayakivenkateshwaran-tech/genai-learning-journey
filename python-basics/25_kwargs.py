#**kwargs is a special syntax used in function definitions to accept any number of keyword arguments (arguments passed as key=value pairs).

def stu_list(**kwargs):
    for key,value in kwargs.items():
        print(f"{key:7}: {value}")
stu_list(Name="Achu",
         Mark=90,
         Grade="A+",
         Rollno="027")

