# 1: Setup

-> setup pipenv

```
pipenv install --python 3
pipenv install flask flask_restful sqlalchemy pymysql
```

-> Create a database

```
mysql -u username -ppassword

mysql > create database testdb;
mysql > use testdb;
```

-> Copy paste these queries

```sql
create table users (
    id int primary key auto_increment,
    fname varchar(100)
);

create table salary (
    id int primary key auto_increment,
    user_id int,
    amout double(12,2),
    foreign key (user_id) references users(id)
);
```

