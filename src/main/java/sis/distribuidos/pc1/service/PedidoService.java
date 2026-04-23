package sis.distribuidos.pc1.service;

import jakarta.transaction.Transactional;
import org.springframework.stereotype.Service;
import sis.distribuidos.pc1.dto.DetalleItem;
import sis.distribuidos.pc1.dto.PedidoRequest;
import sis.distribuidos.pc1.entity.DetallePedido;
import sis.distribuidos.pc1.entity.Pedido;
import sis.distribuidos.pc1.repository.DetalleRepository;
import sis.distribuidos.pc1.repository.PedidoRepository;

@Service
public class PedidoService {

    private final PedidoRepository pedidoRepo;
    private final DetalleRepository detalleRepo;

    public PedidoService(PedidoRepository pedidoRepo, DetalleRepository detalleRepo) {
        this.pedidoRepo = pedidoRepo;
        this.detalleRepo = detalleRepo;
    }

    @Transactional
    public void registrarPedido(PedidoRequest request) {

        // ✅ Validación básica
        if (request.getDetalles() == null || request.getDetalles().isEmpty()) {
            throw new RuntimeException("El pedido debe tener al menos un producto");
        }

        // 🧾 1. Guardar pedido
        Pedido pedido = new Pedido();
        pedido.setIdCliente(request.getIdCliente());
        pedido.setIdEmpleado(request.getIdEmpleado());
        pedido.setFechaPedido(request.getFechaPedido());
        pedido.setFechaEntrega(request.getFechaEntrega());
        pedido.setFechaEnvio(request.getFechaEnvio());
        pedido.setFormaEnvio(request.getFormaEnvio());
        pedido.setCargo(request.getCargo());
        pedido.setDestinatario(request.getDestinatario());
        pedido.setDireccionDestinatario(request.getDireccionDestinatario());
        pedido.setCiudadDestinatario(request.getCiudadDestinatario());
        pedido.setRegionDestinatario(request.getRegionDestinatario());
        pedido.setCodPostalDestinatario(request.getCodPostalDestinatario());
        pedido.setPaisDestinatario(request.getPaisDestinatario());

        Pedido pedidoGuardado = pedidoRepo.save(pedido);

        // 🧾 2. Guardar detalles
        for (DetalleItem item : request.getDetalles()) {

            DetallePedido detalle = new DetallePedido();
            detalle.setIdPedido(pedidoGuardado.getIdPedido());
            detalle.setIdProducto(item.getIdProducto());
            detalle.setPrecioUnidad(item.getPrecioUnidad());
            detalle.setCantidad(item.getCantidad());
            detalle.setDescuento(item.getDescuento());

            detalleRepo.save(detalle);
        }
    }
}
