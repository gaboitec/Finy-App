from dataclasses import dataclass

@dataclass
class Categoria:
    id: int | None
    id_usuario: int
    nombre: str