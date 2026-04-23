package sis.distribuidos.pc1.service;

import org.springframework.stereotype.Service;
import sis.distribuidos.pc1.entity.Producto;
import sis.distribuidos.pc1.repository.ProductoRepository;

import java.util.List;

@Service
public class ProductoService {

    private final ProductoRepository repo;

    public ProductoService(ProductoRepository repo) {
        this.repo = repo;
    }

    // ✅ Crear producto
    public Producto crearProducto(Producto data) {

        if (data.getNombreProducto() == null || data.getNombreProducto().isEmpty()) {
            throw new RuntimeException("El nombre del producto es obligatorio");
        }

        if (data.getPrecioUnidad() == null || data.getPrecioUnidad() <= 0) {
            throw new RuntimeException("El precio debe ser mayor a 0");
        }

        return repo.save(data);
    }

    // ✅ Listar productos
    public List<Producto> listarProductos() {
        return repo.findAll();
    }

    // ✅ Buscar por ID
    public Producto buscarProductoId(Integer id) {
        return repo.findById(id)
                .orElseThrow(() -> new RuntimeException("Producto no encontrado con ID: " + id));
    }
}