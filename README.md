# CreativeHub

[Brian Odhiambo](https://github.com/Brian23-eng)  
  
# Description  
The project enables users post art pieces from their hood and other users can comment on the piece and even follow and subscribe to get newsletter about the web app


##  Live Link  
 Click [View Site](https://brantech.herokuapp.com/)  to visit the site
  

## User Story  
  
* A user can view different posts posted by other artists
* A user can post their art pieces
* A user can comment on art pieces and even follow other artists 
* User can see description of a single art  
* A user can subscribe to the newsletter
* A user can create their own profile and log in to the webapp
* A user can view their profile page. 
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
```bash
https://github.com/Brian23-eng/CreativeHub.git
```
##### Navigate into the folder and install requirements  
 ```bash
 cd CreativeHub pip install -r requirements.txt 
 ```
##### Install and activate Virtual  
```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies  
```bash
 pip install -r requirements.txt 
``` 
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations artist
 ``` 
 Now Migrate

```bash
python manage.py migrate 
```
##### Run the application  
```bash
python manage.py runserver 
```
##### Testing the application  
```bash
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [b.odhiambo.bo@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/brian23-eng/Picture-Globe/blob/master/LICENSE)  
* Copyright (c) 2019 **BranTech**