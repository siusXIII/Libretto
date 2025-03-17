import flet as ft

class View:
    def __init__(self, page: ft.Page):
        self._txtIn = None
        self._btnIn = None
        self._txtOut = None
        self._page = page
        self._controller = None

    def setController(self, c):
        self._controller = c

    def loadInterface(self):
        """
        In questo metodo definiamo e carichiamo tutti i controlli dell'interfaccia.
        :return:
        """
        self._txtIn = ft.TextField(label="Inserisci nome")
        self._btnIn = ft.ElevatedButton("Aggiungi", on_click= self._controller.handleAggiungi)
        row = ft.Row(controls=[self._txtIn, self._btnIn])
        self._txtOut = ft.Text("")
        self._page.add(row, self._txtOut)
