import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._sceltaNodo = None

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        durataMinTxt = self._view._txtInDurata.value

        if durataMinTxt == "":
            self._view.create_alert("NON HA INSERITO NESSUN VALORE")
            return

        try:
            durataMin = int(durataMinTxt)
        except ValueError:
            self._view.create_alert("INSERITO UN VALORE NON VALIDO")
            return


        self._model.buildGraph(durataMin)
        self.fillDDAlbum()
        if self._model.get_num_of_nodes() == 0:
            self._view.create_alert("IL GRAFO NON HA NODI")
        else:
            self._view.txt_result.controls.append(ft.Text("GRAFO CREATO"))
            self._view.txt_result.controls.append(ft.Text(f"VERTICI-> {self._model.get_num_of_nodes()}"))
            self._view.txt_result.controls.append(ft.Text(f"ARCHI-> {self._model.get_num_of_edges()}"))


        self._view.update_page()

    # def getSelectedAlbum(self, e):
    #     pass

    def handleAnalisiComp(self, e):
        self._view.txt_result.controls.clear()
        if self._sceltaNodo is None:
            self._view.txt_result.controls.append(ft.Text(f"ATTENZIONE ALBUM NON SELEZIONATO", color="red"))
            return
        infoCC = self._model.infoComponenteConnessa(self._sceltaNodo)
        self._view.txt_result.controls.append(ft.Text(f"ANALISI COMPONENTE CONNESSA = {self._sceltaNodo.Title}"))
        self._view.txt_result.controls.append(ft.Text(
            f"DIMENSIONE CC = {infoCC[0]}\n"
            f"DURATA TOTALE CC = {infoCC[1]:.4f}"))

        self._view.update_page()

    def handleGetSetAlbum(self, e):
        pass

    def fillDDAlbum(self):
        nodi = self._model.get_nodes()

        self._view._ddAlbum.options.clear()

        #.sorted() BUILT-IN
        #nodi = sorted(nodi, key = lambda x: x.AlbumId, reverse = True)

        #.sort() ORDINA IN PLACE, NON DEVI PASSARLI ARGOMENTI POSIZIONALI
        nodi.sort( key = lambda x: x.AlbumId)
        for nodo in nodi:
            self._view._ddAlbum.options.append(ft.dropdown.Option(text = nodo.Title,
                                                                  on_click=self.readDDValue,
                                                                  data=nodo))

        self._view.update_page()

    def readDDValue(self,e):
        if e.control.data is None:
            print("ERRORE NEL LEGGERE VALORE DD")
            self._sceltaNodo = None
        self._sceltaNodo = e.control.data
