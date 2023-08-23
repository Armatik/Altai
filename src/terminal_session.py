import os
import sys

import default

from settings_packs import Author
from settings_packs import Minimal
from settings_packs import Game
from settings_packs import WpsOffice
from settings_packs import EEPM


class TerminalSession:
    terminal_session = None

    def __init__(self):
        self.terminal_session = True
        pass

    def run(self):
        #TODO Подключение конфига
        print("Запуск Алтая! Издание: Прототип 0.8")
        # Выводим файл приветствия в терминал
        self.print_welcome()

    def exit(self):
        print("Завершение работы Алтая!")
        sys.exit(0)


    def print_welcome(self):
        eepm = EEPM(terminal_session=True)
        eepm.run_default_eepm()
        os.system("clear")

        # выводим файл привествия из text/welcome.txt
        welcome_file = open("text/welcome.txt", "r")
        print(welcome_file.read())
        welcome_file.close()
        user_choice = input()
        if user_choice == "m":
            minimal = Minimal(terminal_session=True)
            minimal.run_minimal_base_pack()
        elif user_choice == "a":
            author = Author(terminal_session=True)
            author.run_author_base_pack()
        elif user_choice == "s":
            os.system("clear")
        else:
            self.exit()

        user_choice = "u"
        while user_choice != "q":
            external = open("text/external.txt", "r")
            print(external.read())
            external.close()
            if os.path.exists("nosu.txt") == True:
                print("ВНИМАНИЕ! Алтаю требуется выполнить часть команд от имени пользователя.\n"
                      "Пожалуйста, при завершении работы с Алтаем, используйте предусмотренную команду: q для выхода.")
            user_choice = input()
            if user_choice == "game":
                Game(terminal_session=True).run_game_extra_pack()
            elif user_choice == "wps":
                WpsOffice(terminal_session=True).run_wps_office_extra_pack()
            if user_choice == "a":
                default.AMD_P_State()
            elif user_choice == "u":
                default.package_update()

        if os.path.exists("nosu.txt") != True:
            print("Настоятельно рекомендуем перезагрузить компьютер!")
            print("Перезагрузить компьютер сейчас? (Да/нет)")
            answer = input()
            if answer == "Да" or answer == "да" or answer == "":
                os.system("reboot")
            else:
                print("Перезагрузку можно выполнить в любое удобное время командой reboot.")



