import os
import sys

import default
import minimal
import author


class TerminalSession:

    def __init__(self):
        pass

    def run(self):
        print("Запуск Алтая! Издание: Прототип 0.3")
        # Выводим файл привествия в терминал
        self.print_welcome()

    def exit(self):
        print("Завершение работы Алтая!")
        sys.exit(0)


    def print_welcome(self):
        # выводим файл привествия из text/welcome.txt
        welcome_file = open("text/welcome.txt", "r")
        print(welcome_file.read())
        welcome_file.close()
        user_choice = input()
        if user_choice == "q":
            self.exit()
        elif user_choice == "m":
            default.eepm()
            minimal.Minimal().initialization()
        elif user_choice == "a":
            default.eepm()
            author.Author().initialization()



