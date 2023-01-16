# example_list = ["Karl", "Kev", "John"]
# example_bool = True
# example_string = "Hello world"
# def this_is_a_function(a, b):
#     return a * b

# print(type(example_list))
# print(type(example_bool))
# print(type(example_string))
# print(type(this_is_a_function))

# class Student(object):
#     def __init__(self, age, name, gender, grades):
#         self.age = age
#         self.name = name
#         self.gender = gender
#         self.grades = grades
    
#     def compute_average(self):
#         average = sum(self.grades)/len(self.grades)
#         print("The average for student " + self.name + " is " + str(average))

# karl = Student(39, "Karl Dudley", "Male", [89,90])
# john = Student(68, "John Dudley", "Male", [96,92])

# print(karl.age)
# print(john.name)
# karl.compute_average()

class Wolf:
    # class variables
    classification = "canine"
    habitat = "forest"
    is_sleeping = False

    # Constructor methos with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_sleep_state(self):
        if self.is_sleeping == False:
            return self.name + " is awake"
        else:
            return self.name + " is sleeping"

def main():
    # First object, set up instance variable of constructor method
    silver_tooth = Wolf("Silvertooth", 5)

    # Print out instance variable name
    print(silver_tooth.name)

    # Print out class variable habitat
    print(silver_tooth.habitat)

    # Second object
    lone_wolf = Wolf("Lone Wolf", 8)
    print(lone_wolf.show_sleep_state())

    # change sleep state
    lone_wolf.is_sleeping = True
    print(lone_wolf.show_sleep_state())

main()
