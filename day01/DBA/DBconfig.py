class DBconfig:

    USERNAME = 'root'
    PASSWORD = 'hzj522zy.'
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'Flask_test'
    DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
