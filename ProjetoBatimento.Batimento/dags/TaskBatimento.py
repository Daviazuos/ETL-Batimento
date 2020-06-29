from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from Common import *
from Task import *

def pull_function(**kwargs):
    ti = kwargs['ti']
    File = ti.xcom_pull(task_ids='TaskOpenFile')
    UploadRedis.SendToReddis(File)

with DAG('PortocredBatimento', description='Python DAG', start_date=datetime(2020, 4, 28),
         catchup=False) as dag:
    
    TaskStartApi = PythonOperator(task_id='TaskStartApi', python_callable=StartApi,provide_context=True)
    TaskOpenFile = PythonOperator(task_id='TaskOpenFile', python_callable=OpenFile, op_kwargs={'FileDir':r'/usr/local/airflow/dags/file/002643.BATIMENTO.ZANC.txt'})
    TaskUploadRedis = PythonOperator(task_id='TaskUploadRedis', python_callable=pull_function,provide_context=True)
    TaskQueryMcob = PythonOperator(task_id='TaskQueryMcob', python_callable=QueryMcob,provide_context=True)
    TaskSendToKnock = PythonOperator(task_id='TaskSendToKnock', python_callable=SendToKnock,provide_context=True)
    TaskKnock = PythonOperator(task_id='TaskKnock', python_callable=BatimentoPortocred,provide_context=True)
    TaskAdjustToFile = PythonOperator(task_id='TaskAdjustToFile', python_callable=AdjustToFile,provide_context=True)
    TaskSaveToFile = PythonOperator(task_id='TaskSaveToFile', python_callable=SaveToFile,provide_context=True)

    TaskStartApi.set_downstream(TaskOpenFile)
    TaskStartApi.set_downstream(TaskQueryMcob)

    TaskOpenFile.set_downstream(TaskUploadRedis)
    TaskQueryMcob.set_downstream(TaskSendToKnock)

    TaskUploadRedis.set_downstream(TaskKnock)
    TaskSendToKnock.set_downstream(TaskKnock)

    TaskKnock.set_downstream(TaskAdjustToFile)
    TaskAdjustToFile.set_downstream(TaskSaveToFile)