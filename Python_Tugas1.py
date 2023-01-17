down = 0
up = 100
for i in range(1,10):
    guessed_age = int((up + down) / 2)
    answer = input('Are you ' + str(guessed_age) + " years old ")
    if answer == 'corret':
        print("Nice")
        break
    elif answer == 'less':
        up = guessed_age
    elif answer == 'more':
        down = guessed_age
    else:
        print('wrong answare')
