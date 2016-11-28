# Class
# Author : xiaosean
# Date : 20161025
class Student(object):
    """docstring for Studen"""
    # http://stackoverflow.com/questions/9056957/correct-way-to-define-class-variables-in-python
    # Elements outside the __init__ method are static elements, it means, they belong to the class.
    # Elements inside the __init__ method are elements of the object (self), they don't belong to the class.
    def __init__(self, id, name, *args):
        super(Student, self).__init__()
        # 學號
        self.id = id
        # 姓名
        self.name = name   
        # 成績
        self.score = []
        for i in args:
            self.score.append(i)
    def __str__(self):
        return "學號為%s 姓名為%s 成績平均為%s" % (self.id, self.name, self.__avg())
    def __avg(self):
        if len(self.score) > 0:
            return sum(self.score) / len(self.score)
        return 0
    def add_score(self, score):
        self.score.append(score)
if __name__ == '__main__':
    student1 = Student("4", "林小翔")
    student1.add_score(80)
    student1.add_score(100)
    student1.add_score(100)
    print(student1)
    print(Student("5","Toby", 90, 85 , 100, 100, 90))
    print(Student("6","Richard", 90, 85 , 100, 100, 100, 100, 100, 100))