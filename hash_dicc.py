class student:
    def __init__(self,name,mark,rank):
        self.name = name
        self.mark = mark
        self.rank = rank

students = [student("alice",85,1), student("bob",90,2), student("charlie",75,3) ]        
student_rank = {}
for stud in students:
    student_rank[stud.name] = stud.rank

for name, rank in student_rank.items():
    print(f"{name}: {rank}")    



        