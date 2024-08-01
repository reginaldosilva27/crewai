import requests
import pandas as pd
from datetime import datetime

# Configurações
host = 'https://adb-3234279603552420.0.azuredatabricks.net'
token = 'dapi376c2d05c0e32672b3bdee3660416e74-3'
headers = {'Authorization': f'Bearer {token}'}

# Função para obter a lista de jobs
def get_jobs():
    url = f'{host}/api/2.1/jobs/list?expand_tasks=true'
    response = requests.get(url, headers=headers)
    return response.json().get('jobs', [])

# Função para obter detalhes de um job
def get_job_details(job_id):
    url = f'{host}/api/2.1/jobs/get?job_id={job_id}'
    response = requests.get(url, headers=headers)
    return response.json()

# Função para obter as execuções de um job
def get_job_runs(job_id):
    url = f'{host}/api/2.1/jobs/runs/list?job_id={job_id}'
    response = requests.get(url, headers=headers)
    return response.json().get('runs', [])

# Função para calcular métricas de execuções
def calculate_run_metrics(runs):
    durations = [run['run_duration'] // 60000 for run in runs[:10]]  # Converter ms para minutos e pegar as últimas 10 execuções
    avg_duration = sum(durations) // len(durations) if durations else 0
    max_duration = max(durations) if durations else 0
    last_duration = durations[0] if durations else 0
    return avg_duration, max_duration, last_duration

# Função para processar os jobs e gerar dados tabulares
def process_jobs():
    jobs = get_jobs()
    data = []
    for job in jobs:
        job_id = job['job_id']
        job_name = job['settings']['name']
        tasks_quantity = len(job['settings']['tasks'])
        tags = job['settings'].get('tags', [])
        
        job_runs = get_job_runs(job_id)
        last_run = job_runs[0] if job_runs else None
        last_run_time = datetime.fromtimestamp(last_run['start_time'] // 1000).strftime('%Y-%m-%d %H:%M:%S') if last_run else 'N/A'
        last_status = last_run['state'].get('result_state', 'N/A') if last_run else 'N/A'
        
        avg_duration, max_duration, last_duration = calculate_run_metrics(job_runs)
        status_duration = 'Warning' if last_duration > avg_duration else 'OK'
        
        data.append({
            'JobName': job_name,
            'TasksQuantity': tasks_quantity,
            'LastRun': last_run_time,
            'LastStatus': last_status,
            'Tags': ', '.join(tags),
            'AvgDurationMin': avg_duration,
            'MaxDurationMin': max_duration,
            'LastDurationMin': last_duration,
            'StatusDuration': status_duration
        })
    return pd.DataFrame(data)

# Gerar a tabela HTML
df = process_jobs()
html_table = df.to_html(index=False, classes='table table-striped')

# Adicionar formatação de cores
html_table = html_table.replace('Warning', '<span style="color: yellow;">Warning</span>')
html_table = html_table.replace('OK', '<span style="color: green;">OK</span>')
html_table = html_table.replace('SUCCESS', '<span style="color: green;">SUCCESS</span>')
html_table = html_table.replace('FAILED', '<span style="color: red;">FAILED</span>')

html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <title>Databricks Job Inventory</title>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Databricks Job Inventory</h1>
        {html_table}
    </div>
</body>
</html>
'''

print(html_content)