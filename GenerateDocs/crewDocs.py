import os
from tokens import get_openai_api_key, get_serper_api_key, get_claude_api_key
from tools import call_claude_api
from crewai import Agent, Task, Crew, Process
from crewai_tools import YoutubeVideoSearchTool, SerperDevTool

os.environ["OPENAI_API_KEY"] = get_openai_api_key()
os.environ["SERPER_API_KEY"] = get_serper_api_key()
os.environ["CLAUDE_KEY"] = get_claude_api_key()

# Tools
youtube_tool = YoutubeVideoSearchTool()
serper_dev = SerperDevTool()
claude_tool = call_claude_api

documentation_specialist  = Agent(
    role='Especialista em documentação',
    goal='Criar uma documentação profissional utilizando tópicos e bullet points, adicionar bastante detalhes e um resumo final como conclusão.',
    backstory="Especialista em documentação com grande experiencia, dominio em Markdown avançado e escritor de livros sobre o tema.",
    memory=False,
    verbose=True,
    model='gpt-4o-mini',
    allow_delegation = False
)

ai_internet_researcher = Agent(
    role='Pesquisador de conteudos na internet',
    goal='Encontrar conteúdos na internet sobre o tema abordado para complementarmos a documentação',
    backstory="Pesquisador senior com vasta experiencia em buscas avançadas de conteudo na internet.",
    memory=False,
    verbose=True,
    max_iter=10,
    allow_delegation = False,
    model='gpt-4o-mini',
    tools=[serper_dev]
)

doc_reviewer  = Agent(
    role='Revisor de documentos',
    goal='Revisar a documentação gerada pelos Agentes e gerar um documento unico em Markdown',
    backstory="Especialista em revisão de documentos e livros, dominio em Markdown e como deixar um visual mais agradavel",
    memory=False,
    verbose=True,
    max_iter=10,
    model='gpt-4o-mini',
    allow_delegation = False
)

databricks_specialist  = Agent(
    role='Especialista em Databricks',
    goal='Validar a documentação gerada pelo agente doc_reviewer se esta de facil entendimento e se pode haver algum erro tecnico, se possivel complementar tecnicamente',
    backstory="Especialista em Databricks com bastante experiencia em todos os tipos de cluster, tambem é muito bom em documentação e Markdown",
    memory=False,
    verbose=True,
    max_iter=10,
    allow_delegation = False,
    model='gpt-4o-mini'
    #tools=[claude_tool]
)

task_documentation = Task(
    description="Documentar a transcrição a seguir: {transcript}",
    expected_output="Uma documentação em Markdown bem detalhada.",
    agent=documentation_specialist,
    async_execution=False
)

task_internet_researcher = Task(
    description="Encontrar conteudos sobre o tema abordado na transcrição",
    expected_output="Extração do conteudo das pesquisas que tenham relação com o resultado, gerar formato de Bullet Points resumidos e unificar as documentações gerando um markdown",
    agent=ai_internet_researcher,
    async_execution=False
)

task_reviewer = Task(
    description="Revisar a documentação gerada anteriormente e propor melhorias",
    expected_output="Juntar as documentações geradas e gerar um Markdown revisado e melhorado, adicionar as referencias utilizadas no final",
    agent=doc_reviewer,
    async_execution=False
)

databricks_reviewer = Task(
    description="Revisar a documentação no nivel técnico",
    expected_output="Documentação em Markdown revisada e melhorada tecnicamente, complementar informações tecnicas se for necessário, ajustar termos e jargões para o publico tecnico",
    agent=databricks_specialist,
    async_execution=False
)

crew = Crew(
    agents=[documentation_specialist,doc_reviewer,ai_internet_researcher,databricks_specialist],
    tasks=[task_documentation,task_reviewer, task_internet_researcher, databricks_reviewer],
    process=Process.sequential,
    verbose=True
)

print("## Iniciando Crew")
print('-------------------------------')
transcript = open("transcript.txt", "r").read()
result = crew.kickoff(inputs={'transcript': transcript})
print("#################")
print("#####  Resultado final: ########")
print(result)
