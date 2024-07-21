# Databricks 0 a 100 - [3] - Clusters Configs - Parte 1 - Desmistificando Nomenclaturas

## Introdução
Neste vídeo da série "Databricks 0 a 100", abordamos as configurações de clusters no Databricks. O objetivo é desmistificar as nomenclaturas e simplificar o entendimento das diversas configurações e modos operacionais dos clusters. Este vídeo é uma atualização de um conteúdo anterior, agora dividido em partes menores para facilitar a compreensão.

## Tópicos Abordados
1. **Tipos de Clusters**
2. **Modos de Operação dos Clusters**
3. **Policies (Políticas)**
4. **Access Mode (Modo de Acesso)**
5. **Comparação entre Interfaces Nova e Antiga**
6. **De-Para das Configurações Antigas para as Novas**

## 1. Tipos de Clusters
Existem quatro tipos principais de clusters no Databricks:
- **All Purpose Clusters**: Utilizados para desenvolvimento, debug e exploração de dados.
- **Job Clusters**: Criados para a execução de jobs específicos e são encerrados após a execução.
- **SQL Compute Clusters**: Focados para consultas em Data Warehouses.
- **Delta Live Tables Clusters**: Utilizados para pipelines de Delta Live Tables.

### Detalhamento dos Tipos de Clusters
- **All Purpose Clusters**: Interativos e compartilhados, conectados a notebooks.
- **Job Clusters**: Criados e encerrados automaticamente durante a execução de um job.
- **SQL Compute Clusters**: Utilizados por ferramentas de visualização para consultas SQL.
- **Delta Live Tables Clusters**: Configurações específicas para pipelines de Delta Live Tables.

## 2. Modos de Operação dos Clusters
Os modos de operação dos clusters foram atualizados com a introdução do Unity Catalog:
- **Single Node**: Um único nó que executa tanto o driver quanto o worker.
- **Multi Node**: Clusters com múltiplos nós, incluindo um driver e vários workers.
- **High Concurrency (Legado)**: Clusters com alta concorrência, agora substituídos por modos mais modernos.
- **Standard (Legado)**: Clusters padrão, também substituídos por configurações mais atuais.

### Descrição dos Modos de Operação
- **Single Node**: Ideal para testes rápidos e exploração de dados devido ao menor custo.
- **Multi Node**: Recomendado para produção e processamento de dados em larga escala.
- **High Concurrency e Standard (Legado)**: Substituídos por Multi Node e Single Node.

## 3. Policies (Políticas)
Policies são conjuntos de regras que restringem ou configuram clusters automaticamente:
- **Unrestricted**: Permite todas as configurações.
- **Personal Compute**: Para clusters pessoais, geralmente single user.
- **Power User Compute**: Clusters multi node para usuários avançados.
- **Shared Compute**: Clusters compartilhados, ideais para uso com Unity Catalog.

### Detalhamento das Policies
- **Unrestricted**: Sem restrições de configuração.
- **Personal Compute**: Configurações simplificadas para uso individual.
- **Power User Compute**: Configurações avançadas para usuários experientes.
- **Shared Compute**: Configurações para clusters compartilhados, suportando Unity Catalog.

## 4. Access Mode (Modo de Acesso)
O modo de acesso define como os dados serão acessados dentro do cluster:
- **Single User**: Cluster pessoal, não compartilhado.
- **Shared**: Cluster compartilhado entre múltiplos usuários.
- **No Isolation**: Cluster sem isolamento, acesso total.
- **Custom**: Configurações legadas e específicas.

### Detalhamento dos Access Modes
- **Single User**: Exclusivo para um usuário, ideal para desenvolvimento pessoal.
- **Shared**: Compartilhado, ideal para equipes e colaboração.
- **No Isolation e Custom**: Utilizados para manutenção de clusters legados.

## 5. Comparação entre Interfaces Nova e Antiga
Diferenças entre as interfaces de criação de clusters:
- **Interface Nova**: Simplicidade e suporte ao Unity Catalog.
- **Interface Antiga**: Suporte a modos legados como High Concurrency e Standard.

### Detalhamento das Interfaces
- **Interface Nova**: Policies claras e modos de acesso definidos.
- **Interface Antiga**: Modos legados e sem suporte a Unity Catalog.

## 6. De-Para das Configurações Antigas para as Novas
Tabela de correlação entre modos antigos e novos:
- **Standard**: Agora é No Isolation Shared.
- **Standard com Passthrough**: Agora é Single User com Passthrough.
- **High Concurrency**: Agora é No Isolation Shared.
- **High Concurrency com Passthrough**: Agora é Shared com Passthrough.

### Tabela de Comparação
| Antigo                         | Novo                     |
|-------------------------------|--------------------------|
| Standard                      | No Isolation Shared      |
| Standard com Passthrough      | Single User com Passthrough |
| High Concurrency              | No Isolation Shared      |
| High Concurrency com Passthrough | Shared com Passthrough   |

## Conclusão
Este vídeo e documentação visam esclarecer e simplificar as diversas configurações de clusters no Databricks. A atualização para a interface nova e a introdução do Unity Catalog trouxeram mudanças significativas que melhoram a segurança, gerenciamento e eficiência dos clusters. Recomenda-se estudar e testar as novas configurações para uma melhor adaptação e aproveitamento das novas funcionalidades.

**Referências:**
- [Documentação Oficial do Databricks](https://docs.databricks.com)
- [Compute configuration reference](https://docs.databricks.com/en/compute/configure.html)
- [Compute configuration best practices](https://docs.databricks.com/en/compute/cluster-config-best-practices.html)
- [Types of Clusters in Databricks 2023](https://azuretrainings.in/types-of-clusters-in-databricks/)
- [Databricks Clusters: Types and 2 Steps to create](https://hevodata.com/learn/databricks-clusters/)
- [Cluster configuration on Databricks best practices](https://www.linkedin.com/pulse/cluster-configuration-databricks-best-practices-santos-saenz-ferrero-h1j0f)

---

Espero que esta documentação detalhada ajude a desmistificar as nomenclaturas e configurações de clusters no Databricks. Para mais detalhes, consulte a documentação oficial e explore as opções diretamente no portal do Databricks.
