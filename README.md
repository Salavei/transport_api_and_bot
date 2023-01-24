<h1 align="center"> Hi there, I'm <a href="http://linkedin.com/in/andrewsalavei/" target="_blank">Andrew Salavei</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" width="40" height="40"/></h1>
<h3 align="center">Моя дипломная работа для TeachMeSkill.</h3>



## Технологии <img src="https://user-images.githubusercontent.com/15955132/214321830-f3ccbde2-954e-4751-bdd3-c75ac96a8a0d.png" width="20" height="20">  
  

![icons8-python-48](https://user-images.githubusercontent.com/15955132/214317185-5e615db0-3bfd-4b32-8622-7bb0ea674c05.png)&nbsp;
![icons8-django-48](https://user-images.githubusercontent.com/15955132/214319364-ae374fbf-3081-4381-bd4a-c3f39540d1d9.png)&nbsp;
<img src="https://user-images.githubusercontent.com/15955132/214318930-b6ccf95f-7704-4a54-962b-0f0c93d10245.png" width="50" height="50">&nbsp;
![icons8-docker-48](https://user-images.githubusercontent.com/15955132/214317222-a7e07749-425f-42f3-b0a6-4478d7ab68ec.png)&nbsp;
<img src="https://user-images.githubusercontent.com/15955132/214320602-1511e829-c307-4cc8-8425-b5b4b9b0fbf9.png" width="100" height="50">&nbsp;  
```Python  DRF  Aiogram   Docker   Bs4   ```  
 
## Структура
Состоит из нескольких частей.  

### Телеграм бот
Телеграм бот с базой данных, которую можно администрировать через админ-панель Django.  
У пользователя может быть по 2 сохранненых транспорта и 2 остановки.  
Телеграм бот показывает актуальную информацию о прибытии транспорта и всех остановках транспорта.  
Информация парсится со сторонних источников.  

### Api
Имеется Api, через который можно получить эту же информацию о транспорте:  
``` https://your_host/api/v1/infotrans ```    
``` https://your_host/api/v1/infostation ```   

### Домашняя страница
Развлекательная домашняя страница про `штанах за 40гривень`.  
На этой странице вы сможете узнать актуальную информацию о курсе 40гривень в `BYN, RUB, USDм.  
Так же, подсчет средней зарплаты граждан этих стран и сколько они могу купить себе штанов по курсу 40 гривень. 
  
## Запуск

⋅*Создать файл `.env`  
⋅*Заполнить его:  
```ts
TOKEN=YOUR_TOKEN   
SECRET_KEY=YOURK_SECRET_KEY  
DEBUG=1_OR_0  
DB_NAME=YOUR_DB_NAME   
DB_USER=YOUR_DB_USER  
DB_PASS=YOUR_DB_PASS
```   
⋅*Запустить билд `docker-compose build`   
⋅*Запустить проект `docker-compose  --env-file .env  up`   
⋅*Сделать миграции `docker-compose run --rm web-app sh -c "python manage.py migrate"`  
⋅*Создать суперюзера `docker-compose run --rm web-app sh -c "python manage.py createsuperuser"`  

## Внешний вид
<p align="center"><img width="500" alt="api_1" src="https://user-images.githubusercontent.com/15955132/214305166-bec02484-36c4-419c-9a4f-e8d98ae7a7f9.png"><img width="500" alt="api_2" src="https://user-images.githubusercontent.com/15955132/214305265-60371812-1ab3-45a3-b48f-525d2ec8a584.png"></p>

 <p align="center"><img width="450" alt="Снимок экрана 2023-01-24 в 16 42 18" src="https://user-images.githubusercontent.com/15955132/214310223-0f000d57-f190-49ec-bbfc-c881e9f6eb65.png"><img width="450" alt="Снимок экрана 2023-01-24 в 16 41 45" src="https://user-images.githubusercontent.com/15955132/214310267-11bb898a-47fa-4b46-acfd-fe550dba078f.png"></p>
