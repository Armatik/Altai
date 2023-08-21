import os
import sys
import GUI

from terminal_session import TerminalSession


def check_su_privilages():
    if os.geteuid() != 0:
        print("Вам необходимо запустить программу с правами суперпользователя из директории altai командой\n"
              "sudo python3 src/main.py \n"
              "или \n"
              "su - \n"
              "python3 /путь/до/файла/altai/src/main.py")
        sys.exit(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_su_privilages()
    terminal_session = TerminalSession()
    terminal_session.run()

    # app = GUI.AltaiApplication()
    # app.run(sys.argv)



