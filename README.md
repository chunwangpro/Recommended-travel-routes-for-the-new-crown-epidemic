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

如果未安装`pymysql`：


```
pip install pymysql
```

用`Terminal`打开到`duma/`路径下，并执行以下语句：


```
python manage.py makemigrations ncov
python manage.py migrate
```

如果第一次运行：

- 请先删除`duma/ncov/migrations/`下的文件

- 进入本地`mysql`数据库，并执行：

```
source duma/ncov/sql/insert-data.sql
```

- 或直接粘贴`duma/ncov/sql/insert-data.sql`中的语句

在`Terminal`中继续执行：

```
python manage.py runserver
```

浏览器打开网址`http://127.0.0.1:8000/ncov/`





