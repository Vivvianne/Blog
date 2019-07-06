export SECRET_KEY= os.environ.get('SECRET_KEY')
export SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://nkimani:her1234@localhost/try'
export MAIL_USERNAME = 'ndiahav@gmail.com'
export MAIL_PASSWORD = 'her1234'

python3.6 manage.py server