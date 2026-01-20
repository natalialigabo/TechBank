package com.techbank.api.model;

import jakarta.persistence.*;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "transacoes")
public class Transacao {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "conta_origem_id")
    private Long contaOrigem;

    @Column(name = "conta_destino_id")
    private Long contaDestino;

    @Column(nullable = false)
    private BigDecimal valor;

    @Column(name = "tipo_transacao")
    private String tipoTransacao;

    @Column(name = "status_processamento")
    private String statusProcessamento;

    @Column(name = "data_transacao")
    private LocalDateTime dataTransacao;
}