import pymysql

# Django-va emaatha intha line mukkiyam
pymysql.version_info = (10, 5, 0, "final", 0) 
pymysql.install_as_MySQLdb()