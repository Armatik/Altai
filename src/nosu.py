import os

class Nosu():

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

    def run_no_su(self):
        # Считываем все строки из файла nosu.txt
        nosu = open("nosu.txt", "r")
        nosu_lines = nosu.readlines()
        nosu.close()

        # Считаем количество строк в файле
        nosu_lines_count = len(nosu_lines)
        self.progress_bar(3)

        # Выполняем команды из файла nosu.txt
        for i in range(0, nosu_lines_count):
            if nosu_lines[i].split(" ")[0] == "setwallpaper":
                # Получаем путь к текущей директории
                current_dir = os.getcwd()
                # Получаем путь к файлу с обои
                wallpaper_path = current_dir + nosu_lines[i].split(" ")[1]
                # Устанавливаем обои
                os.system("gsettings set org.gnome.desktop.background picture-uri " + wallpaper_path)
                os.system("gsettings set org.gnome.desktop.screensaver picture-uri-dark " + wallpaper_path)
            else:
                os.system(nosu_lines[i])
                self.progress_bar(3 + i * 96 / nosu_lines_count)

        # Удаляем файл nosu.txt
        os.system("rm nosu.txt")


    def nosu_start(self):
        self.progress_bar(0)
        self.run_no_su()
        self.progress_bar(100)




