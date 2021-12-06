# **疫情常态化下的旅游出行线路推荐系统**

在`duma/duma/setting.py`中添加自己本地`mysql`账户以及`secret key`：


```
SECRET_KEY = 'your-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '',
        'NAME': 'your-database',
    }
}   
```

如果本地`mysql`数据库中没有数据，请先执行`duma/ncov/sql/insert-data.sql`中的语句

如果未安装`pymysql`：


```
pip install pymysql
```

用`Terminal`打开到`duma/`路径下，并执行以下语句：


```
python manage.py makemigrations ncov
python manage.py migrate
python manage.py runserver
```

浏览器打开网址`http://127.0.0.1:8000/ncov/`





