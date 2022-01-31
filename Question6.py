import datetime #For current year.

#------------------------CLASSES--------------------------

#Our parent class.
class user_data:

#Usernames and passwords contains in it.  
    username_password = dict({})

    def __init__(self, first_name):       
        self.first_name = first_name
        

class student_user(user_data):
    
    def __init__(self, enrolls_year, first_name):
        self.enrolls_year = enrolls_year   #Specific quality of student.
        user_data.__init__(self, first_name)
        
    def show_username(self):
        print(f"This is the username for {self.first_name} : {str(self.first_name).lower()}@pru") 

    def create_password(self):        
        print(f"This is the password for {self.first_name} : {self.enrolls_year}{str(self.first_name[0].upper())}{str(self.first_name[1].lower())}StPR") 
        self.username_password[(str(f"{str(self.first_name).lower()}@pru"))] = (str(f"{self.enrolls_year}{str(self.first_name[0].upper())}{str(self.first_name[1].lower())}StPR")) 
        #This code puts datas to dict for storage.   

        
class academician_user(user_data):
    
    def show_username(self):    
        print(f"This is the username for {self.first_name} : {str(self.first_name).lower()}@pirireis")
        
    def create_password(self):
        self.current_date = datetime.datetime.now()
        self.current_year = self.current_date.year
        print(f"This is the password for {self.first_name} : {self.current_year}{str(self.first_name[0].upper())}{str(self.first_name[1].lower())}AsPR")
        self.username_password[(str(f"{str(self.first_name).lower()}@pirireis"))] = (str(f"{self.current_year}{str(self.first_name[0].upper())}{str(self.first_name[1].lower())}AsPR"))

#-------------------USER ADDING FUNCTIONS---------------------

def student_user_add():
    enrollyear = input("Student's enroll year: ") 
    #a new function has opened and it's creating username and passwords for students.
    string_name = input("Student's name: ")
    User_no = student_user(enrollyear, string_name)
    User_no.show_username()
    User_no.create_password()

def academician_user_add():
    string_name = input("Academician's Name: ")
    #a new function has opened and it's creating username and passwords for academicians.
    User_no = academician_user(string_name)
    User_no.show_username()
    User_no.create_password()

#----------------------USER DATA ADDING---------------------------

again = ""      #This is the part for continue to create user datas and choosement for the entries like student or academicians.
while (again != "e"):

    p = input("Please indicate that the person whose information will be entered is a student or academician: (s for Student/a for Academician)")  
    
    if p == "a":
        academician_user_add()
        again = input("Another user data? (e for exit, anything else for another data.):  ")
    elif p == "s":
        student_user_add()
        again = input("Another user data? (e for exit, anything else for another data.):  ")
    else:
        print("Invalid value!!!\n(s for Student/a for Academician)")

#--------------------LOGIN WINDOW------------------------

def login():
    print("\nLOGIN")        #this is the part that you can check username and password for enter the system.
    Username = input("Username: ")

    if Username in user_data.username_password:
        Password = input("Password: ")
        if user_data.username_password[Username] == Password:
            if "@pru" in Username:
                print("Hello student!")
            else:
                print("Welcome to the system Professor!")
        else:
            print("The system couldn't recognize this user! (illegal user!!!)")

    else:
        print("The system couldn't recognize this user! (illegal user!!!)")


login()
