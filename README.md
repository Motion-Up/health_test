# Проект Health Test
Тестирование ментального и физического состояния своего здоровья.
В этом проекте Вы сможете сами составить тесты, и ответы.
Вы можете посмотреть веб-приложение перейдя по ссылке http://viewoutside.ru

### Установка:
Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Motion-Up/health_test.git
```
```
cd health_test
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

