from dominio.entidades.transaccion import Transaccion
from dominio.objetos_valor.tipo_transaccion import TipoTransaccion
from gestores.transacciones_gestor import TransactionsRepo
from datetime import datetime

class TransaccionService:
    def __init__(self, repo: TransactionsRepo):
        self.repo = repo

    def agregar_transaccion(self, id_usuario: int, id_categoria: int, tipo: TipoTransaccion, cantidad: float, descripcion: str) -> int:
        tx = Transaccion(
            id=None,
            id_usuario=id_usuario,
            id_categoria=id_categoria,
            tipo=tipo,
            cantidad=cantidad,
            descripcion=descripcion,
            fecha=datetime.now()
        )
        return self.repo.crear(tx)

    def total_por_tipo(self, id_usuario: int, tipo: TipoTransaccion) -> float:
        transacciones = self.repo.obtener_por_usuario(id_usuario)
        return sum(tx.cantidad for tx in transacciones if tx.tipo == tipo)