import Incidence
from tabulate import tabulate


class XmlManager:
    def __init__(self, xml_object):
        self.xml_object = xml_object
        self.count_xml = 0
        self.count_today = 0
        self.count_filtered = 0
        self.list_of_incidences = []
        self.data_to_be_printed = []

    def get_xml_incidences(self):
        return self.count_xml
    
    def get_today_incidences(self):
        return self.count_today
    
    def get_filtered_incidences(self):
        return self.count_filtered
    
    def print_filtered_incidences(self):
        print(tabulate(
            self.data_to_be_printed, 
            headers=["Fecha/hora", "Tipo", "Causa", "Carretera", "Longitud", "Latitud", "Sentido"]
            )
            )

    def filter_incidences(self, today_date):
        for incidencia in self.xml_object.raiz.children:
            if today_date in incidencia.fechahora_ini.cdata:
                if "Desconocida" != incidencia.causa.cdata:
                    ind = Incidence.Incidence(
                        incidencia.tipo.cdata,
                        incidencia.autonomia.cdata,
                        incidencia.provincia.cdata,
                        incidencia.matricula.cdata,
                        incidencia.causa.cdata,
                        incidencia.poblacion.cdata,
                        incidencia.fechahora_ini.cdata,
                        incidencia.nivel.cdata,
                        incidencia.carretera.cdata,
                        incidencia.pk_inicial.cdata,
                        incidencia.pk_final.cdata,
                        incidencia.sentido.cdata,
                        incidencia.longitud.cdata,
                        incidencia.latitud.cdata,
                    )
                    prov_data = []
                    prov_data.append(incidencia.fechahora_ini.cdata)
                    prov_data.append(incidencia.tipo.cdata)
                    prov_data.append(incidencia.causa.cdata)
                    prov_data.append(incidencia.carretera.cdata)
                    prov_data.append(incidencia.longitud.cdata)
                    prov_data.append(incidencia.latitud.cdata)
                    prov_data.append(incidencia.sentido.cdata)
                    self.data_to_be_printed.append(prov_data)
                    self.list_of_incidences.append(ind)
                    self.count_filtered+=1
                self.count_today+=1
            self.count_xml+=1
        return self.list_of_incidences