import os
import sys

import default

from settings_packs import Author
from settings_packs import Minimal


class TerminalSession:
    terminal_session = None

    def __init__(self):
        self.terminal_session = True
        pass

    def run(self):
        #TODO Подключение конфига
        print("Запуск Алтая! Издание: Прототип 0.7")
        # Выводим файл приветствия в терминал
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
            minimal = Minimal(terminal_session=True)
            minimal.run_minimal_settings_pack()
        elif user_choice == "a":
            default.eepm()
            author = Author(terminal_session=True)
            author.run_author_settings_pack()
        elif user_choice == "s":
            default.eepm()

        user_choice = "u"
        while user_choice != "q":
            external = open("text/external.txt", "r")
            print(external.read())
            external.close()
            user_choice = input()
            if user_choice == "a":
                default.AMD_P_State()
            elif user_choice == "u":
                default.package_update()


        if os.path.exists("nosu.txt") != True:
            #TODO Добавить обозначение использования терминала, а не GUI для не su команд.
            print("Настоятельно рекомендуем перезагрузить компьютер!")
            print("Перезагрузить компьютер сейчас? (Да/нет)")
            answer = input()
            if answer == "Да" or answer == "да" or answer == "":
                os.system("reboot")
            else:
                print("Перезагрузку можно выполнить в любое удобное время командой reboot.")



