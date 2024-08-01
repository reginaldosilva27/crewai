import requests
from datetime import datetime
from statistics import mean
from tabulate import tabulate

# Databricks API details
HOST = 'adb-3234279603552420.0.azuredatabricks.net'
TOKEN = 'dapi376c2d05c0e32672b3bdee3660416e74-3'
HEADERS = {'Authorization': f'Bearer {TOKEN}'}

def fetch_jobs():
    url = f'https://{HOST}/api/2.1/jobs/list?expand_tasks=true'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('jobs', [])

def fetch_job_runs(job_id):
    url = f'https://{HOST}/api/2.1/jobs/runs/list?job_id={job_id}&limit=10'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('runs', [])

def process_job_data(jobs):
    job_data = []
    for job in jobs:
        job_id = job['job_id']
        job_name = job['settings']['name']
        tasks_quantity = len(job['settings']['tasks'])
        tags = job['settings'].get('tags', {})
        
        runs = fetch_job_runs(job_id)
        if runs:
            last_run = max(runs, key=lambda x: x['start_time'])
            last_run_time = datetime.fromtimestamp(last_run['start_time'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
            last_status = last_run.get('state', {}).get('result_state', 'N/A')
        else:
            last_run_time = 'N/A'
            last_status = 'N/A'
        
        job_data.append([
            job_name, tasks_quantity, last_run_time, last_status, tags, last_run_time, last_status
        ])
    return job_data

jobs = fetch_jobs()
job_data = process_job_data(jobs)
table = tabulate(
    job_data, 
    headers=[
        'JobName', 'TasksQuantity', 'LastRun', 'LastStatus', 'Tags', 'LastRunTime', 'LastStatus'
    ], 
    tablefmt='grid'
)

print(table)