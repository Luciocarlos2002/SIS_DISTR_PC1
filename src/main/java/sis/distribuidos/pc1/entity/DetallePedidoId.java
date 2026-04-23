package sis.distribuidos.pc1.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.io.Serializable;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class DetallePedidoId implements Serializable {
    private Integer idPedido;
    private Integer idProducto;
}
