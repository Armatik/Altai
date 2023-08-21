import os


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
    
    
def eepm():
    try:
        print ("Запуск установки eepm")
        progress_bar(percent=0, clear=False)

        # Выполняем обновление репозиториев через apt-get update
        os.system("apt-get update > /dev/null")

        progress_bar(percent=10, clear=True)

        # Устанавливаем пакеты для работы eepm
        os.system("apt-get install eepm > /dev/null")

        progress_bar(percent=100, clear=True)
        print("Установка базовых пакетов завершена успешно!")

    except:
        print("Ошибка при установке базовых пакетов! Обратитесь в https://t.me/alt_gnome_chat за помощью.")



