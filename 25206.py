# 너의 평점은
import sys

grade_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
             'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

total_credit = 0
total_grade = 0

for _ in range(20):
    subject, credit, grade = sys.stdin.readline().split()

    if grade != 'P':  # 등급이 P인 과목은 계산에서 제외
        credit = float(credit)
        total_credit += credit
        total_grade += grade_dic[grade] * credit

result = total_grade / total_credit
print(result)



