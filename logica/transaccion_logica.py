from dominio.entidades.transaccion import Transaccion
from dominio.objetos_valor.tipo_transaccion import TipoTransaccion
from dominio.objetos_valor.metodo_transaccion import MetodoTransaccion
from gestores.transacciones_gestor import TransactionsRepo
from logica.categoria_logica import CategoriaService
from gestores.categorias_gestor import CategoriasRepo
from datetime import datetime

class TransaccionService:
    def __init__(self, repo: TransactionsRepo):
        self.repo = repo

    def agregar_transaccion(self, id_usuario: int, categoria: str, tip: str, cantidad: float, descripcion: str, metod) -> int:
        tipo = TipoTransaccion(tip.lower())
        id_categoria = CategoriaService(CategoriasRepo()).buscar_por_nombre(id_usuario, categoria)
        metodo = MetodoTransaccion(metod.lower())
        tx = Transaccion(
            id=None,
            id_usuario=id_usuario,
            id_categoria=id_categoria.id,
            tipo=tipo,
            cantidad=cantidad,
            descripcion=descripcion,
            fecha=datetime.now(),
            metodo=metodo,
            categoria=""
        )
        return self.repo.crear(tx)

    def total_por_tipo(self, id_usuario: int, tipo: TipoTransaccion) -> float:
        transacciones = self.repo.obtener_por_usuario(id_usuario)
        return sum(tx.cantidad for tx in transacciones if tx.tipo == tipo)

    def obtener_por_usuario(self,id_usuario: int):
        return self.repo.obtener_por_usuario(id_usuario)