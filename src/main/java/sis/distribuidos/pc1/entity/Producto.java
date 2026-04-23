package sis.distribuidos.pc1.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "productos")
@Getter @Setter
@NoArgsConstructor @AllArgsConstructor
public class Producto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "IdProducto")
    private Integer idProducto;

    @Column(name = "NombreProducto")
    private String nombreProducto;

    @Column(name = "IdProveedor")
    private Integer idProveedor;

    @Column(name = "IdCategoria")
    private Integer idCategoria;

    @Column(name = "CantidadPorUnidad")
    private String cantidadPorUnidad;

    @Column(name = "PrecioUnidad")
    private Double precioUnidad;

    @Column(name = "UnidadesEnExistencia")
    private Integer unidadesEnExistencia;

    @Column(name = "UnidadesEnPedido")
    private Integer unidadesEnPedido;

    @Column(name = "NivelNuevoPedido")
    private Integer nivelNuevoPedido;

    @Column(name = "Suspendido")
    private String suspendido;
}
