from dominio.entidades.usuario import Usuario
from gestores.usuarios_gestor import UsuariosRepo
from datetime import date
from dominio.objetos_valor.estado_usuario import Estado

class UsuarioService:
    def __init__(self, repo: UsuariosRepo):
        self.repo = repo

    def registrar_usuario(self, nombre: str, correo: str, contrasenia: str) -> int:
        usuario = Usuario(
            id=None,
            nombre=nombre,
            correo=correo,
            contrasenia=contrasenia,
            fecha_creacion=date.today(),
            estado=Estado.ACTIVO
        )
        return self.repo.crear(usuario)

    def buscar_por_correo(self, correo: str, contr: str) -> Usuario | None:
        return self.repo.obtener_por_correo(correo, contr)
