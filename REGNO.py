class StudentRegistrationNumber:

    def __init__(self, name, course, registrationnumber):
        self.name = name
        self.course = course
        self.registrationnumber = registrationnumber
          
    def __str__(self):
        return(f"Name: {self.name} Course: {self.course} Registration Number: {self.registrationnumber}")

Regno1 = StudentRegistrationNumber("Nyirinka Gabriel", "Bachelor of Governance in International Relations", "M23B15/022")
print(Regno1)

Regno2 = StudentRegistrationNumber("Malcolm Nkusi", "Bachelor of Science in Information Technology", "S23B55/014")
print(Regno2)

Regno3 = StudentRegistrationNumber("Akaliza Nia", "Bachelor in Accounting and Financial Management", "M23B13/001")
print(Regno3)

Regno4 = StudentRegistrationNumber("Mwiza Daniella", "Bachelor of Science in Information Technology", "M23B13/055")
print(Regno4)

Regno5 = StudentRegistrationNumber("Keza Daphine", "Bachelor in Human Resource Management", "S23B13/011")
print(Regno5)

