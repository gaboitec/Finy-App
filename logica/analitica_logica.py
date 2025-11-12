from gestores.transacciones_gestor import TransactionsRepo
from gestores.presupuestos_gestor import PresupuestosRepo
from gestores.deudas_gestor import DeudasRepo
from gestores.deudores_gestor import DeudoresRepo

from dominio.objetos_valor.tipo_transaccion import TipoTransaccion

from datetime import datetime, timedelta
from collections import defaultdict

class AnalyticsService:
    def __init__(self, tx_repo: TransactionsRepo = None, presupuesto_repo: PresupuestosRepo = None,
                 deuda_repo: DeudasRepo = None, deudor_repo: DeudoresRepo = None):
        self.tx_repo = tx_repo
        self.presupuesto_repo = presupuesto_repo
        self.deuda_repo = deuda_repo
        self.deudor_repo = deudor_repo

        self.hoy = datetime.now().date()
        self.inicio = self.hoy - timedelta(days=30)

    def total_por_tipo(self, id_usuario: int) -> dict[str, float]:
        transacciones = self.tx_repo.obtener_por_usuario(id_usuario)
        totales = {"ingreso": 0.0, "gasto": 0.0}
        for tx in transacciones:
            totales[str(tx.tipo.value)] += tx.cantidad
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

    def porcentaje_por_categoria(self, id_usuario: int, tipo: str) -> dict[str, float]:
            transacciones = self.tx_repo.obtener_por_usuario(id_usuario)
            totales = defaultdict(float)
            total_general = 0.0

            for tx in transacciones:
                if tx.tipo.value == tipo:
                    totales[tx.id_categoria] += tx.cantidad
                    total_general += tx.cantidad

            return {cat: (valor / total_general) * 100 for cat, valor in totales.items() if total_general > 0}

    def comparacion_ingresos_gastos(self, id_usuario: int) -> dict[str, dict[str, float]]:
        transacciones = self.tx_repo.obtener_por_usuario(id_usuario)
        resumen = defaultdict(lambda: {"ingresos": 0.0, "gastos": 0.0})

        for tx in transacciones:
            mes = tx.fecha[:7]  # YYYY-MM
            if tx.tipo.value == "ingreso":
                resumen[mes]["ingresos"] += tx.cantidad
            elif tx.tipo.value == "gasto":
                resumen[mes]["gastos"] += tx.cantidad

        return dict(resumen)

    def evolucion_por_tipo(self, id_usuario: int, tipo: str) -> dict[str, float]:
        transacciones = self.tx_repo.obtener_por_usuario(id_usuario)
        evolucion = defaultdict(float)

        for tx in transacciones:
            if tx.tipo.value == tipo:
                fecha = tx.fecha[:10]  # YYYY-MM-DD
                evolucion[fecha] += tx.cantidad

        return dict(sorted(evolucion.items()))

    def evolucion_deudas(self, id_usuario: int) -> dict[str, float]:
        if not self.deuda_repo:
            return {}
        deudas = self.deuda_repo.obtener_por_usuario(id_usuario)
        evolucion = defaultdict(float)

        for deuda in deudas:
            fecha = deuda.plazo_inicio[:10]
            evolucion[fecha] += deuda.cantidad

        return dict(sorted(evolucion.items()))

    def evolucion_deudores(self, id_usuario: int) -> dict[str, float]:
        if not self.deudor_repo:
            return {}
        deudores = self.deudor_repo.obtener_por_usuario(id_usuario)
        evolucion = defaultdict(float)

        for d in deudores:
            fecha = d.plazo_inicio[:10]
            evolucion[fecha] += d.plazo_inicio

        return dict(sorted(evolucion.items()))

    def evolucion_presupuestos(self, id_usuario: int) -> dict[str, dict[str, float]]:
        presupuestos = self.presupuesto_repo.obtener_por_usuario(id_usuario)
        resumen = defaultdict(lambda: {"asignado": 0.0, "usado": 0.0})

        for p in presupuestos:
            fecha = p.fecha_inicio
            resumen[fecha]["asignado"] += p.cantidad

        return dict(sorted(resumen.items()))

    def evolucion_transacciones(self, id_usuario: int) -> dict[str, int]:
        transacciones = self.tx_repo.obtener_por_usuario(id_usuario)
        conteo = defaultdict(int)

        for tx in transacciones:
            fecha = tx.fecha[:10]
            conteo[fecha] += 1

        return dict(sorted(conteo.items()))