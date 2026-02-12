student={"name":"suraj","age":24,"cource":"mca","markes":560,"grade":"a"}
print(student.keys())

print(student.values())

print(student.items())

print(student.get("age"))

print(student.get("cource"))

student.update({"markes":600,"grade":"A+"})
print(student)

student.pop("cource")
print(student)

student.clear()
print(student)
