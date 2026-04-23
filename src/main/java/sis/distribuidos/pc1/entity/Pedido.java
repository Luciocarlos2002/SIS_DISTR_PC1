package sis.distribuidos.pc1.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Entity
@Table(name = "pedidos")
@Getter @Setter
public class Pedido {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "IdPedido")
    private Integer idPedido;

    @Column(name = "IdCliente")
    private String idCliente;

    @Column(name = "IdEmpleado")
    private Integer idEmpleado;

    @Column(name = "FechaPedido")
    private String fechaPedido;

    @Column(name = "FechaEntrega")
    private String fechaEntrega;

    @Column(name = "FechaEnvío")
    private String fechaEnvio;

    @Column(name = "FormaEnvío")
    private Integer formaEnvio;

    @Column(name = "Cargo")
    private Double cargo;

    @Column(name = "Destinatario")
    private String destinatario;

    @Column(name = "DirecciónDestinatario")
    private String direccionDestinatario;

    @Column(name = "CiudadDestinatario")
    private String ciudadDestinatario;

    @Column(name = "RegiónDestinatario")
    private String regionDestinatario;

    @Column(name = "CódPostalDestinatario")
    private String codPostalDestinatario;

    @Column(name = "PaísDestinatario")
    private String paisDestinatario;
}
