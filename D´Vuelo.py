import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

class Volando:
    def __init__(self):
        self.g = nx.DiGraph()
        self._aeropuerto = None
        self._vueloAIFA = None
        self._vueloAICM = None
        self._presupuesto = None
        self._vuelosrapidos = None
        print(f'El objeto {self} ha sido creado')
    def presupuesto(self):
        while True:
            try:
                self._presupuesto = float(input("Ingrese su presupuesto: "))
                break
            except ValueError:
                print("Ingresa un valor numérico válido para el presupuesto.")
        if self._presupuesto < 7500:
            self.aeropuertos()
            self.menu()
            if self._aeropuerto == "1":
                self.asIgnacionAIFA()
            elif self._aeropuerto == "2":
                self.asignacionAICM()
        elif self._presupuesto >= 7500:
            self.vuelosrapidos()
            self.menu_rapido()
            if self._vuelosrapidos == "a":
                self.destinosguardados()
                self.g.add_edge('AICM','Monterrey',weight=2)
                self.mostrar_rutarapida(self.g, 'AICM', 'Monterrey')
            # Aquí podrías agregar más lógica para otros destinos rápidos
        else:
            print("Ingresa caracteres válidos.")
            return self.presupuesto()

        #Aquí puedes meter una excepcion para caracteres que no sean números.

    def aeropuertos(self):
        print("En este caso tenemos dos opciones de vuelo, cada una tiene vuelos directos a ciertas\n"
              "partes en comparación con el otro, que podría tener el mismo destino pero\n"
              "quizá te pida hacer escala en otro país primero. Aunque también está la variante del horario, puede que el que haga escala salga mucho más temprano.")
        print("En cuanto a las opciones de vuelo tenemos son: \n"
              "1. Aeropuerto Internacional Felipe Ángeles (AIFA) en el Estado de México.\n"
              "2. Aeropuerto Internaciona Ciudad de México (AICM) en Ciudad de México.")
        while True:
            self._aeropuerto = input("Necesito que selecciones una de las dos opciones que te di (1 o 2): ")
            if self._aeropuerto in ["1", "2"]:
                break
            else:
                print("Opción inválida. Por favor, ingresa 1 o 2.")

    def menu(self):
        if self._aeropuerto == "1":
            print("Antes de enseñarte el menú de destinos en el orden en el que te los podemos ofertar, te mostraré cual es el mapa del total de recorridos programados para hoy.")
            g_mapa_aifa = nx.Graph()

            g_mapa_aifa.add_nodes_from(['AIFA','Acapulco','Bogota-Colombia','Ciudad Juárez','Monterrey','Ciudad de México','Guadalajara','Zacatecas','Puerto Vallarta','Mazatlan'])
            g_mapa_aifa.add_edge('AIFA','Acapulco')
            g_mapa_aifa.add_edge('AIFA','Bogota-Colombia')
            g_mapa_aifa.add_edge('AIFA','Ciudad Juárez')
            g_mapa_aifa.add_edge('Acapulco','Monterrey')
            g_mapa_aifa.add_edge('Acapulco','Ciudad de México')
            g_mapa_aifa.add_edge('Bogota-Colombia','Guadalajara')
            g_mapa_aifa.add_edge('Bogota-Colombia','Zacatecas')
            g_mapa_aifa.add_edge('Ciudad Juárez','Puerto Vallarta')
            g_mapa_aifa.add_edge('Ciudad Juárez','Mazatlan')
            g_mapa_aifa.add_edge('Monterrey','Ciudad de México')
            g_mapa_aifa.add_edge('Ciudad de México','Guadalajara')
            g_mapa_aifa.add_edge('Guadalajara','Zacatecas')
            g_mapa_aifa.add_edge('Zacatecas','Puerto Vallarta')
            g_mapa_aifa.add_edge('Puerto Vallarta','Mazatlan')
            plt.gcf().canvas.manager.set_window_title("Grafo General AIFA")
            plt.figure(figsize=(10, 10))
            nx.draw(g_mapa_aifa, with_labels=True, node_color='Red',edge_color='black',node_size=1000, font_size=12)
            plt.title("Grafo General de Rutas desde AIFA\n Oziel Caballero")
            plt.show()

            print("Los destinos disponibles ahora, son: ")
            print("a) Acapulco")
            print("b) Bogotá-Colombia")
            print("c) Ciudad Juárez")
            print("d) Monterrey")
            print("e) Ciudad de México")
            print("f) Guadalajara")
            print("g) Zacatecas")
            print("h) Puerto Vallarta")
            print("i) Mazatlán")
            while True:
                self._vueloAIFA = input("Con respecto al menú que te acabo de dar necesito que me des la opción\nque te interesa (a-i): ").lower()
                if self._vueloAIFA in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
                    break
                else:
                    print("Opción inválida. Por favor, elige una letra del menú.")
        elif self._aeropuerto == "2":
            print("Antes de enseñarte el menú de destinos en el orden en el que te los podemos ofertar, te mostraré cual es el mapa del total de recorridos programados para hoy.")
            g_mapa_aicm = nx.Graph()
            g_mapa_aicm.add_nodes_from(['AICM','Monterrey','Zacatecas','Puerto Vallarta','Guadalajara','Ciudad Juárez','Ciudad de México','Bogota-Colombia','Acapulco','Cancún'])
            g_mapa_aicm.add_edge('AICM','Monterrey')
            g_mapa_aicm.add_edge('Monterrey','Guadalajara')
            g_mapa_aicm.add_edge('Monterrey','Ciudad Juárez')
            g_mapa_aicm.add_edge('Guadalajara','Ciudad Juárez')
            g_mapa_aicm.add_edge('AICM','Zacatecas')
            g_mapa_aicm.add_edge('Zacatecas','Ciudad de México')
            g_mapa_aicm.add_edge('Zacatecas','Bogota-Colombia')
            g_mapa_aicm.add_edge('Ciudad de México','Bogota-Colombia')
            g_mapa_aicm.add_edge('AICM','Puerto Vallarta')
            g_mapa_aicm.add_edge('Puerto Vallarta','Acapulco')
            g_mapa_aicm.add_edge('Puerto Vallarta','Cancún')
            g_mapa_aicm.add_edge('Acapulco','Cancún')
            g_mapa_aicm.add_edge('Ciudad Juárez','Ciudad de México')
            g_mapa_aicm.add_edge('Bogota-Colombia','Acapulco')
            plt.gcf().canvas.manager.set_window_title("Grafo General AICM")
            plt.figure(figsize=(10, 10))
            nx.draw(g_mapa_aicm, with_labels=True, node_color='Red',edge_color='black',node_size=1000, font_size=12)
            plt.title("Grafo General de Rutas desde AICM\n Oziel Caballero")
            plt.show()

            print("A CONTINUACIÓN TE MOSTRARE EL MENÚ DE DESTINOS DE EL AICM:\n")
            print("Los destinos disponibles ahora, son: ")
            print("a) Monterrey")
            print("b) Zacatecas")
            print("c) Puerto Vallarta")
            print("d) Guadalajara")
            print("e) Ciudad Juárez")
            print("f) Ciudad de México")
            print("g) Bogotá-Colombia")
            print("h) Acapulco")
            print("i) Cancún")
            while True:
                self._vueloAICM = input("Con respecto al menú que te acabo de dar necesito que me des la opción\nque te interesa (a-i): ").lower()
                if self._vueloAICM in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
                    break
                else:
                    print("Opción inválida. Por favor, elige una letra del menú.")

    def asIgnacionAIFA(self):
        g_vuelo = nx.DiGraph()

        if self._vueloAIFA == "a":
            g_vuelo.add_edge('AIFA', 'Acapulco', weight=5)
        elif self._vueloAIFA == "b":
            g_vuelo.add_edge('AIFA', 'Bogotá-Colombia', weight=3)
        elif self._vueloAIFA == "c":
            g_vuelo.add_edge('AIFA', 'Ciudad Juárez', weight=6)
        elif self._vueloAIFA == "d":
            g_vuelo.add_edge('AIFA', 'Acapulco', weight=5)
            g_vuelo.add_edge('Acapulco', 'Monterrey', weight=2)
        elif self._vueloAIFA == "e":
            g_vuelo.add_edge('AIFA', 'Acapulco', weight=5)
            g_vuelo.add_edge('Acapulco', 'Ciudad de México', weight=3)
        elif self._vueloAIFA == "f":
            g_vuelo.add_edge('AIFA', 'Bogotá-Colombia', weight=3)
            g_vuelo.add_edge('Bogotá-Colombia', 'Guadalajara', weight=4)
        elif self._vueloAIFA == "g":
            g_vuelo.add_edge('AIFA', 'Bogotá-Colombia', weight=3)
            g_vuelo.add_edge('Bogotá-Colombia', 'Zacatecas', weight=1)
        elif self._vueloAIFA == "h":
            g_vuelo.add_edge('AIFA', 'Ciudad Juárez', weight=6)
            g_vuelo.add_edge('Ciudad Juárez', 'Puerto Vallarta', weight=3)
        elif self._vueloAIFA == "i":
            g_vuelo.add_edge('AIFA', 'Ciudad Juárez', weight=6)
            g_vuelo.add_edge('Ciudad Juárez', 'Mazatlán', weight=3)
        else:
            print("La opción que elegiste no es válida.")
            return

        self.mostrar_grafo(g_vuelo, "AIFA")

    def asignacionAICM(self):
        g_vuelo = nx.DiGraph()

        if self._vueloAICM == "a":
            g_vuelo.add_edge('AICM', 'Monterrey', weight=3)
        elif self._vueloAICM == "b":
            g_vuelo.add_edge('AICM', 'Zacatecas', weight=3)
        elif self._vueloAICM == "c":
            g_vuelo.add_edge('AICM', 'Puerto Vallarta', weight=2)
        elif self._vueloAICM == "d":
            g_vuelo.add_edge('AICM', 'Monterrey', weight=3)
            g_vuelo.add_edge('Monterrey', 'Guadalajara', weight=2)
        elif self._vueloAICM == "e":
            g_vuelo.add_edge('AICM', 'Monterrey', weight=3)
            g_vuelo.add_edge('Monterrey', 'Ciudad Juárez', weight=4)
        elif self._vueloAICM == "f":
            g_vuelo.add_edge('AICM', 'Zacatecas', weight=3)
            g_vuelo.add_edge('Zacatecas', 'Ciudad de México', weight=5)
        elif self._vueloAICM == "g":
            g_vuelo.add_edge('AICM', 'Zacatecas', weight=3)
            g_vuelo.add_edge('Zacatecas', 'Bogotá-Colombia', weight=6)
        elif self._vueloAICM == "h":
            g_vuelo.add_edge('AICM', 'Puerto Vallarta', weight=2)
            g_vuelo.add_edge('Puerto Vallarta', 'Acapulco', weight=7)
        elif self._vueloAICM == "i":
            g_vuelo.add_edge('AICM', 'Puerto Vallarta', weight=2)
            g_vuelo.add_edge('Puerto Vallarta', 'Cancún', weight=2)
        else:
            print("La opción que elegiste no es válida.")
            return

        self.mostrar_grafo(g_vuelo, "AICM")
    def vuelosrapidos(self):
      print("A continuación necesito que de los siguientes destinos me digas a donde quieres ir,\n nosotros nos encargaremos de asignarte la ruta más rapida con respecto al tiempo diagnosticado.\n")
      self.g_mapa_rapido = nx.Graph()
      self.g_mapa_rapido.add_nodes_from(['AICM','AIFA','Monterrey','Zacatecas','Puerto Vallarta','Guadalajara','Ciudad Juárez','Bogota-Colombia','Acapulco','Cancún','Mazatlán'])
      self.g_mapa_rapido.add_edge('AICM','AIFA')
      self.g_mapa_rapido.add_edge('AICM','Zacatecas')
      self.g_mapa_rapido.add_edge('AICM','Cancún')
      self.g_mapa_rapido.add_edge('AICM','Acapulco')
      self.g_mapa_rapido.add_edge('AICM','Bogota-Colombia')
      self.g_mapa_rapido.add_edge('AICM','Ciudad Juárez')
      self.g_mapa_rapido.add_edge('AICM','Guadalajara')
      self.g_mapa_rapido.add_edge('AICM','Puerto Vallarta')
      self.g_mapa_rapido.add_edge('AIFA','Mazatlán')
      self.g_mapa_rapido.add_edge('Mazatlán','Monterrey')
      self.g_mapa_rapido.add_edge('Monterrey','Cancún')
      self.g_mapa_rapido.add_edge('Cancún','Acapulco')
      self.g_mapa_rapido.add_edge('Acapulco','Bogota-Colombia')
      self.g_mapa_rapido.add_edge('Bogota-Colombia','Ciudad Juárez')
      self.g_mapa_rapido.add_edge('Ciudad Juárez','Guadalajara')
      self.g_mapa_rapido.add_edge('Guadalajara','Puerto Vallarta')
      self.g_mapa_rapido.add_edge('Puerto Vallarta','Mazatlán')
      self.g_mapa_rapido.add_edge('AIFA','Monterrey')
      self.g_mapa_rapido.add_edge('AIFA','Puerto Vallarta')
      self.g_mapa_rapido.add_edge('AIFA','Zacatecas')
      self.g_mapa_rapido.add_edge('Zacatecas','Cancún')
      plt.gcf().canvas.manager.set_window_title("Grafo General Vuelos Rápidos")
      plt.figure(figsize=(12, 12))
      nx.draw(self.g_mapa_rapido, with_labels=True, node_color='Red',edge_color='black',node_size=1000, font_size=12)
      plt.title("Grafo General de Vuelos Rápidos\n Oziel Caballero")
      plt.show()
      self.menu_rapido()
    def menu_rapido(self):
      print("           MENÚ DE DESTINOS")
      print("           a) Monterrey")
      print("           b) Zacatecas")
      print("           c) Puerto Vallarta")
      print("           d) Guadalajara")
      print("           e) Ciudad Juárez")
      print("           f) Bogota-Colombia")
      print("           g) Acapulco")
      print("           h) Cancún")
      print("           i) Mazatlan")
      print("           j) Ciudad de México")
      print("           k) Estado de México")
      while True:
          self._vuelosrapidos = input("Con respecto al menú que te acabo de dar necesito que me des la opción\nque te interesa (a-k): ").lower()
          if self._vuelosrapidos in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]:
              break
          else:
              print("Opción inválida. Por favor, elige una letra del menú.")

      if self._vuelosrapidos == "a":
          origen = 'AICM'
          destino = 'Monterrey'
      elif self._vuelosrapidos == "b":
          origen = 'AICM'
          destino = 'Zacatecas'
      elif self._vuelosrapidos == "c":
          origen = 'AICM'
          destino = 'Puerto Vallarta'
      elif self._vuelosrapidos == "d":
          origen = 'AICM'
          destino = 'Guadalajara'
      elif self._vuelosrapidos == "e":
          origen = 'AICM'
          destino = 'Ciudad Juárez'
      elif self._vuelosrapidos == "f":
          origen = 'AICM'
          destino = 'Bogota-Colombia'
      elif self._vuelosrapidos == "g":
          origen = 'AICM'
          destino = 'Acapulco'
      elif self._vuelosrapidos == "h":
          origen = 'AICM'
          destino = 'Cancún'
      elif self._vuelosrapidos == "i":
          origen = 'AIFA' # Asumiendo que Mazatlán es más rápido desde AIFA
          destino = 'Mazatlán'
      elif self._vuelosrapidos == "j":
          print("Por favor, especifica un destino diferente a Ciudad de México para un vuelo rápido.")
          return self.menu_rapido()
      elif self._vuelosrapidos == "k":
          print("Por favor, especifica un destino diferente al Estado de México para un vuelo rápido.")
          return self.menu_rapido()
      else:
          return

      self.mostrar_ruta_en_grafo(self.g_mapa_rapido, origen, destino)


    def destinosguardados(self):
      pass

    def mostrar_grafo(self, g, aeropuerto):
      plt.figure(figsize=(5, 5))
      pos = nx.spring_layout(g)#Es para asegurarse de que los nodos en cuanto a su visualización queden bien distribuidos.
      nx.draw(g, pos, with_labels=True, arrows=True, node_color='green', edge_color='yellow',node_size=1500, font_size=12)
      edge_labels = nx.get_edge_attributes(g, 'weight')
      edge_labels = {k: f"{v} hrs" for k, v in edge_labels.items()}
      nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=8)#edge_labels=edge_labels, digamos que es un:"En el espacio que necesita la función (edge_labels), ponle lo que tengo guardado en mi cajita (edge_labels)."
      plt.title(f"Vuelo - {aeropuerto}\n Oziel Caballero")
      plt.show()


    def mostrar_rutarapida(self, g, source, target):
      try:
          ruta_corta = nx.dijkstra_path(g, source=source, target=target, weight='weight')
          print(f"Ruta más corta de {source} a {target}:", " → ".join(ruta_corta))

          aristas_en_ruta = list(zip(ruta_corta[:-1], ruta_corta[1:]))
          color_nodos = ['red' if nodo in ruta_corta else 'lightgray' for nodo in g.nodes()]

          pos = nx.spring_layout(g, seed=42)
          plt.figure(figsize=(8, 6))
          nx.draw(g, pos, with_labels=True, node_color=color_nodos,
                  edge_color='gray', node_size=2000, font_size=15, font_weight='bold')

          edge_labels = nx.get_edge_attributes(g, 'weight')
          nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

          nx.draw_networkx_edges(g, pos, edgelist=aristas_en_ruta, edge_color='red', width=4)

          plt.title(f"Grafo No Dirigido con Ruta Más Corta ({source} → {target})")
          plt.show()
      except nx.NetworkXNoPath:
          print(f"No existe una ruta entre {source} y {target}.")
      except nx.NetworkXError as e:
          print(f"Ocurrió un error al calcular la ruta: {e}")

    def mostrar_ruta_en_grafo(self, g, source, target):
      try:
          ruta_corta = nx.dijkstra_path(g, source=source, target=target, weight='weight')
          aristas_en_ruta = list(zip(ruta_corta[:-1], ruta_corta[1:]))
          color_nodos = ['lightgray'] * len(g.nodes())
          nodos_dict = {node: i for i, node in enumerate(g.nodes())}
          for nodo in ruta_corta:
              if nodo in nodos_dict:
                  color_nodos[nodos_dict[nodo]] = 'red'

          pos = nx.spring_layout(g, seed=42)
          plt.figure(figsize=(12, 12))
          nx.draw(g, pos, with_labels=True, node_color=color_nodos,
                  edge_color='black', node_size=1000, font_size=12)
          nx.draw_networkx_edges(g, pos, edgelist=aristas_en_ruta, edge_color='red', width=4)
          plt.title(f"Ruta Rápida en el Grafo General ({source} → {target})\nOziel Caballero")
          plt.show()

      except nx.NetworkXNoPath:
          print(f"No existe una ruta entre {source} y {target}.")
      except nx.NetworkXError as e:
          print(f"Ocurrió un error al calcular la ruta: {e}")

if __name__ == '__main__':
    g = Volando()
    g.presupuesto()
