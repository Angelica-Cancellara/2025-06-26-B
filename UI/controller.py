import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleBuildGraph(self, e):
        yearMin = int(self._view._ddYear1.value)
        yearMax = int(self._view._ddYear2.value)
        if yearMin > yearMax:
            self._view._txtGraphDetails.controls.clear()
            self._view._txtGraphDetails.controls.append(ft.Text("Range di anni non valido."))
            self._view.update_page()
            return

        self._model.buildGraph(yearMin, yearMax)
        self._view._txtGraphDetails.controls.clear()
        self._view._txtGraphDetails.controls.append(ft.Text("Grafo correttamente creato."))
        self._view._txtGraphDetails.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi."))
        self._view.update_page()

    def handlePrintDetails(self, e):
        result = self._model.getGraphDetails()
        self._view._txtGraphDetails.controls.clear()
        self._view._txtGraphDetails.controls.append(ft.Text("Stampa dettagli:"))
        for r in result:
            self._view._txtGraphDetails.controls.append(ft.Text(f"{r[0]} -- {r[1]}"))
        self._view.update_page()

    def handleCercaDreamChampionship(self, e):
        pass

    def fillDDAnnoInizio(self):
        for a in self._model.getAnni():
            self._view._ddYear1.options.append(ft.dropdown.Option(a))
        self._view.update_page()

    def fillDDAnnoFine(self):
        for a in self._model.getAnni():
            self._view._ddYear2.options.append(ft.dropdown.Option(a))
        self._view.update_page()