n, x = map(int, input().split())

matrix = []
for x in range(x):
    element = list(map(float, input().split()))
    matrix.append(element)

student_score = list(zip(*matrix))
for score in student_score:
    average = sum(score) / len(score)
    print(average)


