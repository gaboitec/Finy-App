import tkinter as tk
from gui.vistas.login_vista import LoginView
from gui.vistas.inicio_vista import HomeView
from gui.vistas.registro_vista import RegistroView

from logica.usuario_logica import UsuarioService
from logica.analitica_logica import AnalyticsService
from logica.deuda_logica import DeudaService

from gestores.usuarios_gestor import UsuariosRepo
from gestores.transacciones_gestor import TransactionsRepo
from gestores.presupuestos_gestor import PresupuestosRepo
from gestores.deudas_gestor import DeudasRepo

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("FINY")
        self.root.geometry("900x600")
        self.usuario = None

        #self.usuario_logica = UsuarioService(UsuariosRepo())
        self.analytics_logica = AnalyticsService(TransactionsRepo(), PresupuestosRepo())
        self.deuda_logica = DeudaService(DeudasRepo())

        self._mostrar_login()

        self.root.mainloop()

    def _mostrar_login(self):
        self._limpiar_vista()
        self.login_view = LoginView(self.root, on_login=self._login_exitoso)
        self.login_view.master.mostrar_registro = self.mostrar_registro
        self.login_view.pack(fill="both", expand=True)

    def _login_exitoso(self, usuario):
        self.usuario = usuario
        self._mostrar_home()

    def _mostrar_home(self):
        self._limpiar_vista()
        self.home_view = HomeView(self.root, self.usuario)
        self.home_view.pack(fill="both", expand=True)

    def mostrar_registro(self):
        self._limpiar_vista()
        self.registro_view = RegistroView(self.root, on_registro_exitoso=self._mostrar_login)
        self.registro_view.pack(fill="both", expand=True)

    def _limpiar_vista(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    App()
