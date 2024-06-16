# 1) Метод старый с помощью % (2 варианта, сразу число или через переменную)
team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s !' % (team1_num))
print('В команде Мастера кода участников: %d !' % 5)

print('Итого сегодня в командах участников: %d и %d !' % (5, 6))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# 2) Метод новый с помощью .format() (2 варианта, сразу число или через переменную)
score_2 = 42
print('Команда Волшебники данных решила задач: {0} !'.format(score_2))
print('Команда Волшебники данных решила задач: {0} !'.format(42))
team1_time = 18015.2
print('Волшебники данных решили задачи за {0} с !'.format(team1_time))
print('Волшебники данных решили задачи за {0} с !'.format(18015.2))
team2_time = 18013.2
# 3) Метод новейший с помощью f строк.
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')

# Итоги соревнований:

if score_1 > score_2 or score_1 == score_2 and team2_time > team1_time:
    challenge_result = 'Результаты битвы: победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team2_time < team1_time:
    challenge_result = 'Результаты битвы: победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

tasks_total = score_2 + score_1
time_avg = (team1_time + team2_time) / 2
print(f"Сегодня было решено {tasks_total} задач, в среднем по {(team1_time + team2_time) / 2} секунды на задачу!.")
print(challenge_result)
