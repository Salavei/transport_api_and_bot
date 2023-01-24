<h1 align="center"> Hi there, I'm <a href="http://linkedin.com/in/andrewsalavei/" target="_blank">Andrew Salavei</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" width="40" height="40"/></h1>
<h3 align="center">My thesis for TeachMeSkill.</h3>



## Technology <img src="https://user-images.githubusercontent.com/15955132/214321830-f3ccbde2-954e-4751-bdd3-c75ac96a8a0d.png" width="20" height="20">  
  

![icons8-python-48](https://user-images.githubusercontent.com/15955132/214317185-5e615db0-3bfd-4b32-8622-7bb0ea674c05.png)&nbsp;
![icons8-django-48](https://user-images.githubusercontent.com/15955132/214319364-ae374fbf-3081-4381-bd4a-c3f39540d1d9.png)&nbsp;
<img src="https://user-images.githubusercontent.com/15955132/214318930-b6ccf95f-7704-4a54-962b-0f0c93d10245.png" width="50" height="50">&nbsp;
![icons8-docker-48](https://user-images.githubusercontent.com/15955132/214317222-a7e07749-425f-42f3-b0a6-4478d7ab68ec.png)&nbsp;
<img src="https://user-images.githubusercontent.com/15955132/214320602-1511e829-c307-4cc8-8425-b5b4b9b0fbf9.png" width="100" height="50">&nbsp;  
```Python  DRF  Aiogram   Docker   Bs4   ```  
 
## Structure
Consists of several parts.  

### Telegram bot
Telegram bot with a database which can be administered through the Django admin panel.  
The user can have 2 saved transports and 2 stops.  
Telegram bot shows actual information about transport arrivals and all transport stops.  
The information is parsed from third-party sources.   

### Api
There is an Api, through which you can get the same information about the transport:  
`` https://your_host/api/v1/infotrans ``    
`` https://your_host/api/v1/infostation ``    

### Home Page
Entertaining home page about ``pants for 40 UAH``.  
On this page you can find up-to-date information about the rate of ` 40 UAH in ` BYN, RUB, USDm.  
Also, calculation of the average salary of citizens of these countries and how much they can buy themselves pants at the rate of 40 UAH. 
  
## Запуск

⋅*Create file `.env`  
⋅*Fill it:  
```ts
TOKEN=YOUR_TOKEN   
SECRET_KEY=YOURK_SECRET_KEY  
DEBUG=1_OR_0  
DB_NAME=YOUR_DB_NAME   
DB_USER=YOUR_DB_USER  
DB_PASS=YOUR_DB_PASS
```   
⋅*Run the `docker-compose build`   
⋅*Start project `docker-compose --env-file .env up`   
⋅*Migration `docker-compose run --rm web-app sh -c "python manage.py migrate"`  
⋅*Create superuser `docker-compose run --rm web-app sh -c "python manage.py createsuperuser"`  

## Appearance

