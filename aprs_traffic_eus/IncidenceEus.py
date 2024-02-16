class IncidenceEus:
    def __init__(self, 
                 tipo, 
                 autonomia, 
                 provincia, 
                 matricula, 
                 causa, 
                 poblacion,
                 fechahora_ini,
                 nivel,
                 carretera,
                 pk_inicial,
                 pk_final,
                 sentido,
                 longitud,
                 latitud):
        self.tipo = tipo
        self.autonomia = autonomia
        self.provincia = provincia
        self.matricula = matricula
        self.causa = causa
        self.poblacion = poblacion
        self.fechahora_ini = fechahora_ini
        self.nivel = nivel
        self.carretera = carretera
        self.pk_inicial = pk_inicial
        self.pk_final = pk_final
        self.sentido = sentido
        self.longitud = longitud
        self.latitud = latitud

    def info_msg(self):
        return self.causa + " " + self.poblacion + " " + self.carretera + " " + "Sentido: " + self.sentido