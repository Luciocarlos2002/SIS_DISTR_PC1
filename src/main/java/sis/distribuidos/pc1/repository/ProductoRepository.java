package sis.distribuidos.pc1.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import sis.distribuidos.pc1.entity.Producto;

public interface ProductoRepository extends JpaRepository<Producto, Integer> {
}
