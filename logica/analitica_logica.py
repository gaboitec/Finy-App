from gestores.transacciones_gestor import TransactionsRepo
from gestores.presupuestos_gestor import PresupuestosRepo
from dominio.objetos_valor.tipo_transaccion import TipoTransaccion
#from datetime import datetime
from collections import defaultdict

class AnalyticsService:
    def __init__(self, tx_repo: TransactionsRepo, presupuesto_repo: PresupuestosRepo):
        self.tx_repo = tx_repo
        self.presupuesto_repo = presupuesto_repo

    def total_por_tipo(self, id_usuario: int) -> dict[str, float]:
        transacciones = self.tx_repo.obtener_por_usuario(id_usuario)
        totales = {"ingreso": 0.0, "gasto": 0.0}
        for tx in transacciones:
            totales[tx.tipo.value] += tx.cantidad
        return totales

    def total_por_categoria(self, id_usuario: int) -> dict[int, float]:
        transacciones = self.tx_repo.obtener_por_usuario(id_usuario)
        totales = defaultdict(float)
        for tx in transacciones:
            totales[tx.id_categoria] += tx.cantidad
        return dict(totales)

    def evolucion_mensual(self, id_usuario: int) -> dict[str, dict[str, float]]:
        transacciones = self.tx_repo.obtener_por_usuario(id_usuario)
        resumen = defaultdict(lambda: {"ingreso": 0.0, "gasto": 0.0})
        for tx in transacciones:
            clave = tx.fecha.strftime("%Y-%m")
            resumen[clave][tx.tipo.value] += tx.cantidad
        return dict(resumen)

    def cumplimiento_presupuestos(self, id_usuario: int) -> list[dict]:
        presupuestos = self.presupuesto_repo.obtener_por_usuario(id_usuario)
        transacciones = self.tx_repo.obtener_por_usuario(id_usuario)
        resultados = []

        for p in presupuestos:
            total_gastado = sum(
                tx.cantidad for tx in transacciones
                if tx.tipo == TipoTransaccion.GASTO and
                   p.fecha_inicio <= tx.fecha.date() <= p.fecha_fin and
                   (p.id_categoria is None or tx.id_categoria == p.id_categoria)
            )
            cumplimiento = total_gastado / p.cantidad if p.cantidad > 0 else 0
            resultados.append({
                "id_presupuesto": p.id,
                "categoria": p.id_categoria,
                "gasto": total_gastado,
                "limite": p.cantidad,
                "cumplimiento": round(cumplimiento * 100, 2)
            })

        return resultados