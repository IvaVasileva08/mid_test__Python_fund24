first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

total = first_employee + second_employee + third_employee
need_hour = 0
while students_count > 0:
    need_hour += 1
    if need_hour % 4 == 0:
        continue

    students_count -= total
print(f"Time needed: {need_hour}h.")