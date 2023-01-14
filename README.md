# transport_timewait_bot_telegram
Моя дипломная работа для TeachMeSkill. 
http://40uah.duckdns.org  
http://40uah.duckdns.org/api/infostation/ 
http://40uah.duckdns.org/api/infotrans/  
http://40uah.duckdns.org/car/  
https://t.me/transport_minskBot  
Технологии:   
Django, DRF, Bs4, Aiogram, Docker.  
Состоит из нескольких частей.  
1)Самое главное, это телеграм бот, который показываем время ожидание транспорта и остановки транспорта.  
Узнать информацию о транспорте также можно и через API DRF.  
2)Хоум пэйдж о штанах за 40гривень, на котором выводится информация и курсе 40гривень в BYN, RUB, USD, а так же, подсчет   
средней зарплаты граждан этих стран и сколько они могу купить себе штанов по курсу 40 гривень  
  
  
Заполнить вашими данными environment в docker-compose  
   
Запустить билд docker-compose build
Запустить проект docker-compose up
Сделать миграции docker-compose run --rm web-app sh -c "python manage.py migrate"
Создать суперюзера docker-compose run --rm web-app sh -c "python manage.py createsuperuser"


<img width="1635" alt="Снимок экрана 2022-04-09 в 22 37 30" src="https://user-images.githubusercontent.com/15955132/162589172-da374af1-2585-4c5c-b92f-47708db398fa.png">
