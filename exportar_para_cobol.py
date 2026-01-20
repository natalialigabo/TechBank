import psycopg2

def exportar():
    conn = None # Inicializamos como None para o 'finally' não reclamar
    try:
        conn = psycopg2.connect(
            dbname="tech_bank",
            user="postgres",
            password="admin", # Coloque a senha que você usa no psql
            host="localhost"
        )
        cursor = conn.cursor()

        print("📡 Conectado ao banco para exportação...")

        cursor.execute("""
            SELECT id, conta_origem_id, valor 
            FROM transacoes 
            WHERE status_processamento = 'PENDENTE';
        """)
        
        transacoes = cursor.fetchall()

        if not transacoes:
            print("⚠️ Nenhuma transação PENDENTE encontrada.")
            return

        with open('movimentacoes.dat', 'w') as f:
            for t in transacoes:
                id_trans = str(t[0]).zfill(6)
                conta = str(t[1]).zfill(6)
                # O COBOL não entende ponto decimal facilmente, 
                # então multiplicamos por 100 para virar centavos inteiros
                valor_centavos = int(float(t[2]) * 100)
                valor_str = str(valor_centavos).zfill(10)
                
                f.write(f"{id_trans}{conta}{valor_str}\n")
        
        print(f"✅ Sucesso! Gerado arquivo 'movimentacoes.dat' com {len(transacoes)} registros.")

    except Exception as e:
        print(f"❌ Erro na exportação: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    exportar()