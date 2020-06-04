# Instructions
# Define a function that uses the python logger to log a function. 
import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


#
# TODO: Define a function for the PythonOperator to call and have it log something
#
def my_function():
     logging.info('This is my first DAG')


dag = DAG(
        'lesson1.DAG-exercise1',
        start_date=datetime.datetime.now())

#
# TODO: Uncomment the operator below and replace the arguments labeled <REPLACE> below
#

greet_task = PythonOperator(
    task_id="First_Node",
    python_callable=my_function,
    dag=dag
)

