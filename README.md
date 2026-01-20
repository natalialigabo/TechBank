# TechBank Hybrid System 🚀

Este projeto simula o ecossistema de uma Fintech moderna integrada a um sistema bancário legado.

## 🛠 Stack Tecnológica

- **Banco de Dados:** PostgreSQL (Relacional)
- **Data Engine:** Python (Faker, Psycopg2)
- **Core Bancário:** COBOL (Processamento Batch)
- **API:** Java Spring Boot (Em breve)
- **Frontend:** Flutter (Em breve)

## ⚙️ Como funciona?

1. O Python gera dados fictícios no Postgres.
2. O Python exporta transações PENDENTES para um arquivo flat (.dat).
3. O COBOL processa as taxas e gera um arquivo de retorno.
4. (Próximo passo) O Java expõe os resultados para o cliente final.
5. (Próximo passo) O Flutter oferece uma interface amigável para o usuário.

## 📂 Estrutura do Projeto