# Django Girls python tutorial

## installation

1. environment
rename `env.example` to `.env`and replace the SECRET in the line with the secret you can generate this way:
- open the python console in your terminal/command line  by typing `python` or `python3` depending on your system.
- paste in the following code
```python
from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())
```

- copy the result into the `SECRET` value between quotes.

2. create virtual enviornment

type in the following commands:
- create the virtual enviroment: `python -m venv env`
- on windows cmd `env\Scripts\activate.bat, powershell `env/Scripts/activate.ps1`. on linux and mac:  `source ./env/bin/activate`.

3. install dependancies
`pip install -r requirements.txt` if on windows. on linux and mac use `pip3`. if pip not found error.

4.Django initial configurations 
- change `settings.py`:
 - ```ALLOWED_HOSTS = []``` add your domain name between the square brackets [] as a quoted string.
 -  change the language and time zones to your own.
- run migrations
`python manage.py migrate`
- create a super user for admin login
`python manage.py createsuperuser`
then answer all the questions.

5. run the develepment server `python manage.py runserver`. it will run on localhodt port 8000 by default.
if the is a pid error because subprocesses are not supported, use the `--noreload` command. Note: if you do that you will have to cut and start the server again each time a file is changed.
