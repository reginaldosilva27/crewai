# Documentação: Databricks 0 a 100 - Clusters Configs - Parte 1 - Desmistificando Nomenclaturas

## Introdução

Bem-vindo a mais um vídeo da série "Databricks 0 a 100". Neste vídeo, abordaremos a configuração de clusters no Databricks. O vídeo foi dividido em várias partes para facilitar a compreensão dos tópicos, devido à sua complexidade e à quantidade de detalhes a serem discutidos.

## Tópicos Abordados

### 1. Tipos de Clusters
- **Cluster All Purpose**: Utilizado para desenvolvimento, depuração e exploração de dados.
- **Job Cluster**: Criado para a execução de jobs específicos e destruído após a conclusão do job.
- **SQL Compute Cluster**: Focado para consultas em data warehouses, anteriormente conhecido como "Endpoint".
- **Delta Live Tables Cluster**: Utilizado em pipelines de Delta Live Tables, com uma interface de criação diferente.

### 2. Modos de Operação dos Clusters
- **Single Node**: Ideal para testes rápidos e depuração devido ao seu baixo custo.
- **Multi Node**: Inclui um driver e múltiplos workers, adequado para produção e processamento distribuído.
- **High Concurrency**: Otimizado para múltiplos usuários, atualmente substituído por "Shared".

### 3. Access Mode
- **Single User**: Exclusivo para um único usuário.
- **Shared**: Pode ser compartilhado entre múltiplos usuários, suportando apenas Python e SQL.
- **No Isolation**: Sem isolamento, permitindo acesso total aos dados.
- **Custom**: Mantém configurações legadas.

### 4. Políticas de Clusters (Policies)
- **No Restriction**: Permite qualquer configuração.
- **Personal Compute**: Configurações básicas para uso pessoal.
- **Power User Compute**: Para usuários avançados, com algumas restrições.
- **Shared Compute**: Otimizado para compartilhamento e uso de Unity Catalog.

### 5. Depara de Nomenclaturas
- **Standard Cluster**: Agora chamado de "No Isolation".
- **High Concurrency Cluster**: Agora chamado de "Shared".
- **Clusters com Passthrough**: Classificados como "Single User" ou "Shared" com passthrough.

### 6. Configurações Práticas
- **Interface Nova vs. Interface Antiga**: Diferenças na criação e configuração de clusters.
- **Comparação de JSONs**: Ferramenta para visualizar diferenças entre policies.

## Detalhamento das Configurações

### Interface de Criação de Clusters

#### Interface Nova
- **Policies Disponíveis**:
  - No Restriction
  - Personal Compute
  - Power User Compute
  - Shared Compute
- **Access Mode**:
  - Single User
  - Shared
  - No Isolation

#### Interface Antiga
- **Cluster Modes**:
  - Standard
  - High Concurrency
  - Single Node
- **Access Mode não disponível** na interface antiga.

### Comparação de Policies

#### JSON Comparativo
- **Power User Compute** vs. **Shared Compute**:
  - Diferenças em runtime, tamanho do cluster, configuração de máquinas e auto-terminação.

### Configurações de Acesso

#### Passthrough
- **Não suportado** em clusters com Unity Catalog.
- **Importante** para ambientes que utilizam AD para autenticação de dados.

## Conclusão

Este vídeo detalhou as diferentes configurações de clusters no Databricks, explicando os tipos, modos de operação, access modes e policies. A introdução de Unity Catalog trouxe novas nomenclaturas e modos de acesso que podem causar confusão. Recomenda-se testar as configurações e consultar a documentação oficial para um entendimento mais profundo.

Para mais detalhes, consulte o mapa mental e os links de referência fornecidos nos comentários do vídeo.

---

Muito obrigado por assistir e até a próxima!

## Referências

- Documentação oficial do Databricks: [Databricks Documentation](https://docs.databricks.com/)
- Série de vídeos "Databricks 0 a 100" no YouTube: [Link para a série](https://www.youtube.com/playlist?list=PL...)
- Artigos sobre Unity Catalog e Clusters: [Unity Catalog](https://docs.databricks.com/unity-catalog/index.html), [Clusters](https://docs.databricks.com/clusters/index.html)

## Conteúdos Complementares

### Clusters Configuration Best Practices

- **Compute Configuration Reference**: Guia extenso sobre como criar e configurar recursos de computação, incluindo políticas, modos de acesso e versões do Databricks Runtime. [Link](https://docs.databricks.com/en/compute/configure.html)
- **Cluster Configuration on Databricks Best Practices**: Artigo que detalha melhores práticas para configuração de clusters, incluindo tipos de instâncias e otimização de recursos. [Link](https://www.linkedin.com/pulse/cluster-configuration-databricks-best-practices-santos-saenz-ferrero-h1j0f)
- **Types of Clusters in Databricks 2023**: Explicação dos diferentes tipos de clusters disponíveis, como Single-Node, Multi-Node, Auto-Scaling, High Concurrency e GPU-Enabled. [Link](https://azuretrainings.in/types-of-clusters-in-databricks/)
- **Beginners Guide to Cluster Configuration for MLOps**: Guia introdutório sobre configuração de clusters para MLOps, abordando modos de acesso e suporte a várias linguagens. [Link](https://community.databricks.com/t5/technical-blog/mlops-gym-beginners-guide-to-cluster-configuration-for-mlops/ba-p/66373)
- **Cluster Configuration Best Practices Video**: Vídeo detalhado sobre as melhores práticas para configuração de clusters no Databricks, apresentado por um engenheiro sênior. [Link](https://www.youtube.com/watch?v=DH7psXPl9c0)
- **Cluster Configuration - Adatis**: Artigo sobre os dois tipos principais de clusters no Azure Databricks e suas aplicações práticas. [Link](https://adatis.co.uk/databricks-cluster-configuration/)

### Políticas de Clusters

- **General Availability of Cluster Policies**: Anúncio sobre a disponibilidade geral das políticas de clusters, que restringem a forma como os usuários interagem com as configurações de clusters. [Link](https://www.databricks.com/blog/2023/04/07/announcing-general-availability-cluster-policies.html)
- **Create and Manage Compute Policies**: Tutorial sobre como criar e gerenciar políticas de computação no Databricks, limitando capacidades de criação de clusters para usuários e grupos de usuários. [Link](https://docs.databricks.com/en/admin/clusters/policies.html)
- **Databricks Industry Solutions - Cluster Policy**: Guia sobre como definir políticas de clusters usando a API de Políticas de Clusters 2.0 e a API de Permissões 2.0. [Link](https://github.com/databricks-industry-solutions/cluster-policy)
- **Understanding Databricks Cluster Types in Unity Catalog**: Artigo que explora os diferentes tipos de clusters dentro do Unity Catalog, suas aplicações práticas e desafios de implementação. [Link](https://www.tredence.com/blog/databricks-cluster-types)
```

Esta documentação detalhada em Markdown fornece uma visão completa das configurações de clusters no Databricks, desmistificando as nomenclaturas e modos de operação com exemplos práticos e comparações. Além disso, inclui conteúdos complementares que enriquecem ainda mais o entendimento sobre o tema.
