from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from Common import OpenFile
from Common import UploadRedis

def pull_function(**kwargs):
    ti = kwargs['ti']
    File = ti.xcom_pull(task_ids='TaskOpenFile')
    UploadRedis.SendToReddis(File)

with DAG('TaskBatimento', description='Python DAG', schedule_interval='*/5 * * * *', start_date=datetime(2020, 4, 28),
         catchup=False) as dag:
    TaskOpenFile = PythonOperator(task_id='TaskOpenFile', python_callable=OpenFile, op_kwargs={'FileDir':r'/usr/local/airflow/dags/file/002643.BATIMENTO.ZANC.txt'})
    TaskUploadRedis = PythonOperator(task_id='TaskUploadRedis', python_callable=pull_function,provide_context=True)

    TaskOpenFile >> TaskUploadRedis