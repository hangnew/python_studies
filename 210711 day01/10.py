english = input('영어 점수 입력: ')
math = input('수학 점수 입력: ')
korean = input('국어 점수 입력: ')
sum = int(english) + int(math) + int(korean)
avg = int(sum / 3)
print('세 과목의 합은', sum, '점')
print('세 과목의 평균은', avg, '점')
