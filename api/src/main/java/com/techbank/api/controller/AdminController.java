package com.techbank.api.controller;

import com.techbank.api.service.ReconciliacaoService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/admin")
public class AdminController {

    private final ReconciliacaoService service;

    public AdminController(ReconciliacaoService service) {
        this.service = service;
    }

    @GetMapping("/status") // URL final: /admin/status
    public String checarStatus() {
        return service.verificarStatusBanco();
    }
}