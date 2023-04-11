import pandas as pd
import requests

def read_csv_to_df(path):
    df = pd.read_csv(path, header=None)
    return df

def load_job():
    api_url = "http://127.0.0.1:9000/jobs"
    df = read_csv_to_df('data/job.csv')

    for index, row in df.iterrows():
        job_json = {"job": row[1]}
        print(job_json)
        response = requests.post(api_url, json=job_json)
        print(response.json())


def load_departments():
    api_url = "http://127.0.0.1:9000/departments"
    df = read_csv_to_df('data/departments.csv')

    for index, row in df.iterrows():
        job_json = {"department": row[1]}
        print(job_json)
        response = requests.post(api_url, json=job_json)
        print(response.json())


def load_hired_employees():
    api_url = "http://127.0.0.1:9000/hired_employees"
    df = read_csv_to_df('data/hired_employees.csv')

    for index, row in df.iterrows():
        job_json = {"name": row[1], "datetime": row[2], "department_id": row[3], "job_id": row[4]}
        print(job_json)
        response = requests.post(api_url, json=job_json)
        print(response.json())



load_job()
load_departments()
load_hired_employees()

        


    


#print(df.to_string()) 