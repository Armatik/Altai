#!/bin/sh
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
echo "Запуск Алтая! Введите пароль от root:"
su - -c "cd $SCRIPTPATH/src && python3 main.py"
cd $scriptdir/src && python3 main.py
exit 0

