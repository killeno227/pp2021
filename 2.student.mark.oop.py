import math
import numpy
import curses

#
Student = []
StudentID = []
Course = []
CourseID = []
Mark = []


class Students:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        Student.append(self)
        StudentID.append(self.__id)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob


class Courses:
    def __init__(self, cid, cname):
        self._cid = cid
        self._cname = cname

        Course.append(self)
        CourseID.append(self._cid)

    def get_id(self):
        return self._cid

    def get_name(self):
        return self.cname


class Marks:
    def __init__(self, mid, nid, mark):
        self._mid = mid
        self._nid = nid
        self._mark = mark
        Mark.append(self)

    def get_mid(self):
        return self.mid

    def get_nid(self):
        return self.nid

    def get_mark(self):
        return self.mark

    def get_gpa(self):
        return self.gpa


# Input number of students

def student_num():
    print("---- TOTAL NUMBER OF STUDENTS----")
    student = int(input("Enter total number of student: "))
    return student


# Add student

def add_student():
    print("-----ADD A STUDENT-----")
    id = input("Enter Student's ID: ")
    name = input("Enter Student's NAME: ")
    dob = input("Enter Student's DOB: ")
    st_u = {
        'id': id,
        'name': name,
        'dob': dob
    }
    Student.append(st_u)
    StudentID.append(id)


# Add number of course
def course_num():
    print("---- ADD NUMBER OF COURSE----")
    course = int(input("Enter total number of course: "))
    return course


# Add course
def add_course():
    print("---- ADD A COURSE ----")
    cid = input("Enter Course's ID: ")
    cname = input("Enter Course's NAME: ")
    cc = input("Enter Course's Credit:")
    cr_o = {
        'cid': cid,
        'cname': cname,
        'cc': cc
    }
    Course.append(cr_o)
    CourseID.append(cid)


# Create mark for students
def create_mark():
    g = 1
    tu = len(Student)
    while g <= tu:
        g += 1
        mid = input("Enter the Student ID: ")
        if mid in Student:
            for i in range(0, len(CourseID)):
                nid = input("Enter the Course ID: ")
                if nid in CourseID:
                    mark = float(input("Enter Student Mark: "))
                    m_add = {
                        'mid': mid,
                        'nid': nid,
                        'mark': mark
                    }
                else:
                    print("Student ID NOT FOUND !!")
                    break
                Mark.append(m_add)
        else:
            print("Course ID NOT FOUND !!")
            break


def show_list_student():
    print("----Student List----")
    for i in range(0, len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")


def show_list_course():
    print("----COURSE LIST----")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")


def show_mark():
    print("----STUDENTS MARK LIST----")
    for i in range(0, len(Mark)):
        print(f"ID-course: {Mark[i]['nid']} ID-Student: {Mark[i]['mid']}  mark:{Mark[i]['mark']}")


# main
s = int(student_num())
l = 1
while l <= s:
    l += 1
    add_student()
show_list_student()

c = int(course_num())
p = 1
while p <= c:
    p += 1
    add_course()
show_list_course()


create_mark()
for i in range(0, len(CourseID)):
    print("Show mark? 1. YES  2. NO")
    ol = int(input("You Choose: "))
    if ol == 1:
        print("--STUDENT MARK--")
        show_mark()
        break
    else:
        break
