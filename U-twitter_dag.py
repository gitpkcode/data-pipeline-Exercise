from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import logging

import fetching_tweets
import cleaning_tweets
dag = DAG(
        dag_id = "twitter_dag",
        start_date = datetime(2020,1,1),
        schedule_interval = "@daily"
        )

waiting_for_tweets = FileSensor(
        task_id = "waiting_for_tweets",
        fs_conn_id = "fs_tweets",
        filepath = "data.csv",
        poke_interval = 5,
        dag = dag
        )

fetching_tweets_task = PythonOperator(
    task_id="fetching_tweets",
    python_callable=fetching_tweets.main,
    dag=dag
        )

cleaning_tweets_task = PythonOperator(
        task_id = "cleaning_tweets",
        python_callable = cleaning_tweets.main,
        dag = dag
        )