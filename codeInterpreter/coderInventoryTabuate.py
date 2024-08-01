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
    model='gpt-4o-mini',
    allow_delegation = False,
    tools=[CodeInterpreterTool()]
)

# Define tasks for researcher
task_inventory= Task(
    description="Job Inventory",
    expected_output="""Criar um inventario de Jobs do Databricks no formato tabular retornar uma tabela bem formata com a biblioteca Tabulate, imprimir o resultado na tela.
    Para cada Job devera retornar as seguintes informações:
    -JobName: Nome do Job - Origem /api/2.1/jobs/list
    -TasksQuantity: Quantidade de tasks que o job possui - Origem /api/2.1/jobs/get aplicar LEN(len(job['settings']['tasks']) utilize o parametro expand_tasks para pegar as tasks
    -LastRun: A data e hora da ultima execucao, transformar no formato yyyy-MM-dd HH:mm:ss, default N/A - Origem api/2.1/jobs/runs/list
    -LastStatus: Status da última execucao do Job, default N/A - Origem api/2.1/jobs/runs/list - state.result_state 
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
result = crew.kickoff(inputs={'HOST': 'adb-3234279603552420.0.azuredatabricks.net', 'TOKEN': 'dapi376c2d05c0e32672b3bdee3660416e74-3'})
print(result)


