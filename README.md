## Сервис для просмотра меню

### Запуск приложения и тестов CRUD
* Скачайте проект
* На вашем компьютере должны быть установлены:
  * docker (https://www.docker.com/)
* В папке с проектом в командной строке запустите команду:
  * docker-compose up -d
* Сервис запущен по адресу 127.0.0.1:8000
* Для запуска тестов введите:
  * docker-compose run tests pytest -v
