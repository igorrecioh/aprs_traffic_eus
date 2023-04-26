class Incidence:
    def __init__(self):
        self.tipo = ""
        self.autonomia = ""
        self.provincia = ""
        self.matricula = ""
        self.causa = ""
        self.poblacion = ""
        self.fechahora_ini = ""
        self.nivel = ""
        self.carretera = ""
        self.pk_inicial = ""
        self.pk_final = ""
        self.sentido = ""
        self.longitud = 0.0
        self.latitud = 0.0

    def info_msg(self):
        return self.causa + " " + self.poblacion + " " + self.carretera + " " + "Sentido: " + self.sentido