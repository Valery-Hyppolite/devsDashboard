# from flask import Flask, render_template, request
# import os, psycopg2
# from dotenv import load_dotenv
# from pathlib import Path
# load_dotenv()
# env_path = Path(".")/'.flaskenv'
# load_dotenv(dotenv_path=env_path)


# app = Flask(__name__)
#con = psycopg2.connect("postgresql://discover-devs:valou@localhost:5432/discover-devs")
# def get_db_connection():
#     conn = psycopg2.connect(
#         host='ecommerce-22.c3ysewtjmgae.us-east-1.rds.amazonaws.com',
#         database='ecommerce-22',
#         user='valou',
#         password='Devvalou80k$',
#     )
#     return conn
# def get_db_connection():
#     conn = psycopg2.connect(
#         host = 'discover-dev-2022.c3ysewtjmgae.us-east-1.rds.amazonaws.com',
#         database = 'discover_devs',
#         user = 'valou',
#         password ='Devvalou80k$',
#         port = '5432',
#     )
#     return conn

# conn = psycopg2.connect(
#     host = os.environ.get('AWSRDB_HOST'),
#     database = os.environ.get('AWSRDB_NAME'),
#     user = os.environ.get('AWSRDB_USER'),
#     password = os.environ.get('AWSRDB_PASWD'),
# )

# @app.route('/')
# def home():
    # conn = get_db_connection()
    # cur = conn.cursor()
    # cur.execute('SELECT * FROM project_projects')
    # projects = cur.fetchall()
    # print(projects)
    # cur.close()
    # conn.close()
    
    # return render_template('Dashboard.html')

# if __name__ == '__main__':
#     app.run(debug=True)