# Описаниее
Программа для docker, которая выводит все числа от начального, до конечного числа 
`!!!(Важно понимать, что docker должен быть у вас установлен)!!!!!`

---------------------

# Подготовка к установке docker
Открываем косноль и по очереди прописываем команды

* Для начала, обновим состав установочных пакетов, чтобы иметь представление об их актуальных версиях:
`sudo apt update`
* Предварительно установим набор пакетов, необходимый для доступа к репозиториям по протоколу HTTPS:
`sudo apt install apt-transport-https ca-certificates curl software-properties-common` 
* Далее добавим в систему GPG-ключ для работы с официальным репозиторием Docker:
`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
* Теперь добавим репозиторий Docker в локальный список репозиториев:
`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
* Повторно обновим данные о пакетах операционной системы:
`sudo apt update`
* Приступим к установке Docker
`sudo apt install docker-ce -y`
* Поверим:
`sudo docker version`
![](/home/yaroslav/Pictures/Screenshots/docker.png)

должны увидеть что то подобное




## Создаем контейнер (Ubuntu)
$ sudo docker build -t test .

---------------------

## Запускаем контейнер (Ubuntu)
$ sudo docker run --rm test

