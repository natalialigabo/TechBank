package com.techbank.api.service;

import com.techbank.api.repository.TransacaoRepository;
import org.springframework.stereotype.Service;

@Service
public class ReconciliacaoService {

    private final TransacaoRepository repository;

    public ReconciliacaoService(TransacaoRepository repository) {
        this.repository = repository;
    }

    public String verificarStatusBanco() {
        long total = repository.count();
        return "O Banco de Dados PostgreSQL tem " + total + " transações registradas.";
    }
}
