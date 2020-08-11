class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    @classmethod
    def get_data(cls, data):
        students = []
        for entry in data:
            student = cls(entry["name"], entry["age"], entry["roll_no"])
            students.append(student)


        return students


data = [
    {
        "name": "Anna",
        "age": 42,
        "roll_no": 115
    },
    {
        "name": "Banana",
        "age": 48,
        "roll_no":456
    }
]

students = Student.get_data(data)

print(students[1].age)