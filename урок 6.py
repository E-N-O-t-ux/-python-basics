a = 10while a > 0:    print(a)    a -= 1##password = "adminpass"psw = input("Введите пароль")while psw != password:    psw = input("Пароль неверный")print("Добро пожаловать!")##a = 1while True:    print("Да")    if a == 10:        break##login = input("Введите логин")password = input("Введите пароль")while login != "meadmin" or password != "adminpass":    print("Неверный логин или пароль, попробуйте еще раз")    password = input("Введите пароль")print("Добро пожаловать!")##def check(login, password):    login_secret = "admin"    password_secret = "adminpass"    if login != login_secret or password != password_secret:        return True    else:        return False# ## #flag = 5login = input("Введите логин")password = input("Дай пароль")while check(login, password):    print("Вы Ввели не правильно, попробуйте еще раз")    flag -= 1    if flag <= 0:        break    login = input("введите логин")    password = input("Введите пароль")print("Попробуйте завтра")##num_1 = int(input("Введи число"))secret_number = 7while num_1 != secret_number:    num = int(input("Угадай число от 1 до 10"))