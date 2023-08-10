# DarkBox
### *__DarkBox__* is a catalog of different electronics at an affordable price.
1. Firstly, you need to make an local environment and activate it 
   ```python
   python -m venv venv
   source venv/bin/activate
2. Insall packages
   ```python
   pip install -r requirements.txt
2. Create a ".env" file at the root of the directory with params
   ```python
   DEBUG=True or False
   
   # ALL SETTINGS FOR !POSTGRESQL!
   DB_USER='your postgres user'
   DB_PASS='your password for user'
   DB_NAME='your name of db'
   DB_HOST='127.0.0.1' or 'localhost'
   DB_PORT='5432'
4. After that, make migrations and do migrate to your DB
   ```python
   python manage.py makemigrations
   python manage.py migrate
3. Finally, you can start the project due a command 
    ```
    python manage.py runserver
> As well as, you can start tests
  ```python
  python manage.py test <'name_folder'> ( without (),<> and '' )
