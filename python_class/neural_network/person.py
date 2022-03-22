class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self    ):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

class Person(AttrDisplay):
    def __init__(self, name, number, tel = None):
        self.name = name   
        self.number = number
        self.tel = tel
  
class Teacher(Person):
    def info(course):
        if self.name == course.teacher:
            print(course)
        
class Student(Person):
    self.course = []
    def append(course):
        self.course.append(course)

class courses(Person):
    def set(teacher):
        self.teacher = teacher 
        
if __name__ == '__main__':
    studen = []     #20
    teacher = []    #6
    course = []     #3
































