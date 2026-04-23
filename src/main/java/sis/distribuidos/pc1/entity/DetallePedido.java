package sis.distribuidos.pc1.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.IdClass;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "detalle")
@Getter @Setter
@IdClass(DetallePedidoId.class)
public class DetallePedido {

    @Id
    @Column(name = "IdPedido")
    private Integer idPedido;

    @Id
    @Column(name = "IdProducto")
    private Integer idProducto;

    @Column(name = "PrecioUnidad")
    private Double precioUnidad;

    @Column(name = "Cantidad")
    private Integer cantidad;

    @Column(name = "Descuento")
    private Integer descuento;
}
