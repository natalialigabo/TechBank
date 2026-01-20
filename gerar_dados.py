import psycopg2
import random
from faker import Faker

# Configura o gerador de dados para o padrão Brasileiro
fake = Faker('pt_BR')

def conectar_banco():
    try:
        conn = psycopg2.connect(
            dbname="tech_bank",
            user="postgres",
            password="admin", 
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None

def gerar_clientes_e_contas(qtd_clientes, cursor):
    print(f"--- Gerando {qtd_clientes} clientes e contas ---")
    
    ids_contas_geradas = []

    for _ in range(qtd_clientes):
        # 1. Gerar dados do Cliente
        nome = fake.name()
        cpf = fake.cpf().replace('.', '').replace('-', '')
        email = fake.email()
        nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90)
        
        # Inserir Cliente
        cursor.execute("""
            INSERT INTO clientes (nome, cpf, email, data_nascimento)
            VALUES (%s, %s, %s, %s) RETURNING id;
        """, (nome, cpf, email, nascimento))
        
        cliente_id = cursor.fetchone()[0]
        
        # 2. Gerar Conta para este Cliente
        # Alguns clientes terão saldo alto, outros zero
        saldo_inicial = round(random.uniform(0, 50000), 2)
        tipo = random.choice(['CORRENTE', 'POUPANCA'])
        
        cursor.execute("""
            INSERT INTO contas (cliente_id, numero_conta, tipo_conta, saldo)
            VALUES (%s, %s, %s, %s) RETURNING id;
        """, (cliente_id, fake.random_int(min=10000, max=99999), tipo, saldo_inicial))
        
        conta_id = cursor.fetchone()[0]
        ids_contas_geradas.append(conta_id)
        
    return ids_contas_geradas

def gerar_transacoes(qtd_transacoes, ids_contas, cursor):
    print(f"--- Simulando {qtd_transacoes} transações financeiras ---")
    
    tipos = ['PIX', 'TED', 'DOC', 'BOLETO', 'COMPRA_DEBITO']
    
    for _ in range(qtd_transacoes):
        # Escolhe duas contas aleatórias (Origem e Destino)
        origem = random.choice(ids_contas)
        destino = random.choice(ids_contas)
        
        # Evita transferir para si mesmo
        while destino == origem:
            destino = random.choice(ids_contas)
            
        valor = round(random.uniform(1.0, 5000.0), 2)
        tipo = random.choice(tipos)
        status = random.choice(['PENDENTE', 'PROCESSADO', 'FALHA'])
        
        cursor.execute("""
            INSERT INTO transacoes (conta_origem_id, conta_destino_id, valor, tipo_transacao, status_processamento)
            VALUES (%s, %s, %s, %s, %s);
        """, (origem, destino, valor, tipo, status))

def main():
    conn = conectar_banco()
    if not conn:
        return

    cursor = conn.cursor()
    
    # 1. Vamos criar 100 novos clientes (pode aumentar esse número depois!)
    ids_novas_contas = gerar_clientes_e_contas(100, cursor)
    
    # 2. Vamos criar 500 transações entre essas contas
    gerar_transacoes(500, ids_novas_contas, cursor)
    
    # Salvar alterações no banco
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Sucesso! O banco de dados foi povoado.")

if __name__ == "__main__":
    main()