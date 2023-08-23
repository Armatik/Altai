import time

from core import Core, log
import os


class Author:
    patch = "author/"
    file_patch = "author/files"
    terminal_session = None

    def __init__(self, terminal_session):
        self.terminal_session = terminal_session
        pass

    def run_author_base_pack(self):
        core = Core(self.terminal_session, self.patch)
        core.work_with_package()
        core.work_with_command((self.patch + "/command_list_after_copy.txt"))


class Minimal:
    patch = "minimal/"
    file_patch = None
    terminal_session = None

    def __init__(self, terminal_session):
        self.terminal_session = terminal_session
        pass

    def run_minimal_base_pack(self):
        core = Core(self.terminal_session, self.patch)
        core.work_with_package()
        core.work_with_command((self.patch + "/command_list.txt"))


class Game:
    patch = "game/"
    file_patch = None
    terminal_session = None

    def __init__(self, terminal_session):
        self.terminal_session = terminal_session
        pass

    def driver_info(self):
        try:
            lspci = os.popen("lspci -vnn | grep -i VGA -A 12").read()
            # Построчно проверяем вывод пока не найдём строку Kernel driver in use:
            if lspci == "":
                # Вызываем ошибку, если lspci пустой
                raise Exception
            if "NVIDIA" in lspci:
                return "nvidia"
            elif "[AMD/ATI]" in lspci:
                return "amdgpu"
            raise Exception
        except Exception:
            log("Не удалось определить видеокарту " + os.popen("lspci -vnn | grep -i VGA -A 12").read())

    def install_32_bit_libs(self):
        print("Установка 32-битных библиотек")
        gpu = self.driver_info()
        try:
            if "nvidia" in gpu:
                os.system("apt-get -qq install i586-xorg-dri-nouveau &> /dev/null")
            elif "amdgpu" in gpu:
                os.system("apt-get -qq install i586-xorg-dri-radeon &> /dev/null")
                os.system("apt-get -qq install i586-xorg-dri-swrast &> /dev/null")
            else:
                log("Не удалось определить видеокарту, вывод lspci:\n" + gpu)
                if self.terminal_session:
                    print("Не удалось определить видеокарту. Подробности в log файле, завершаю установку библиотек")
                    time.sleep(3)
                    os.system("clear")
                    return
        except Exception:
            log("Не удалось установить 32-битные библиотеки gpu: " + gpu)
            if self.terminal_session:
                print("Не удалось установить 32-битные библиотеки. Подробности в log файле, завершаю установку библиотек")
                time.sleep(3)
                os.system("clear")
                return
        print("Установка 32-битных библиотек завершена успешно")
        time.sleep(3)
        os.system("clear")

    def run_game_extra_pack(self):
        self.install_32_bit_libs()
        # core = Core(self.terminal_session, self.patch)
        # core.work_with_package()


class WpsOffice:
    patch = "other/office/"
    file_patch = None
    terminal_session = None

    def __init__(self, terminal_session):
        self.terminal_session = terminal_session
        pass

    def run_wps_office_extra_pack(self):
        core = Core(self.terminal_session, self.patch)
        core.work_with_command((self.patch + "/command_list.txt"))

class EEPM:
    patch = None
    file_patch = None
    terminal_session = None

    def __init__(self, terminal_session):
        self.terminal_session = terminal_session
        pass

    def run_default_eepm(self):
        try:
            print("Обновление репозиториев.")
            # Выполняем обновление репозиториев через apt-get update
            os.system("apt-get -qq update > /dev/null")

            print("Установка базовых пакетов.")
            # Устанавливаем пакеты для работы eepm
            os.system("apt-get -qq install eepm > /dev/null")
            print("Установка базовых пакетов завершена успешно!")

        except Exception:
            print("Ошибка при установке базовых пакетов! Обратитесь в https://t.me/alt_gnome_chat за помощью.")




