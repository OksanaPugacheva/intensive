## Сервис для просмотра меню

### Запуск сервиса
* Скачайте проект 
* На вашем компьютере должны быть установлены:
  * python (https://www.python.org/)
  * poetry (https://python-poetry.org/)
  * postgresql (https://www.postgresql)
* В файле database.py измените значения полей DATABASE_LOGIN, DATABASE_PASSWORD
на ваши логин и пароль от postgresql, значение поля DATABASE_NAME на имя базы данных
* В папке с проектом запустите последовательно команды:
  * poetry install
  * poetry run start
* Сервис запущен на 8000 порту. При необходимости порт можно изменить в функции start_uvicorn() находящейся в main.
