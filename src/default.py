import os

import time


def progress_bar(percent, clear=True):
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


def AMD_P_State():
    try:
        # Проверка версии ядра, выше 6.4.10 поддерживается.
        progress_bar(percent=0)
        print("Проверьте версию ядра командой : uname -r")
        print("Если версия ядра ниже 6.4.10, то обновите ядро используя: epm full-upgrade и повторите установку AMD P-State.")
        print("Версия ядра выше 6.4.10? (да/нет)")
        answer = input()
        progress_bar(percent=10, clear=False)
        if answer == "да":
            # Установка power-profiles-daemon
            os.system("apt-get -qq install power-profiles-daemon > /dev/null")
            # Получение всех строк из файла /etc/sysconfig/grub2
            grub2 = open("/etc/sysconfig/grub2", "r")
            grub2_lines = grub2.readlines()
            grub2.close()
            progress_bar(percent=25)
            flag = True

            # Ищмем строку GRUB_CMDLINE_LINUX_DEFAULT
            for line in grub2_lines:
                if "GRUB_CMDLINE_LINUX_DEFAULT" in line:
                    progress_bar(percent=60)
                    # Удаляем с конца строки символ -"'"
                    line = line[:-1]
                    # Проверяем есть ли в конце строки параметр " amd_pstate=active'"
                    if "amd_pstate=active'" in line or "amd_pstate=guided" in line or "amd_pstate=passive" in line:
                        print("AMD P-State уже установлен!")
                        time.sleep(5)
                        flag = False

                    else:
                        # Добавляем в конец строки параметр " amd_pstate=active'"
                        line += " initcall_blacklist=acpi_cpufreq_init amd_pstate=active'"
                        # Записываем изменения в файл
                        grub2 = open("/etc/sysconfig/grub2", "w")
                        grub2.writelines(grub2_lines)
                        grub2.close()
                    progress_bar(percent=65)
                    break

            if flag:
                progress_bar(percent=70)
                # Обновляем grub
                os.system("grub2-mkconfig -o /boot/grub2/grub.cfg > /dev/null")
                progress_bar(percent=100)
                print("Установка AMD P-State завершена успешно!")
            else:
                print("Установка AMD P-State не произведена!")
        else:
            print("Версия ядра не поддерживается! Обновите ядро до версии 6.4.10 и выше используя: epm full-upgrade")
            print("После обновления ядра повторите установку AMD P-State, Программа продолжит работу через 10 секунд.")
            time.sleep(10)
    except:
        print("Ошибка при установке AMD P-State! Обратитесь в https://t.me/alt_gnome_chat за помощью.")


def package_update():
    try:
        progress_bar(percent=0)
        # Выполняем обновление репозиториев через apt-get update
        os.system("apt-get -qq update > /dev/null")
        progress_bar(percent=50)
        # Выполняем обновление системы через apt-get dist-upgrade
        os.system("apt-get -qq dist-upgrade > /dev/null")
        progress_bar(percent=100)
        print("Обновление системы завершено успешно!")
    except:
        print("Ошибка при обновлении системы! Обратитесь в https://t.me/alt_gnome_chat за помощью.")






