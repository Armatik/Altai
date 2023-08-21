import os


# Инициализация пакета установки author
class Author:
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
            package_list = open("author/package_list.txt", "r")
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
                os.system("apt-get --qq remove " + remove_packages[i] + "&> /dev/null")
                # Увеличиваем процент выполнения
                self.progress_bar(10 + (20 / len(remove_packages) * i))

            # Устанавливаем выбранные пакеты. Бюджет процентов на все пакеты 40%. С каждым установленным пакетом увеличиваем
            # заполнение прогресс бара на 40/количество_пакетов.
            for i in range(0, len(install_packages)):
                # Устанавливаем пакет
                os.system("apt-get -qq install " + install_packages[i] + "&> /dev/null")
                # Увеличиваем процент выполнения
                self.progress_bar(30 + (40 / len(install_packages) * i))
        except:
            print("Ошибка при установке/удалении пакетов пакета author! Обратитесь в https://t.me/alt_gnome_chat за помощью.")


    def move_files(self):
        try:
            # Открываем файл с файлами
            file_list = open("author/file_to_copy.txt", "r")
            # Считываем все строки из файла
            file_list_lines = file_list.readlines()
            # Закрываем файл
            file_list.close()

            # считаем количество строк в файле
            file_list_lines_count = len(file_list_lines)

            # Формируем словарь с названием файла в виде ключа и путём к файлу в виде значения. Бюджет процентов на все
            # файлы 5%
            files = {}
            for i in range(0, file_list_lines_count):
                # Первое слово строки название файла, остальное путь к файлу
                file_name = file_list_lines[i].split(" ")[0]
                file_path = file_list_lines[i].split(" ")[1]
                # Добавляем в словарь
                files[file_name] = file_path
                # Увеличиваем процент выполнения
                self.progress_bar(80 + (5 / file_list_lines_count * i))

            # Перемещаем файлы из author/file по указанному пути, при необхадимости перезаписываем файлы. Бюджет
            # процентов на все файлы 5%
            for i in range(0, len(files)):
                # Перемещаем файл
                os.system("cp author/file/" + list(files.keys())[i] + " " + list(files.values())[i] + " &> /dev/null")
                # Увеличиваем процент выполнения
                self.progress_bar(85 + (5 / len(files) * i))
        except:
            print("Ошибка при перемещения файлов пакета author! Обратитесь в https://t.me/alt_gnome_chat за помощью.")


    # Выполнение команд из author/commands_list.txt
    def run_commands_before(self):
        try:
            # Открываем файл с командами
            commands_list = open("author/command_list_before_copy.txt", "r")
            # Считываем все строки из файла
            commands_list_lines = commands_list.readlines()
            # Закрываем файл
            commands_list.close()

            # Считаем количество строк в файле
            commands_list_lines_count = len(commands_list_lines)

            # Выполняем команды. Бюджет процентов на все команды 10%. С каждой выполненной командой увеличиваем
            # заполнение прогресс бара на 10/количество_команд.
            for i in range(0, commands_list_lines_count):
                # Выполняем команду
                os.system(commands_list_lines[i] + " &> /dev/null")
                # Увеличиваем процент выполнения
                self.progress_bar(70 + (10 / commands_list_lines_count * i))
        except:
            print("Ошибка при выполнении команд пакета author! Обратитесь в https://t.me/alt_gnome_chat за помощью.")

        # Выполнение команд из author/commands_list.txt

    def run_commands_after(self):
        try:
            # Открываем файл с командами
            commands_list = open("author/command_list_after_copy.txt", "r")
            # Считываем все строки из файла
            commands_list_lines = commands_list.readlines()
            # Закрываем файл
            commands_list.close()

            # Считаем количество строк в файле
            commands_list_lines_count = len(commands_list_lines)

            # Выполняем команды. Бюджет процентов на все команды 10%. С каждой выполненной командой увеличиваем
            # заполнение прогресс бара на 10/количество_команд.
            for i in range(0, commands_list_lines_count):
                # Выполняем команду
                os.system(commands_list_lines[i] + " &> /dev/null")
                # Увеличиваем процент выполнения
                self.progress_bar(70 + (10 / commands_list_lines_count * i))
        except:
            print("Ошибка при выполнении команд пакета author! Обратитесь в https://t.me/alt_gnome_chat за помощью.")


    def replace_text(self):
        try:
            # Открываем файл с текстом
            text_list = open("author/replace_text.txt", "r")
            # Считываем все строки из файла
            text_list_lines = text_list.readlines()
            # Закрываем файл
            text_list.close()

            # считаем количество строк в файле
            text_list_lines_count = len(text_list_lines)

            # Формируем двух мерный список каждый элемент которого содержит путь до файла который нужно изменить, что и
            # на что заменить. Бюджет процентов на все файлы 5%
            text = []
            for i in range(0, text_list_lines_count):
                # Первое слово строки путь до файла, второе что заменить, третье на что заменить
                file_path = text_list_lines[i].split(" ")[0]
                replace_from = text_list_lines[i].split(" ")[1]
                replace_to = text_list_lines[i].split(" ")[2]
                # Добавляем в список
                text.append([file_path, replace_from, replace_to])
                # Увеличиваем процент выполнения
                self.progress_bar(90 + (5 / text_list_lines_count * i))

            # Заменяем текст в файлах
            for i in range(0, len(text)):
                replace_from = text[i][1]
                replace_to = text[i][2]

                # Открываем файл
                file = open(text[i][0], "r")
                # Считываем все строки из файла
                file_lines = file.readlines()
                # Закрываем файл
                file.close()

                # Открываем файл на запись
                file = open(text[i][0], "w")
                # Заменяем текст строки при совпадении с replace_from на replace_to
                for j in range(0, len(file_lines)):
                    if file_lines[j] == replace_from:
                        file_lines[j] = replace_to
                # Записываем изменённый текст в файл
                file.writelines(file_lines)
                # Закрываем файл
                file.close()

                # Увеличиваем процент выполнения
                self.progress_bar(90 + (5 / len(text) * i))

        except:
            print("Ошибка при замене текста в файлах пакета author! Обратитесь в https://t.me/alt_gnome_chat за помощью.")


    # Инициализация установки
    def initialization(self):
        print("Запуск установки author")

        self.progress_bar(0, False)
        self.install_packages()
        self.run_commands_before()
        self.move_files()
        self.run_commands_after()
        self.replace_text()
        self.progress_bar(100)

        print("Установка пакета author завершена успешно!")
        print("Настоятельно рекомендуем перезагрузить компьютер для корректной работы пакета author.")
        print("Перезагрузить компьютер сейчас? (Да/нет)")
        answer = input()
        if answer == "Да" or answer == "да" or answer == "":
            os.system("reboot")
        else:
            print("Перезагрузку можно выполнить в любое удобное время командой reboot.")

