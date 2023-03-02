# Описаниее
Программа для docker, которая выводит все числа от начального, до конечного числа (в коде программы указаны числа от 1 до 10, и в обратном порядке от 10 до 1)
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
`Client: Docker Engine - Community
 Version:           23.0.1
 API version:       1.42
 Go version:        go1.19.5
 Git commit:        a5ee5b1
 Built:             Thu Feb  9 19:46:49 2023
 OS/Arch:           linux/amd64
 Context:           default
 Server: Docker Engine - Community
 Engine:
  Version:          23.0.1
  API version:      1.42 (minimum version 1.12)
  Go version:       go1.19.5
  Git commit:       bc3805a
  Built:            Thu Feb  9 19:46:49 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.18
  GitCommit:        2456e983eb9e37e47538f59ea18f2043c9a73640
 runc:
  Version:          1.1.4
  GitCommit:        v1.1.4-0-g5fd4c4d
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0`


Должны увидеть что то подобное

# Теперь скачиваем себе этот репозиторий
Для этого нам понадобится git (как его устанавливать можно посмотреть в интернЕтах)

Открываем терминал в той директории, в которую будем скачивать репозиторий.
или же
можем прейти из общего терминала в нужную нам папку с помощью команды `cd`.
Копируем репозиторий:
`git clone <вставляем ссылку на мой репозиторий ( без < >)>`

## Создаем контейнер (Ubuntu)
`sudo docker build -t test . `

---------------------

## Запускаем контейнер (Ubuntu)
`sudo docker run --rm test`

