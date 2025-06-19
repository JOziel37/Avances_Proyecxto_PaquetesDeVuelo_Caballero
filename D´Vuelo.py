import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
import threading
import time 

class Volando:
    def __init__(self):
        self.g = nx.DiGraph()
        self._aeropuerto = None
        self._vueloAIFA = None
        self._vueloAICM = None
        self._presupuesto = None
        self._vuelosrapidos = None
        
        self.rutas_precargadas = {} 
        self.carga_finalizada = False

        self.aifa_destinos = {
            "a": "Acapulco",
            "b": "Bogotá-Colombia",
            "c": "Ciudad Juárez",
            "d": "Monterrey",
            "e": "Ciudad de México",
            "f": "Guadalajara",
            "g": "Zacatecas",
            "h": "Puerto Vallarta",
            "i": "Mazatlán"
        }
        self.aifa_rutas = {
            "a": [('AIFA', 'Acapulco', 5)],
            "b": [('AIFA', 'Bogotá-Colombia', 3)],
            "c": [('AIFA', 'Ciudad Juárez', 6)],
            "d": [('AIFA', 'Acapulco', 5), ('Acapulco', 'Monterrey', 2)],
            "e": [('AIFA', 'Acapulco', 5), ('Acapulco', 'Ciudad de México', 3)],
            "f": [('AIFA', 'Bogotá-Colombia', 3), ('Bogotá-Colombia', 'Guadalajara', 4)],
            "g": [('AIFA', 'Bogotá-Colombia', 3), ('Bogotá-Colombia', 'Zacatecas', 1)],
            "h": [('AIFA', 'Ciudad Juárez', 6), ('Ciudad Juárez', 'Puerto Vallarta', 3)],
            "i": [('AIFA', 'Ciudad Juárez', 6), ('Ciudad Juárez', 'Mazatlán', 3)]
        }
        self.aifa_mapa_completo_aristas = [
            ('AIFA','Acapulco'), ('AIFA','Bogotá-Colombia'), ('AIFA','Ciudad Juárez'),
            ('Acapulco','Monterrey'), ('Acapulco','Ciudad de México'),
            ('Bogotá-Colombia','Guadalajara'), ('Bogotá-Colombia','Zacatecas'),
            ('Ciudad Juárez','Puerto Vallarta'), ('Ciudad Juárez','Mazatlán'),
            ('Monterrey','Ciudad de México'), ('Ciudad de México','Guadalajara'),
            ('Guadalajara','Zacatecas'), ('Zacatecas','Puerto Vallarta'),
            ('Puerto Vallarta','Mazatlán')
        ]
        self.aifa_mapa_completo_nodos = ['AIFA','Acapulco','Bogotá-Colombia','Ciudad Juárez','Monterrey','Ciudad de México','Guadalajara','Zacatecas','Puerto Vallarta','Mazatlán']


        self.aicm_destinos = {
            "a": "Monterrey",
            "b": "Zacatecas",
            "c": "Puerto Vallarta",
            "d": "Guadalajara",
            "e": "Ciudad Juárez",
            "f": "Ciudad de México",
            "g": "Bogotá-Colombia",
            "h": "Acapulco",
            "i": "Cancún"
        }
        self.aicm_rutas = {
            "a": [('AICM', 'Monterrey', 3)],
            "b": [('AICM', 'Zacatecas', 3)],
            "c": [('AICM', 'Puerto Vallarta', 2)],
            "d": [('AICM', 'Monterrey', 3), ('Monterrey', 'Guadalajara', 2)],
            "e": [('AICM', 'Monterrey', 3), ('Monterrey', 'Ciudad Juárez', 4)],
            "f": [('AICM', 'Zacatecas', 3), ('Zacatecas', 'Ciudad de México', 5)],
            "g": [('AICM', 'Zacatecas', 3), ('Zacatecas', 'Bogotá-Colombia', 6)],
            "h": [('AICM', 'Puerto Vallarta', 2), ('Puerto Vallarta', 'Acapulco', 7)],
            "i": [('AICM', 'Puerto Vallarta', 2), ('Puerto Vallarta', 'Cancún', 2)]
        }
        self.aicm_mapa_completo_aristas = [
            ('AICM','Monterrey'), ('Monterrey','Guadalajara'), ('Monterrey','Ciudad Juárez'),
            ('Guadalajara','Ciudad Juárez'), ('AICM','Zacatecas'),
            ('Zacatecas','Ciudad de México'), ('Zacatecas','Bogotá-Colombia'),
            ('Ciudad de México','Bogotá-Colombia'), ('AICM','Puerto Vallarta'),
            ('Puerto Vallarta','Acapulco'), ('Puerto Vallarta','Cancún'),
            ('Acapulco','Cancún'), ('Ciudad Juárez','Ciudad de México'),
            ('Bogotá-Colombia','Acapulco')
        ]
        self.aicm_mapa_completo_nodos = ['AICM','Monterrey','Zacatecas','Puerto Vallarta','Guadalajara','Ciudad Juárez','Ciudad de México','Bogotá-Colombia','Acapulco','Cancún']


        self.destinos_vuelos_rapidos = {
            "a": "Monterrey", "b": "Zacatecas", "c": "Puerto Vallarta",
            "d": "Guadalajara", "e": "Ciudad Juárez", "f": "Bogotá-Colombia",
            "g": "Acapulco", "h": "Cancún", "i": "Mazatlán",
            "j": "Ciudad de México", "k": "Estado de México"
        }
        self.vuelos_rapidos_mapa_aristas = [
            ('AICM','AIFA', 1), ('AICM','Zacatecas', 3), ('AICM','Cancún', 2), ('AICM','Acapulco', 2.5),
            ('AICM','Bogotá-Colombia', 5), ('AICM','Ciudad Juárez', 4), ('AICM','Guadalajara', 2),
            ('AICM','Puerto Vallarta', 2), ('AIFA','Mazatlán', 3), ('Mazatlán','Monterrey', 2.5),
            ('Monterrey','Cancún', 3.5), ('Cancún','Acapulco', 1.5), ('Acapulco','Bogotá-Colombia', 4),
            ('Bogotá-Colombia','Ciudad Juárez', 6), ('Ciudad Juárez','Guadalajara', 3),
            ('Guadalajara','Puerto Vallarta', 1.5), ('Puerto Vallarta','Mazatlán', 2),
            ('AIFA','Monterrey', 2.5), ('AIFA','Puerto Vallarta', 2.5), ('AIFA','Zacatecas', 3.5),
            ('Zacatecas','Cancún', 4)
        ]
        self.vuelos_rapidos_mapa_nodos = ['AICM','AIFA','Monterrey','Zacatecas','Puerto Vallarta','Guadalajara','Ciudad Juárez','Bogotá-Colombia','Acapulco','Cancún','Mazatlán']

        self.puntos_inicio_vuelos_rapidos = { 
            "a": 'AICM', "b": 'AICM', "c": 'AICM', "d": 'AICM', "e": 'AICM',
            "f": 'AICM', "g": 'AICM', "h": 'AICM', "i": 'AIFA' 
        }
        
        print(f'El objeto {self} ha sido creado')
        hilo_precarga = threading.Thread(target=self._precargar_datos)
        hilo_precarga.daemon = True 
        hilo_precarga.start()


    def _obtener_entrada_usuario(self, prompt, opciones_validas):
        while True:
            choice = input(prompt).lower()
            if choice in opciones_validas:
                return choice
            else:
                print("Opción inválida. Por favor, elige una de las opciones disponibles.")

    def _precargar_datos(self):
        print("\nCargando datos de vuelos en segundo plano... Por favor, espere un momento.")
        time.sleep(3) 
        
        self.carga_finalizada = True
        print("Carga de datos completada en segundo plano. ¡Listo para volar!")

    def presupuesto(self):
        while True:
            try:
                self._presupuesto = float(input("Ingrese su presupuesto: (PMX) "))
                break
            except ValueError:
                print("Ingresa un valor numérico válido para el presupuesto.")
            
        if self._presupuesto < 8364:
            self.aeropuertos()
            self.menu()
            if self._aeropuerto == "1":
                self.asignacionAIFA()
            elif self._aeropuerto == "2":
                self.asignacionAICM()
        elif self._presupuesto >= 8364:
            self.vuelosrapidos() 
        else:
            print("Ingresa caracteres válidos.")
            return self.presupuesto()

    def aeropuertos(self):
        print("En este caso tenemos dos opciones de vuelo, cada una tiene vuelos directos a ciertas\n"
              "partes en comparación con el otro, que podría tener el mismo destino pero\n"
              "quizá te pida hacer escala en otro país primero. Aunque también está la variante del horario, puede que el que haga escala salga mucho más temprano.")
        print("En cuanto a las opciones de vuelo tenemos son: \n"
              "1. Aeropuerto Internacional Felipe Ángeles (AIFA) en el Estado de México.\n"
              "2. Aeropuerto Internacional Ciudad de México (AICM) en Ciudad de México.")
        self._aeropuerto = self._obtener_entrada_usuario("Necesito que selecciones una de las dos opciones que te di (1 o 2): ", ["1", "2"])

    def menu(self):
        if self._aeropuerto == "1":
            print("Antes de enseñarte el menú de destinos en el orden en el que te los podemos ofertar, te mostraré cual es el mapa del total de recorridos programados para hoy.")
            g_mapa_aifa = nx.Graph()
            g_mapa_aifa.add_nodes_from(self.aifa_mapa_completo_nodos)
            g_mapa_aifa.add_edges_from(self.aifa_mapa_completo_aristas)
            
            plt.gcf().canvas.manager.set_window_title("Grafo General AIFA")
            plt.figure(figsize=(10, 10))
            nx.draw(g_mapa_aifa, with_labels=True, node_color='Red',edge_color='black',node_size=1000, font_size=12)
            plt.title("Grafo General de Rutas desde AIFA\n Oziel Caballero")
            plt.show()

            print("Los destinos disponibles ahora, son: ")
            for key, value in self.aifa_destinos.items():
                print(f"{key}) {value}")
            self._vueloAIFA = self._obtener_entrada_usuario("Con respecto al menú que te acabo de dar necesito que me des la opción\nque te interesa (a-i): ", list(self.aifa_destinos.keys()))
            
        elif self._aeropuerto == "2":
            print("Antes de enseñarte el menú de destinos en el orden en el que te los podemos ofertar, te mostraré cual es el mapa del total de recorridos programados para hoy.")
            g_mapa_aicm = nx.Graph()
            g_mapa_aicm.add_nodes_from(self.aicm_mapa_completo_nodos)
            g_mapa_aicm.add_edges_from(self.aicm_mapa_completo_aristas)

            plt.gcf().canvas.manager.set_window_title("Grafo General AICM")
            plt.figure(figsize=(10, 10))
            nx.draw(g_mapa_aicm, with_labels=True, node_color='Red',edge_color='black',node_size=1000, font_size=12)
            plt.title("Grafo General de Rutas desde AICM\n Oziel Caballero")
            plt.show()

            print("A CONTINUACIÓN TE MOSTRARE EL MENÚ DE DESTINOS DE EL AICM:\n")
            print("Los destinos disponibles ahora, son: ")
            for key, value in self.aicm_destinos.items():
                print(f"{key}) {value}")
            self._vueloAICM = self._obtener_entrada_usuario("Con respecto al menú que te acabo de dar necesito que me des la opción\nque te interesa (a-i): ", list(self.aicm_destinos.keys()))

    def asignacionAIFA(self):
        g_vuelo = nx.DiGraph()
        
        selected_route_edges = self.aifa_rutas.get(self._vueloAIFA)
        
        if selected_route_edges:
            for source, target, weight in selected_route_edges:
                g_vuelo.add_edge(source, target, weight=weight)
            self.mostrar_grafo(g_vuelo, "AIFA")
        else:
            print("La opción que elegiste no es válida o no tiene rutas definidas.")
            return

    def asignacionAICM(self):
        g_vuelo = nx.DiGraph()
        
        selected_route_edges = self.aicm_rutas.get(self._vueloAICM)

        if selected_route_edges:
            for source, target, weight in selected_route_edges:
                g_vuelo.add_edge(source, target, weight=weight)
            self.mostrar_grafo(g_vuelo, "AICM")
        else:
            print("La opción que elegiste no es válida o no tiene rutas definidas.")
            return

    def vuelosrapidos(self):
        print("A continuación necesito que de los siguientes destinos me digas a donde quieres ir,\n nosotros nos encargaremos de asignarte la ruta más rapida con respecto al tiempo diagnosticado.\n")
        
        self.g_mapa_rapido = nx.Graph()
        self.g_mapa_rapido.add_nodes_from(self.vuelos_rapidos_mapa_nodos)
        
        for u, v, weight in self.vuelos_rapidos_mapa_aristas:
            self.g_mapa_rapido.add_edge(u, v, weight=weight) 

        plt.gcf().canvas.manager.set_window_title("Grafo General Vuelos Rápidos")
        plt.figure(figsize=(12, 12))
        nx.draw(self.g_mapa_rapido, with_labels=True, node_color='Red',edge_color='black',node_size=1000, font_size=12)
        
        edge_labels = nx.get_edge_attributes(self.g_mapa_rapido, 'weight')
        nx.draw_networkx_edge_labels(self.g_mapa_rapido, nx.spring_layout(self.g_mapa_rapido), edge_labels=edge_labels)
        
        plt.title("Grafo General de Vuelos Rápidos\n Oziel Caballero")
        plt.show()
        
        self.menu_rapido() 

    def menu_rapido(self):
        print("           MENÚ DE DESTINOS")
        for key, value in self.destinos_vuelos_rapidos.items():
            print(f"           {key}) {value}")
        
        self._vuelosrapidos = self._obtener_entrada_usuario("Con respecto al menú que te acabo de dar necesito que me des la opción\nque te interesa (a-k): ", list(self.destinos_vuelos_rapidos.keys()))
        
        destino_elegido = self.destinos_vuelos_rapidos.get(self._vuelosrapidos)

        if destino_elegido == "Ciudad de México":
            print("Por favor, especifica un destino diferente a Ciudad de México para un vuelo rápido.")
            return self.menu_rapido()
        elif destino_elegido == "Estado de México":
            print("Por favor, especifica un destino diferente al Estado de México para un vuelo rápido.")
            return self.menu_rapido()
        
        origen = self.puntos_inicio_vuelos_rapidos.get(self._vuelosrapidos)
        destino = destino_elegido

        if origen and destino:
            self.mostrar_ruta_en_grafo(self.g_mapa_rapido, origen, destino)
        else:
            print("No se pudo determinar el origen o destino para el vuelo rápido. Intenta de nuevo.")

    def destinosguardados(self):
        pass 

    def mostrar_grafo(self, g, aeropuerto):
        plt.figure(figsize=(5, 5))
        pos = nx.spring_layout(g)
        nx.draw(g, pos, with_labels=True, arrows=True, node_color='green', edge_color='yellow',node_size=1500, font_size=12)
        edge_labels = nx.get_edge_attributes(g, 'weight')
        edge_labels = {k: f"{v} hrs" for k, v in edge_labels.items()}
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=8)
        plt.title(f"Vuelo - {aeropuerto}\n Oziel Caballero")
        plt.show()

    def mostrar_rutarapida(self, g, source, target):
        try:
            ruta_corta = nx.dijkstra_path(g, source=source, target=target, weight='weight')
            total_weight = nx.dijkstra_path_length(g, source=source, target=target, weight='weight')
            print(f"Ruta más corta de {source} a {target}:", " → ".join(ruta_corta))
            print(f"Tiempo total estimado: {total_weight} horas")

            aristas_en_ruta = list(zip(ruta_corta[:-1], ruta_corta[1:]))
            color_nodos = ['red' if nodo in ruta_corta else 'lightgray' for nodo in g.nodes()]

            pos = nx.spring_layout(g, seed=42)
            plt.figure(figsize=(8, 6))
            nx.draw(g, pos, with_labels=True, node_color=color_nodos,
                     edge_color='gray', node_size=2000, font_size=15, font_weight='bold')

            edge_labels = nx.get_edge_attributes(g, 'weight')
            nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

            nx.draw_networkx_edges(g, pos, edgelist=aristas_en_ruta, edge_color='red', width=4)

            plt.title(f"Grafo No Dirigido con Ruta Más Corta ({source} → {target})\n Oziel Caballero")
            plt.show()
        except nx.NetworkXNoPath:
            print(f"No existe una ruta entre {source} y {target}.")
        except nx.NetworkXError as e:
            print(f"Ocurrió un error al calcular la ruta: {e}")

    def mostrar_ruta_en_grafo(self, g, source, target):
        try:
            ruta_corta = nx.dijkstra_path(g, source=source, target=target, weight='weight')
            total_weight = nx.dijkstra_path_length(g, source=source, target=target, weight='weight')
            print(f"Ruta más corta de {source} a {target}:", " → ".join(ruta_corta))
            print(f"Tiempo total estimado: {total_weight} horas")

            aristas_en_ruta = []
            for i in range(len(ruta_corta) - 1):
                u, v = ruta_corta[i], ruta_corta[i+1]
                if g.has_edge(u, v):
                    aristas_en_ruta.append((u,v))
                elif g.has_edge(v, u): 
                    aristas_en_ruta.append((v,u))
            
            color_nodos = ['lightgray'] * len(g.nodes())
            nodos_list = list(g.nodes()) 
            for nodo in ruta_corta:
                if nodo in nodos_list:
                    color_nodos[nodos_list.index(nodo)] = 'red'

            pos = nx.spring_layout(g, seed=42)
            plt.figure(figsize=(12, 12))
            nx.draw(g, pos, with_labels=True, node_color=color_nodos,
                     edge_color='black', node_size=1000, font_size=12)
            
            edge_labels = nx.get_edge_attributes(g, 'weight')
            nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=8)

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
