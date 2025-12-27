class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber,scores):
        super().__init__(firstName, lastName, idNumber) # hàm super() giúp gọi lại 3 biến firstName, lastName, idNumber mà ở trên class person đã gán
        self.scores = scores
   
    def calculate(self):
        result = sum(self.scores) / (len(self.scores))
        if result < 40:
            return "T"
        elif 40 <= result < 55:
            return "D"
        elif 55 <= result < 70:
            return "P"
        elif 70 <= result < 80:
            return 'A'
        elif 80 <= result < 90:
            return 'E'
        elif 90 <= result <= 100:
            return 'O'
            
    
   

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())