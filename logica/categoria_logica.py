from dominio.entidades.categoria import Categoria
from gestores.categorias_gestor import CategoriasRepo

class CategoriaService:
    def __init__(self, repo: CategoriasRepo):
        self.repo = repo

    def crear_categoria(self, id_usuario: int, nombre: str) -> int:
        categoria = Categoria(
            id=None,
            id_usuario=id_usuario,
            nombre=nombre
        )
        return self.repo.crear(categoria)

    def listar_por_usuario(self, id_usuario: int) -> list[Categoria]:
        try:
            return self.repo.obtener_por_usuario(id_usuario)
        except Exception as e:
            print(f"Error al obtener datos para usuario {id_usuario}: {e}")
            return []

    def buscar_por_nombre(self, usuario, cat):
        try:
            return self.repo.por_nombre(usuario, cat)[0]
        except Exception as e:
            print(f"Error al obtener datos para usuario {usuario}: {e}")
            return []