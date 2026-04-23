package sis.distribuidos.pc1.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import sis.distribuidos.pc1.entity.Pedido;

public interface PedidoRepository extends JpaRepository<Pedido, Integer> {}
