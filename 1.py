import pyodbc
pyodbc.connect("DRIVER=FreeTDS;SERVER=192.168.1.1;PORT=1433;DATABASE=db_name;UID=user_name;PWD=password;TDS_Version=8.0;ClientCharset=UTF8;")