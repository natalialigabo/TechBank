IDENTIFICATION DIVISION.
       PROGRAM-ID. PROCESSAR-LOTE.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT ARQUIVO-TRANS ASSIGN TO 'movimentacoes.dat'
           ORGANIZATION IS LINE SEQUENTIAL.
       
           SELECT ARQUIVO-RETORNO ASSIGN TO 'processados.dat'
           ORGANIZATION IS LINE SEQUENTIAL.

     
           

       DATA DIVISION.
       FILE SECTION.
       FD  ARQUIVO-TRANS.
       01  REGISTRO-TRANS.
           05 ID-TRANS         PIC 9(06).
           05 ID-CONTA         PIC 9(06).
           05 VALOR-TRANS      PIC 9(08)V99.
       FD  ARQUIVO-RETORNO.
       01  REG-RETORNO.
           05 ID-RETORNO       PIC 9(06).
       WORKING-STORAGE SECTION.
       01  WS-EOF              PIC X VALUE 'N'.
       01  WS-TOTAL-TAXAS      PIC 9(08)V99 VALUE 0.
       01  WS-TAXA-FIXA        PIC 9(01)V99 VALUE 0.50.
       01  WS-CONTADOR         PIC 9(05) VALUE 0.

       PROCEDURE DIVISION.
           MAIN-PROCEDURE.
           *> Abrimos um para ler e o outro para gravar
           OPEN INPUT ARQUIVO-TRANS
           OPEN OUTPUT ARQUIVO-RETORNO
           
           DISPLAY "--- INICIANDO PROCESSAMENTO COBOL ---"
           
           PERFORM UNTIL WS-EOF = 'Y'
               READ ARQUIVO-TRANS
                   AT END 
                       MOVE 'Y' TO WS-EOF
                   NOT AT END
                       ADD 1 TO WS-CONTADOR
                       ADD WS-TAXA-FIXA TO WS-TOTAL-TAXAS
                       DISPLAY "PROC. ID: " ID-TRANS " CONTA: " ID-CONTA
                       
                       *> Movemos o ID lido para o registro de retorno e gravamos
                       MOVE ID-TRANS TO ID-RETORNO
                       WRITE REG-RETORNO
               END-READ
           END-PERFORM

           CLOSE ARQUIVO-TRANS
           CLOSE ARQUIVO-RETORNO
           
           DISPLAY "-------------------------------------"
           DISPLAY "TRANSACAO PROCESSADAS: " WS-CONTADOR
           DISPLAY "TOTAL DE TAXAS (R$):   " WS-TOTAL-TAXAS
           DISPLAY "--- FIM DO PROCESSAMENTO ---"
           STOP RUN.
         END PROGRAM PROCESSAR-LOTE.
