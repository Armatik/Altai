import os
import time


def log(message):
    current_date = time.strftime("%Y-%m-%d")

    # Проверяем наличия log файла с сегодняшней датой в названии в папке logs.
    # Если его нет, то создаём в название ставим текущую дату.
    if os.path.isfile("logs/" + current_date + ".log") != True:
        log_file = open("logs/" + current_date + ".log", "w")
        log_file.close()

    # Открываем log файл на запись
    log_file = open("logs/" + current_date + ".log", "a")
    # Записываем в log файл текущую дату и время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС и сообщение через тире
    log_file.write(time.strftime("%Y-%m-%d %H:%M:%S") + " - " + message + "\n")
    # Закрываем log файл
    log_file.close()


class Core:
    patch_to_dir = None
    terminal_session = None
    temp_percent = 0

    def __init__(self, terminal_session=True, patch_to_dir="None"):
        self.patch_to_dir = patch_to_dir
        self.terminal_session = terminal_session
        self.temp_percent = 0

    def progress_bar(self, process, percent, clear=True):
        if self.terminal_session:
            # Очищаем экран если clear = True
            if clear:
                os.system("clear")

            # Округляем процент до целого числа

            print(process + ":")

            # Выводим прогресс бар длинной в 50 символов и заполненный на percent процентов
            print("[", end="")
            for i in range(0, 50):
                if i < percent / 2:
                    print("#", end="")
                else:
                    print("-", end="")
            # Выводим текущий процент выполнения
            print("] - " + str(int(percent)) + "%")
            self.temp_percent = percent
            if percent == 100:
                self.temp_percent = 0

    def work_with_package(self):
        task_name = "Работаю с пакетами"
        self.progress_bar(task_name, 0)

        try:
            # Открываем файл с пакетами
            package_list = open(self.patch_to_dir + "package_list.txt", "r")
            # Считываем все строки из файла
            package_list_lines = package_list.readlines()
            # Закрываем файл
            package_list.close()

            # Считаем количество строк в файле
            package_list_lines_count = len(package_list_lines)
            self.progress_bar(task_name, 3)

        except Exception:
            log("Ошибка при открытии файла " + self.patch_to_dir + "package_list.txt")
            if self.terminal_session:
                print("Ошибка чтения файла " + self.patch_to_dir + "package_list.txt. Подробности в log файле.")
                print("Завершаю выполнения работы с пакетами")
                time.sleep(5)
            return

        try:
            # Отбираем названия пакетов для удаления и установки исходя из синтаксиса remove и install.
            remove_packages = []
            install_packages = []
            task_name = "Отбираю пакеты для удаления и установки"

            for i in range(0, package_list_lines_count):
                # Если строка содержит 2 элемента, то продолжаем работу
                if len(package_list_lines[i].split()) == 2:

                    # Если строка первым элементом содержит remove, то добавляем в список пакетов для удаления
                    if package_list_lines[i].split()[0] == "remove":
                        remove_packages.append(package_list_lines[i].split()[1])

                    # Если строка первым элементом содержит install, то добавляем в список пакетов для установки
                    elif package_list_lines[i].split()[0] == "install":
                        install_packages.append(package_list_lines[i].split()[1])

                else:
                    log("Ошибка в синтаксисе файла " + self.patch_to_dir + "package_list.txt. Строка " + str(
                        i + 1) + " содержит "
                        + str(len(package_list_lines[i].split())) + " элементов вместо 2.")
                    log("Строка: " + package_list_lines[i])

                    if self.terminal_session:
                        print("Незначительная ошибка, информация записана в log файл.")
                        print("Продолжаю работу.")
                        time.sleep(3)

                self.progress_bar(task_name, self.temp_percent + (12 / package_list_lines_count))

        except Exception:
            log("Ошибка при отборе пакетов для удаления и установки")
            if self.terminal_session:
                print("Ошибка при отборе пакетов для удаления и установки. Подробности в log файле.")
                print("Завершаю выполнения работы с пакетами")
                time.sleep(5)
            return

        # Удаляем выбранные пакеты. Бюджет процентов на все пакеты 25%. С каждым удалённым пакетом увеличиваем
        print("Собираюсь удалить пакеты: " + str(remove_packages))
        print("Подтвердите удаление пакетов Да\нет")
        answer = input().lower
        if answer == "да" or answer == "д" or answer == "y" or answer == "":
            os.system("clear")
            task_name = "Удаляю пакеты"
            print()
            for i in range(0, len(remove_packages)):
                try:
                    # Удаляем пакет
                    os.system("apt-get -qq remove" + remove_packages[i] + " &> /dev/null")
                    # Увеличиваем процент выполнения
                    self.progress_bar(task_name, self.temp_percent + (25 / len(remove_packages) * i))
                except Exception:
                    log("Ошибка при удалении пакета " + remove_packages[i])

        # Устанавливаем выбранные пакеты. Бюджет процентов на все пакеты 60%. С каждым установленным пакетом увеличиваем
        task_name = "Устанавливаю пакеты"
        for i in range(0, len(install_packages)):
            try:
                # Устанавливаем пакет
                os.system("apt-get -qq install " + install_packages[i] + " &> /dev/null")
                # Увеличиваем процент выполнения
                self.progress_bar(task_name, self.temp_percent + (60 / len(install_packages) * i))
            except Exception:
                log("Ошибка при установке пакета " + install_packages[i])

        task_name = "Завершаю работу с пакетами"
        self.progress_bar(task_name, 100)
        time.sleep(2)

    def work_with_file(self, patch_to_list, patch_to_folder_with_file):
        task_name = "Работаю с файлами"
        self.progress_bar(task_name, 0)
        current_dir = os.getcwd()

        try:
            # Открываем файл с пакетами
            file_list = open(patch_to_list + "file_list.txt", "r")
            # Считываем все строки из файла
            file_list_lines = file_list.readlines()
            # Закрываем файл
            file_list.close()

            # Считаем количество строк в файле
            file_list_lines_count = len(file_list_lines)
            self.progress_bar(task_name, 3)

        except Exception:
            log("Ошибка при открытии файла " + patch_to_list + "file_list.txt")
            if self.terminal_session:
                print("Ошибка чтения файла " + patch_to_list + "file_list.txt. Подробности в log файле.")
                print("Завершаю выполнения работы с файлами")
                time.sleep(5)
            return

        try:
            # Формируем словарь с ключом в виде имени файла, а значением в виде пути к файлу
            file_list_dict = {}
            task_name = "Формирую словарь с файлами"

            for i in range(0, file_list_lines_count):
                # Если строка содержит 2 элемента, то продолжаем работу
                if len(file_list_lines[i].split()) == 2:
                    file_list_dict[file_list_lines[i].split()[0]] = file_list_lines[i].split()[1]
                else:
                    log("Ошибка в синтаксисе файла " + patch_to_list + "file_list.txt. Строка " + str(
                        i + 1) + " содержит "
                        + str(len(file_list_lines[i].split())) + " элементов вместо 2.")
                    log("Строка: " + file_list_lines[i])

                    if self.terminal_session:
                        print("Незначительная ошибка, информация записана в log файл.")
                        print("Продолжаю работу.")
                        time.sleep(3)

                self.progress_bar(task_name, self.temp_percent + (12 / file_list_lines_count))

        except Exception:
            log("Ошибка при формировании словаря с файлами")
            if self.terminal_session:
                print("Ошибка при формировании словаря с файлами. Подробности в log файле.")
                print("Завершаю выполнения работы с файлами")
                time.sleep(5)
            return

        try:
            # Переходим в папку с файлами
            os.chdir(patch_to_folder_with_file)
            task_name = "Копирую файлы"
            self.progress_bar(task_name, 15)
            i = 0

            # Копируем файлы согласно словарю в папку с файлами
            for key in file_list_dict:
                try:
                    i += 1
                    os.system("cp " + file_list_dict[key] + " " + key)
                    self.progress_bar(task_name, self.temp_percent + (85 / len(file_list_dict) * i))

                except Exception:
                    log("Ошибка при копировании файла " + key)
                    if self.terminal_session:
                        print("Ошибка при копировании файла " + key + ". Подробности в log файле.")
                        print("Продолжаю работу.")
                        time.sleep(3)
            i = 0

        except Exception:
            log("Ошибка при копировании файлов")
            if self.terminal_session:
                print("Ошибка при копировании файлов. Подробности в log файле.")
                print("Завершаю выполнения работы с файлами")
                time.sleep(5)
            return

        task_name = "Завершаю работу с файлами"
        self.progress_bar(task_name, 100)
        time.sleep(2)

    def work_with_command(self, file_full_patch):
        task_name = "Работаю с командами"
        self.progress_bar(task_name, 0)

        try:
            # Открываем файл с пакетами
            command_list = open(file_full_patch, "r")
            # Считываем все строки из файла
            command_list_lines = command_list.readlines()
            # Закрываем файл
            command_list.close()

            # Считаем количество строк в файле
            command_list_lines_count = len(command_list_lines)
            self.progress_bar(task_name, 3)

        except Exception:
            log("Ошибка при открытии файла " + file_full_patch)
            if self.terminal_session:
                print("Ошибка чтения файла " + file_full_patch + ". Подробности в log файле.")
                print("Завершаю выполнения работы с командами")
                time.sleep(5)
            return

        try:
            # Выполняем команды из файла
            task_name = "Выполняю команды"
            for i in range(0, command_list_lines_count):
                try:
                    if command_list_lines[i].startswith("nosu "):
                        # Проверяем наличие файла nosu.txt рядом с файлом core.py
                        if os.path.exists("nosu.txt") != True:
                            # Если файла нет, то создаём его
                            os.system("touch nosu.txt")
                            # Разрешаем любому пользователю любой доступ к файлу
                            os.system("chmod 777 nosu.txt")

                        # Открываем файл и добавляем в него команду без nosu
                        nosu_file = open("nosu.txt", "a")
                        nosu_file.write(command_list_lines[i].replace("nosu ", ""))
                        nosu_file.close()
                    else:
                        os.system(command_list_lines[i])
                        self.progress_bar(task_name, self.temp_percent + (97 / command_list_lines_count * i))

                except Exception:
                    log("Ошибка при выполнении команды " + command_list_lines[i])
                    if self.terminal_session:
                        print("Ошибка при выполнении команды " + command_list_lines[i] + ". Подробности в log файле.")
                        print("Продолжаю работу.")
                        time.sleep(3)

        except Exception:
            log("Критическая ошибка выполнения команд!")
            if self.terminal_session:
                print("Ошибка при выполнении команд. Подробности в log файле.")
                print("Завершаю выполнения работы с командами")
                time.sleep(5)
            return

        task_name = "Завершаю работу с командами"
        self.progress_bar(task_name, 100)
        time.sleep(2)
