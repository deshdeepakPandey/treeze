please follow below Steps

Note -- Please make sure you have python 3.10

git clone https://github.com/deshdeepakPandey/treeze.git

cd .\treeze\

pip install -r .\requirements.txt -->> To install all project Dependency

python .\manage.py runserver --> This command Start your Projects

open url --->>> http://127.0.0.1:8000/transactions/index
Swagger also implemented --->>> http://127.0.0.1:8000/swagger/

Admin panel:
http://127.0.0.1:8000/admin/login/?next=/admin/
user: deshdeepak
pass:DESHec1/


Features:
1. Sqlite3 Db used here and table created.
2. inside admin panal transaction table have import export functionality.
3. Active Functionality:
   a. pagination implemented 15 items per page
   b. Next and previous button are working
   c. search Field is active and with server-side rendering
   d. also can download csv file
