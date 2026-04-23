package sis.distribuidos.pc1.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import sis.distribuidos.pc1.entity.Producto;
import sis.distribuidos.pc1.service.ProductoService;

import java.util.List;

@RestController
@RequestMapping("/api/productos")
@CrossOrigin("*")
public class ProductoController {

    private final ProductoService service;

    public ProductoController(ProductoService service) {
        this.service = service;
    }

    // ✅ Crear producto
    @PostMapping
    public Producto crear(@RequestBody Producto data) {
        return service.crearProducto(data);
    }

    // ✅ Listar productos
    @GetMapping
    public List<Producto> listar() {
        return service.listarProductos();
    }

    // ✅ Buscar por ID
    @GetMapping("/{id}")
    public Producto buscar(@PathVariable Integer id) {
        return service.buscarProductoId(id);
    }
}
