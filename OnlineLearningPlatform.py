from abc import ABC, abstractmethod

# Abstract class
class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def course_details(self):
        pass


# Subclass 1: Programming Course
class ProgrammingCourse(Course):
    def course_details(self):
        print(f"Course: {self.course_name}")
        print(f"Duration: {self.duration}")
        print("Includes coding exercises and real-world projects.\n")


# Subclass 2: Design Course
class DesignCourse(Course):
    def course_details(self):
        print(f"Course: {self.course_name}")
        print(f"Duration: {self.duration}")
        print("Focuses on UI/UX principles and creative tools.\n")


# Subclass 3: Marketing Course
class MarketingCourse(Course):
    def course_details(self):
        print(f"Course: {self.course_name}")
        print(f"Duration: {self.duration}")
        print("Covers digital marketing strategies and branding.\n")


# Creating objects
course1 = ProgrammingCourse("Python Development", "3 Months")
course2 = DesignCourse("Graphic Design Mastery", "2 Months")
course3 = MarketingCourse("Digital Marketing Pro", "1.5 Months")

# Displaying course details
courses = [course1, course2, course3]

for course in courses:
    course.course_details()