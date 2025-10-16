from gestores.deudas_gestor import DeudasRepo
from gestores.transacciones_gestor import TransactionsRepo
from gestores.presupuestos_gestor import PresupuestosRepo
from gestores.usuarios_gestor import UsuariosRepo
from gui.vistas.inicio_vista import HomeView
from logica.usuario_logica import UsuarioService
from logica.analitica_logica import AnalyticsService
from logica.deuda_logica import DeudaService
import tkinter as tk

usuario = UsuarioService(UsuariosRepo()).buscar_por_correo("yefry@correo.com")
print(usuario)

# Crear ventana principal
root = tk.Tk()
root.title("FINY - Dashboard")
root.geometry("900x600")

# Inyectar servicios
servicios = {
    "analytics": AnalyticsService(TransactionsRepo(), PresupuestosRepo()),
    "deuda": DeudaService(DeudasRepo())
}

# Mostrar HomeView
home = HomeView(root, usuario, servicios)
root.mainloop()