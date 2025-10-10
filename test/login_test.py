from gestores.usuarios_gestor import UsuariosRepo
from logica.usuario_logica import UsuarioService

usuarios_repo = UsuariosRepo()
usuario_service = UsuarioService(usuarios_repo)

nuevo_id = usuario_service.registrar_usuario("Yefry", "yefry@correo.com", "hash123")
print("Usuario creado con ID:", nuevo_id)

usuario = usuario_service.buscar_por_correo("yefry@correo.com")
print("Usuario encontrado:", usuario)