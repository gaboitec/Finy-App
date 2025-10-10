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
        return self.repo.obtener_por_usuario(id_usuario)