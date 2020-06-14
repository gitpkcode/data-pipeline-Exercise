from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from datetime import datetime
import logging
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