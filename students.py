#First we declare the class
####
class student:


    #number of students is a class variable used to count the number of students in the class.

    number_of_students = 0
    #then we declare the method in the class which is __init__

    def __init__(self, name, Id, grade):
        self.name = name
        self.Id = Id
        self.grade = grade
        #self.email =  Id + "@hitch.edu.my"
        student.number_of_students +=1

        #a property decorator is added here if in any case anyone would like to change the Id of the student.
        # the email is defined as a method but we can access it just like the alttribute
    @property
    def email(self):
        return '{}@hitch.edu.my'.format(self.Id)

#__str__ is a dunder method and it over print for you what ever you need
    def __str__(self):
        #if self.members is True:
            #print("Group members ----> {}".format(self.members))
        return """
        Student Name -------> {}
        Student ID   -------> {}
        Student Email-------> {}
        Student CGPA -------> {}
        Student course------> {}
        Student fees -------> {}

    """.format(self.name, self.Id, self.email, self.grade, self.major, self.fees)
    #to give this class more functinality call this method to check the lenght of the student name.
    def __len__(self):
        name_len = len(self.name)
        if name_len > 12:
            print("Your name is too long!, add name less than 12 characters.")
        else:
            return name_len


#--------------------------------------------------------------------------------------------------------------------------------------------------


#inheritance: copying all the variables of the parant class in this case it's the student class that we are inheriting from.
class engineering(student):
    def __init__(self, name, Id, grade, fees, major):
        super().__init__(name, Id, grade)
        self.fees = fees
        self.major = major
    def __add__(self,other):
        return self.fees + other.fees

    # Using the class method form_string() as an alturnative constructor to parse the string containg the data of the student.
    @classmethod
    def form_string(cls, stud_data):
        name, Id, grade, fees, major = stud_data.split('-')
        return cls(name, Id, grade, fees, major)

class leder(engineering):
    def __init__(self, name, Id, grade, fees, major, members=None):
        super().__init__(name, Id, grade, fees, major)
        if members is None:
            self.members = []
        else:
            self.members = members

    def add_memb(self, mem):
        if mem not in self.members:
            self.members.append(mem)

    def remove_memb(self, mem):
        if mem in self.members:
            self.members.remove(mem)

    #def __str__(self):
        #return"Grup members -----> {}".format(self.members)

    def print_membs(self):
        for memb in self.members:
            print("--->",memb.name)




# To read the students data from a file (students.txt) then pass the students as instances to our class engineering.

with open('students.txt', 'r') as f:
    student_data = f.readline().splitlines()
    #splitline will put all the read lines into a list of one variable of their own so we will need to access it by
    #student IDs are in the students.txt file.
    student_id = input("Enter the student ID number: ")

    while(len(student_data) > 0):
        if student_id in student_data[0]:
            student1 = engineering.form_string(student_data[0])
            #passing the student data as'name-Id-grade-fees-major' to
            #the form_string() class method to parse the student data string and the returns them as objects.
        student_data = f.readline().splitlines()

print("student 1",student1)

# Print statments were used in the initial testing of the project

student2=engineering("Lim kee", 'c1500456', 2.4, 25000, "Mechanical Engineering")
student3=engineering("Naim Hakimey", "c1500355", 2.59, 23000, "Electrical Engineering")
#student4=leder("Abdalla Ashraf", 'c1500696', 3.34, 25000, "Mechanical Engineering", [student2, student1])

#various ways of interacting with this project
print("--------------------------------------------------------------------------")
#student2.Id = "c1500333"
print("student 2 ",student2)
print("student 3",student3)
#print(student3)
#student3.print_membs()
print("There are ", student.number_of_students," students in the college")
print(student1.__len__())

# to use this print statment make use of the instenses in lines 109-111
print("The addition of the fees for student 2 and 3 is ---> ", student3+student2)
