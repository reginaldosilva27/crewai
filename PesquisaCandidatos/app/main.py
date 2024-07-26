import os
from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

app = FastAPI()

# Carregar as chaves da API
os.environ["OPENAI_API_KEY"] = 'xx'
os.environ["SERPER_API_KEY"] = 'xx'
os.environ["CLAUDE_KEY"] = 'xx'


# Definir o modelo de entrada
class JobRequirements(BaseModel):
    job_requirements: str

# Criar o agente pesquisador
search_tool = SerperDevTool()
researcher = Agent(
    role='Recrutador Senior de Dados',
    goal='Encontrar os melhores perfis de dados para trabalhar baseados nos requisitos da vaga',
    verbose=True,
    memory=True,
    model='gpt-4o-mini',
    backstory=(
        "Experiencia na area de dados e formação academica em Recursos Humanos e "
        "Especilista em Linkedin, tem dominio das principais taticas de busca de profissionais"
    ),
    tools=[search_tool]
)

# Definir a rota para executar a tarefa
@app.post("/research_candidates")
async def research_candidates(req: JobRequirements):
    # Criar a tarefa de pesquisa
    research_task = Task(
        description=(
            f"Realizar pesquisas completas para encontrar candidatos em potencial para o cargo especificado "
            f"Utilize vários recursos e bancos de dados online para reunir uma lista abrangente de candidatos em potencial. "
            f"Garanta que o candidato atenda os requisitos da vaga. Requisitos da vaga: {req.job_requirements}"
        ),
        expected_output=""" Uma lista com top 5 candidatos potenciais separada por Bullet points, 
                            cada candidado deve conter informações de contato e breve descrição do perfil destacando a sua qualificação para a vaga 
                            trazer junto a url para encontrar o perfil do candidato""",
        tools=[search_tool],
        agent=researcher,
    )

    # Criar a equipe e executar a tarefa
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        process=Process.sequential
    )

    result = crew.kickoff(inputs={'job_requirements': req.job_requirements})
    return {"result": result}

# Rodar o servidor usando Uvicorn
if __name__ == "__main__":
    import uvicorn
    print(">>>>>>>>>>>> version V0.0.1")
    uvicorn.run(app, host="0.0.0.0", port=8000)
