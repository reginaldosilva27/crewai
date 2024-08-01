import os
from tokens import get_openai_api_key, get_serper_api_key, get_claude_api_key
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, CodeInterpreterTool
os.environ["OPENAI_API_KEY"] = get_openai_api_key()
os.environ["SERPER_API_KEY"] = get_serper_api_key()
os.environ["CLAUDE_KEY"] = get_claude_api_key()

# Tools
serper_dev = SerperDevTool()

# Define a senior researcher agent
ai_coder = Agent(
    role='Desenvolvedor Python e Especilista Databricks',
    goal='Criar um script python para retornar dados formatados em tabular',
    backstory="Desenvolvedor Senior em Python e Especialista Databricks",
    memory=True,
    verbose=True,
    allow_delegation = False,
    tools=[CodeInterpreterTool()]
)

# Define tasks for researcher
task_inventory= Task(
    description="Job Inventory",
    expected_output="""Criar um inventario de Jobs do Databricks no formato tabular retornar um código HTML com visual legal para abrir em um navegador
    Para cada Job devera retornar as seguintes informações:
    -JobName: Nome do Job - Origem /api/2.1/jobs/list
    -TasksQuantity: Quantidade de tasks que o job possui - Origem /api/2.1/jobs/get aplicar LEN(len(job['settings']['tasks']) utilize o parametro expand_tasks para pegar as tasks
    -LastRun: A data e hora da ultima execucao, transformar no formato yyyy-MM-dd HH:mm:ss, default N/A - Origem api/2.1/jobs/runs/list
    -LastStatus: Status da última execucao do Job, default N/A - Origem api/2.1/jobs/runs/list - state.result_state - Se status for SUCCESS ficar verde no HTML, se for FAILED ficar vermelho no HTML
    -Tags: Tags do Job - Origem /api/2.1/jobs/list
    -AvgDurationMin - Média de duração em minutos - Usar as ultimas 10 execuções - Origem  api/2.1/jobs/runs/list campo run_duration converter para minutos sem casas decimais
    -MaxDurationMin - Maior duração em minutos - Usar as ultimas 10 execuções - Origem  api/2.1/jobs/runs/list campo run_duration converter para minutos sem casas decimais
    -LastDurationMin - A duração da execução mais recente em minutos - Origem  api/2.1/jobs/runs/list campo run_duration converter para minutos sem casas decimais
    -StatusDuration - Caso o LastDurationMin esteja maior do que a media, colocar 'Warning' em cor amarelo no HTML caso contratio 'OK' em cor verde no HTML
    Utilizar para acesso na API o Hos: {HOST} e token: {TOKEN},
    Dica: Para isso sera necessario uma chamada na API de /api/2.1/jobs/list utilize o parametro expand_tasks e com o resultado dela sera necessario uma nova chamada na API de /api/2.1/jobs/get e tabem uma chamada na API api/2.1/jobs/runs/list para cada Job""",
    agent=ai_coder,
    async_execution=False
)

# Form the senior crew with the junior crew as a sub-crew
crew = Crew(
    agents=[ai_coder],
    tasks=[task_inventory],
    process=Process.sequential,
    verbose=1
)

# Kick off the senior crew
result = crew.kickoff(inputs={'HOST': 'adb-3234279603552420.0.azuredatabricks.net', 'TOKEN': 'xxxxxxx'})
print(result)


