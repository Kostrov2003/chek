# Описаниее
Программа для docker, которая выводит все числа от начального, до конечного числа 
!!!(Важно понимать, что docker должен быть у вас установлен)!!!!!

---------------------

# Подготовка к установке docker
Открываем косноль и по очереди прописываем команды

* Для начала, обновим состав установочных пакетов, чтобы иметь представление об их актуальных версиях:
`sudo apt update`



## Создаем контейнер (Ubuntu)
$ sudo docker build -t test .

---------------------

## Запускаем контейнер (Ubuntu)
$ sudo docker run --rm test

