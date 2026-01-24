# TechBank Hybrid System 🚀

Este projeto simula o ecossistema de uma Fintech moderna integrada a um sistema bancário legado, demonstrando a interoperabilidade entre tecnologias de diferentes eras (COBOL e Java Spring Boot).

## 🛠 Stack Tecnológica

- **Core Bancário:** COBOL (GnuCOBOL) - Processamento Batch e Regras de Negócio Legadas.
- **API & Auditoria:** Java 17 + Spring Boot 3 - Camada de conciliação e exposição de dados.
- **Data Engine:** Python (Faker, Psycopg2) - Geração de massa de dados e simulação de transações.
- **Banco de Dados:** PostgreSQL - Persistência relacional.
- **Frontend:** Flutter (Em desenvolvimento) - Interface Mobile para o cliente final.

## ⚙️ Arquitetura e Fluxo de Dados

O sistema opera em um ciclo contínuo de geração, processamento e auditoria:

1.  **Ingestão:** O Python gera transações financeiras simuladas (Empréstimos, CDB, Compras) e as insere no PostgreSQL.
2.  **Exportação Legacy:** Um script extrai transações `PENDENTES` para um arquivo flat (`.dat`) compatível com mainframes.
3.  **Processamento Batch:** O Core em COBOL lê o arquivo, aplica regras de juros/tarifas e gera um arquivo de retorno.
4.  **Auditoria Automatizada:** A API Java lê o arquivo processado pelo COBOL, cruza com os dados do banco e valida a integridade (Anti-Fraud Check).
5.  **Conciliação:** Se validado, o Java atualiza os saldos no PostgreSQL.

## 📊 Diagrama de Solução

```mermaid
graph TD
    A["Python Data Engine"] -->|"1. INSERT (Pendentes)"| B[("PostgreSQL")]
    A -->|"2. Exporta Arquivo"| C["movimentacoes.dat"]
    C -->|"3. Processamento Batch"| D["COBOL Core"]
    D -->|"4. Arquivo Retorno"| E["processados.dat"]
    E -->|"5. Leitura e Auditoria"| F["Java Spring API"]
    F -->|"6. Validação e Update"| B
    G["App Flutter"] -.->|"Future: Consulta Saldo"| F
    ```

    ## 🤖 Gemini como CTO & AI-Assisted Engineering

Este projeto vai além do uso de IA para gerar código. Foi utilizada uma arquitetura de **Engenharia de Prompt** para simular um ambiente corporativo real, onde o Gemini atua com a persona de um **Senior Bank Architect**.

### 🧠 O Papel da IA no Projeto

- **CTO & Tech Lead:** Definição de arquitetura híbrida (Legacy + Cloud) e Code Review rigoroso.
- **Product Owner:** Simulação de demandas de negócio voláteis (ex: "O Banco Central mudou a regra do PIX às 02h da manhã").
- **Chaos Manager:** Injeção de falhas propositais nos arquivos de dados para testar a resiliência da auditoria Java.

### 📝 O Prompt de Comando (System Role)

Para replicar a experiência de desenvolvimento deste projeto, foi utilizado o seguinte prompt mestre para configurar a IA:

> "Atue como um Senior Tech Lead especializado em sistemas bancários. Sua missão é me guiar na construção de um banco digital híbrido (TechBank). Você deve ser exigente com padrões de arquitetura (Clean Code), segurança e resiliência. Você não deve apenas me dar o código pronto, mas explicar o 'porquê' das decisões arquiteturais. Periodicamente, atue como o 'Chefe do Caos', sugerindo cenários de falha crítica (como corrupção de arquivos COBOL ou queda do banco de dados) para que eu precise implementar soluções de contorno."

## 📂 Estrutura do Repositório

```text
/TechBank
├── api/                # API Java Spring Boot (Controllers, Services, Repositories)
├── core-bancario/      # Fontes COBOL (.cob) e binários compilados
├── data-engine/        # Scripts Python para geração de massa e ETL
├── database/           # Scripts SQL (DDL) para criação e alteração de tabelas
└── README.md           # Documentação do projeto

```

## 🚀 Roadmap e Próximos Passos

Acompanhe a evolução do projeto no GitHub Projects.

[x] Configuração do Ambiente Híbrido (Docker/Postgres).

[x] Pipeline de Dados (Python -> COBOL).

[x] API de Auditoria em Java Spring Boot.

[ ] Implementação de Juros Compostos e Tabela Price no COBOL.

[ ] Frontend em Flutter (Dashboard do Cliente).

[ ] Dashboards de Análise de Dados (Jupyter Notebooks).