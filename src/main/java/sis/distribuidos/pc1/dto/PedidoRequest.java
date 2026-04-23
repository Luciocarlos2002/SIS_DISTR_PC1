package sis.distribuidos.pc1.dto;

import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;
import java.util.List;

@Getter
@Setter
public class PedidoRequest {

    private String idCliente;
    private Integer idEmpleado;
    private String fechaPedido;
    private String fechaEntrega;
    private String fechaEnvio;
    private Integer formaEnvio;
    private Double cargo;

    private String destinatario;
    private String direccionDestinatario;
    private String ciudadDestinatario;
    private String regionDestinatario;
    private String codPostalDestinatario;
    private String paisDestinatario;

    private List<DetalleItem> detalles;
}