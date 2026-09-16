maths_mark = int(input('What\'s your score in Maths?'))
english_mark = int(input('What\'s your score in English?'))
science_mark = int(input('What\'s your score in Science?'))
economics_mark = int(input('What\'s your score in Economics?'))
malayalam_mark = int(input('What\'s your score in Malayalam?'))
total = maths_mark + english_mark + science_mark + economics_mark + malayalam_mark
average = total / 5
print(f"Total: {total}")
print(f"Average: {average}")
if average >= 90 and average <= 100:
    print('Grade: A')
elif average >= 75:
    print('Grade: B')
elif average >= 50:
    print('Grade: C')
else:
    print('Fail')