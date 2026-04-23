package sis.distribuidos.pc1.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import sis.distribuidos.pc1.dto.PedidoRequest;
import sis.distribuidos.pc1.service.PedidoService;

@RestController
@RequestMapping("/api/pedidos")
public class PedidoController {

    private final PedidoService service;

    public PedidoController(PedidoService service) {
        this.service = service;
    }

    @PostMapping
    public String registrar(@RequestBody PedidoRequest request) {
        service.registrarPedido(request);
        return "Pedido registrado correctamente";
    }
}
