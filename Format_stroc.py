# Использование %:

team1_num = 5
team2_num = 6
print("В команде 'Мастера кода' участников: %s!" % (team1_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))


# Использование format():

score1 = 42
score2 = 40
team1_time = 18015.2
team2_time = 10717.6

print('Команда "Волшебники данных" решила задач: {}!'.format(score1))
print('Команда "Мастера кода" решила задач: {}!'.format(score2))
print('"Волшебники данных" решили задачи за {}!'.format(team1_time))
print('"Мастера кода" решили задачи за {}!'.format(team2_time))


# Использование f-строк:

challenge_result = 'Кто то должен победить!!!'
tasks_total = 82
time_avg = 45.2

print(f'Команды решили {score1} и {score2} задач.')
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
#print(f'Результат битвы: {challenge_result}')


if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}')