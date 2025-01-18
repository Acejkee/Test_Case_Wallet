## Тестовое задание

## Установка

### Клонирование репозитория

Сначала клонируйте репозиторий на ваш локальный компьютер:

```bash
git clone https://github.com/Acejkee/Test_Case_Wallet.git
```
и перейдите в каталог с проектом.

```bash
cd Test_Case_Wallet
```

### Настройка файла .env

В корневом каталоге проекта вы найдете файл .env.example. переименуйте в .env
Откройте файл .env в текстовом редакторе и если Вам необходимо,
измените переменные окружения, такие как секретный ключ, данные для подключения к базе данных 
и другие параметры, которые могут быть необходимы для вашего проекта.



### Запуск с помощью Docker Compose

Запустите проект с помощью Docker Compose, используя следующую команду:

```bash
docker compose up -d --build
```

Эта команда создаст и запустит контейнеры в фоновом режиме, а также пересоберет их при необходимости.

### Выполнение миграций и создание суперпользователя

После запуска контейнеров выполните команду для доступа к консоли контейнера:

```bash
docker compose exec web bash
```

Теперь внутри контейнера выполните следующие команды:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Следуйте инструкциям на экране для создания суперпользователя.

## Остановка контейнеров

Чтобы остановить и удалить контейнеры, используйте команду:

```bash
docker compose down
```

## Дополнительная информация

Чтобы запустить тесты, выполните команду

```bash
poetry run python manage.py test
```