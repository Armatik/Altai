import os


# Инициализация пакета установки minimal
class Minimal:
    # Инициализация класса
    def __init__(self):
        pass

    def progress_bar(self, percent, clear=True):
        # Очищаем последнюю строку если clear = True
        if clear:
            os.system("clear")
        # Выводим прогресс бар длинной в 50 символов и заполненный на percent процентов
        print("[", end="")
        for i in range(0, 50):
            if i < percent / 2:
                print("#", end="")
            else:
                print("-", end="")
        # Выводим текущий процент выполнения
        print("] - " + str(percent) + "%")



    # Установка/удаление пакетов из minimal/package_list.txt
    def install_packages(self):
        try:
            # Открываем файл с пакетами
            package_list = open("minimal/package_list.txt", "r")
            # Считываем все строки из файла
            package_list_lines = package_list.readlines()
            # Закрываем файл
            package_list.close()

            # Считаем количество строк в файле
            package_list_lines_count = len(package_list_lines)
            self.progress_bar(3)

            # Отбираем названия пакетов для удаления исходя из синтаксиса remove название пакета
            remove_packages = []
            for i in range(0, package_list_lines_count):
                # Если строка начинается с remove то добавляем название пакета в список без remove и пробела
                if package_list_lines[i].startswith("remove"):
                    remove_packages.append(package_list_lines[i][7:])
            self.progress_bar(6)

            # Отбираем названия пакетов для установки исходя из синтаксиса install название пакета
            install_packages = []
            for i in range(0, package_list_lines_count):
                # Если строка начинается с install то добавляем название пакета в список без install и пробела
                if package_list_lines[i].startswith("install"):
                    install_packages.append(package_list_lines[i][8:])
            self.progress_bar(10)

            # Удаляем выбранные пакеты. Бюджет процентов на все пакеты 20%. С каждым удалённым пакетом увеличиваем
            # заполнение прогресс бара на 20/количество_пакетов.
            for i in range(0, len(remove_packages)):
                # Удаляем пакет
                os.system("apt-get -qq install" + remove_packages[i] + " &> /dev/null")
                # Увеличиваем процент выполнения
                self.progress_bar(10 + (20 / len(remove_packages) * i))

            # Устанавливаем выбранные пакеты. Бюджет процентов на все пакеты 40%. С каждым установленным пакетом увеличиваем
            # заполнение прогресс бара на 40/количество_пакетов.
            for i in range(0, len(install_packages)):
                # Устанавливаем пакет
                os.system("apt-get -qq install " + install_packages[i] + " &> /dev/null")
                # Увеличиваем процент выполнения
                self.progress_bar(30 + (40 / len(install_packages) * i))
        except:
            print("Ошибка при установке/удалении пакетов пакета minimal! Обратитесь в https://t.me/alt_gnome_chat за помощью.")


    # Выполнение команд из minimal/commands_list.txt
    def run_commands(self):
        # Открываем файл с командами
        commands_list = open("minimal/commands_list.txt", "r")
        # Считываем все строки из файла
        commands_list_lines = commands_list.readlines()
        # Закрываем файл
        commands_list.close()

        # Считаем количество строк в файле
        commands_list_lines_count = len(commands_list_lines)

        # Выполняем команды. Бюджет процентов на все команды 30%. С каждой выполненной командой увеличиваем
        # заполнение прогресс бара на 30/количество_команд.
        for i in range(0, commands_list_lines_count):
            if commands_list_lines[i].split(" ")[0] == "nosu":
                # Проверяем наличие файла nosu.txt рядом с файлом author.py
                if os.path.exists("nosu.txt") != True:
                    # Если файла нет, то создаём его
                    os.system("touch nosu.txt")
                # Открываем файл и добавляем в него команду без nosu
                nosu_file = open("nosu.txt", "a")
                nosu_file.write(commands_list_lines[i].replace("nosu ", ""))
                nosu_file.close()
            else:
                # Выполняем команду
                os.system(commands_list_lines[i] + " &> /dev/null")
            self.progress_bar(70 + (30 / commands_list_lines_count * i), False)


    # Инициализация установки
    def initialization(self):
        print("Запуск установки minimal")
        self.progress_bar(0)
        self.install_packages()
        self.run_commands()
        self.progress_bar(100)
        
        print("Установка пакета minimal завершена успешно!")
        # Если есть файл nosu.txt, то не предлагаем перезагрузку
        if os.path.exists("nosu.txt") != True:
            print("Настоятельно рекомендуем перезагрузить компьютер для корректной работы пакета author.")
            print("Перезагрузить компьютер сейчас? (Да/нет)")
            answer = input()
            if answer == "Да" or answer == "да" or answer == "":
                os.system("reboot")
            else:
                print("Перезагрузку можно выполнить в любое удобное время командой reboot.")

