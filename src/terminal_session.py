import os
import sys
import time
import rich
from rich.console import Console


import default

from settings_packs import Author
from settings_packs import Minimal
from settings_packs import Game
from settings_packs import WpsOffice
from settings_packs import EEPM


class TerminalSession:
    terminal_session = None
    console = Console()

    def __init__(self):
        self.terminal_session = True
        console = Console()
        pass

    def run(self):
        #TODO Подключение конфига
        self.console.print("Запуск CLI([yellow]legacy[/yellow]) версии [bold green]Алтай[/bold green] | Прототип 0.10")
        # Выводим файл приветствия в терминал
        self.print_welcome()

    def exit(self):
        self.console.print("[bold red]Завершение работы [green]Алтая![/green][/bold red]")
        time.sleep(2)
        sys.exit(0)


    def print_welcome(self):
        eepm = EEPM(terminal_session=True)
        eepm.run_default_eepm()
        os.system("clear")

        # выводим файл привествия из text/welcome.txt
        welcome_file = open("text/welcome.txt", "r")
        self.console.print(welcome_file.read())
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
            self.console.print(external.read())
            external.close()
            if os.path.exists("nosu.txt") == True:
                self.console.print("[bold red]ВНИМАНИЕ![/bold red] [bold green]Алтаю[/bold green] требуется выполнить часть команд от имени пользователя.\n"
                      "[bold]Пожалуйста, при завершении работы с Алтаем, используйте предусмотренную команду: [white]q[/white] для выхода.[/bold]")
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
            self.console.print("Настоятельно рекомендуем перезагрузить компьютер!")
            self.console.print("Перезагрузить компьютер сейчас? ([bold][green]Да[/green]/[red]нет[/red][/bold])")
            answer = input()
            if answer == "Да" or answer == "да" or answer == "":
                os.system("reboot")
            else:
                self.console.print("Перезагрузку можно выполнить в любое удобное время командой [mono]reboot[/mono].")
                time.sleep(5)



