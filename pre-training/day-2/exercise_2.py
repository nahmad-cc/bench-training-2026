def calculate_average(scores):
    total = sum(scores)
    avg = total / len(scores)
    return avg


def get_grade(avg):
    if avg >= 90:
        return 'Distinction'
    elif avg >= 60:
        return 'Pass'
    else:
        return 'Fail'


def class_topper(students):
    best_student = None
    best_avg = 0
    
    for s in students:
        avg = calculate_average(s['scores'])
        if avg > best_avg:
            best_avg = avg
            best_student = s
    
    return best_student


students = [
    {'name': 'Ali Khan', 'scores': [85, 90, 88], 'subject': 'Math'},
    {'name': 'Fatima Ahmed', 'scores': [92, 95, 91], 'subject': 'English'},
    {'name': 'Hassan Ali', 'scores': [78, 82, 80], 'subject': 'Science'},
    {'name': 'Zara Khan', 'scores': [88, 86, 89], 'subject': 'History'},
    {'name': 'Umer Hassan', 'scores': [75, 77, 76], 'subject': 'Geography'}
]

topper = class_topper(students)

# make a list with names and averages
report = []
for student in students:
    name = student['name']
    avg = calculate_average(student['scores'])
    grade = get_grade(avg)
    report.append((name, avg, grade))

# sort by average
for i, _ in enumerate(report):
    for j in range(i+1, len(report)):
        if report[j][1] > report[i][1]:
            report[i], report[j] = report[j], report[i]

print("Class Report")
for name, avg, grade in report:
    if name == topper['name']:
        print(f"*** TOP *** {name} | {avg:.1f} | {grade}")
    else:
        print(f"{name} | {avg:.1f} | {grade}")
