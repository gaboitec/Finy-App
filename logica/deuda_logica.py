# app/servicios/deuda_service.py

from dominio.entidades.deuda import Deuda
from dominio.objetos_valor.estado_deuda import  EstadoDeuda
from gestores.deudas_gestor import DeudasRepo
from datetime import date

class DeudaService:
    def __init__(self, repo: DeudasRepo):
        self.repo = repo

    def registrar_deuda(self, id_usuario: int, plazo_inicio: date, plazo_fin: date, cantidad: float, interes: float, descripcion: str) -> int:
        deuda = Deuda(
            id=None,
            id_usuario=id_usuario,
            plazo_inicio=plazo_inicio,
            plazo_fin=plazo_fin,
            cantidad=cantidad,
            interes=interes,
            descripcion=descripcion,
            estado=EstadoDeuda.PENDIENTE
        )
        return self.repo.crear(deuda)

    def listar_por_usuario(self, id_usuario: int) -> list[Deuda]:
        return self.repo.obtener_por_usuario(id_usuario)

    def total_adeudado(self, id_usuario: int) -> float:
        deudas = self.repo.obtener_por_usuario(id_usuario)
        return sum(d.cantidad + d.cantidad * d.interes / 100 for d in deudas if d.estado == EstadoDeuda.PENDIENTE)

    def listar_por_estado(self, id_usuario: int, estado: EstadoDeuda) -> list[Deuda]:
        return [d for d in self.repo.obtener_por_usuario(id_usuario) if d.estado == estado]