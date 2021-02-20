class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


vardi = ("Alex", "Carl", "Hannah")
students_class_list = [Student(x) for x in vardi]
print(*students_class_list)
