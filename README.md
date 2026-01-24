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


graph TD
    A["Python Data Engine"] -->|"1. INSERT (Pendentes)"| B("PostgreSQL")
    A -->|"2. Exporta Arquivo"| C["movimentacoes.dat"]
    C -->|"3. Processamento Batch"| D["COBOL Core"]
    D -->|"4. Arquivo Retorno"| E["processados.dat"]
    E -->|"5. Leitura e Auditoria"| F["Java Spring API"]
    F -->|"6. Validação e Update"| B
    G["App Flutter"] -.->|"Future: Consulta Saldo"| F


    /TechBank
├── api/                # API Java Spring Boot (Controllers, Services, Repositories)
├── core-bancario/      # Fontes COBOL (.cob) e binários compilados
├── data-engine/        # Scripts Python para geração de massa e ETL
├── database/           # Scripts SQL (DDL) para criação e alteração de tabelas
└── README.md           # Documentação do projeto

