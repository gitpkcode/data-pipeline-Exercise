import pandas as pd
from datetime import datetime as dt

LOCAL_DIR='/tmp/'

def main():
        # Create the dataframe from data.csv
        tweets = pd.read_csv('/home/pkumar/airflow/dags/data/data.csv', encoding='latin1')

        # Fomat time using pd.to_datetime and drop the column Row ID
        tweets = tweets.assign(Time=pd.to_datetime(tweets.Time)).drop('row ID', axis='columns')

        # Export the dataframe into a new csv file with the current date
        tweets.to_csv(LOCAL_DIR + 'data_fetched.csv', index=False)

if __name__ == '__main___':
        main()