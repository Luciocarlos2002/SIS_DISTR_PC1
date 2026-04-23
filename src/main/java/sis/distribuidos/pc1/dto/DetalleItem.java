package sis.distribuidos.pc1.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class DetalleItem {
    private Integer idProducto;
    private Double precioUnidad;
    private Integer cantidad;
    private Integer descuento;
}
