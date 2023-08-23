import os
import sys
from terminal_session import TerminalSession
from core import Core
# from nosu import Nosu



# TODO Придумать другую реализацию выполнения не su команд. Как вариант использовать subproccess.
def check_su_privilages():
    if os.geteuid() != 0:
        # Проверяем наличие файла nosu.txt
        if os.path.isfile("nosu.txt"):
            # Если файл есть, то запускаем nosu.start
            # nosu = Nosu()
            # nosu.nosu_start()

            core = Core()
            core.work_with_command("nosu.txt")
            # Если есть файл nosu.txt, то не предлагаем перезагрузку
            print("Настоятельно рекомендуем перезагрузить компьютер для корректной работы пакета author.")
            print("Перезагрузить компьютер сейчас? (Да/нет)")
            answer = input()
            if answer == "Да" or answer == "да" or answer == "":
                os.system("sudo reboot")
            else:
                print("Перезагрузку можно выполнить в любое удобное время командой reboot.")
        sys.exit(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_su_privilages()
    terminal_session = TerminalSession()
    terminal_session.run()

    # app = GUI.AltaiApplication()
    # app.run(sys.argv)



