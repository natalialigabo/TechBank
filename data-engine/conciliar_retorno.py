import psycopg2

def conciliar():
    conn = None
    try:
        conn = psycopg2.connect(dbname="tech_bank", user="postgres", password="admin", host="localhost")
        cursor = conn.cursor()

        with open('processados.dat', 'r') as f:
            ids = [line.strip() for line in f.readlines()]

        if not ids:
            print("Nenhum ID para processar.")
            return

        
        for trans_id in ids:
            cursor.execute("UPDATE transacoes SET status_processamento = 'PROCESSADO' WHERE id = %s", (int(trans_id),))
        
        conn.commit()
        print(f"✅ Sucesso! {len(ids)} transações marcadas como PROCESSADAS no PostgreSQL.")

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        if conn: conn.close()

if __name__ == "__main__":
    conciliar()