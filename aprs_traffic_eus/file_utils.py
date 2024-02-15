def normalize_characters(xmlFileNameIn, xmlFileNameOut):
    with open(xmlFileNameIn, 'r') as file:
        data = file.read()
        
        data = data.replace('Á', 'A')
        data = data.replace('É', 'E')
        data = data.replace('Í', 'I')
        data = data.replace('Ó', 'O')
        data = data.replace('Ú', 'U')
        data = data.replace('á', 'a')
        data = data.replace('é', 'e')
        data = data.replace('í', 'i')
        data = data.replace('ó', 'o')
        data = data.replace('ú', 'u')
        data = data.replace('ñ', 'n')
  
    with open(xmlFileNameOut, 'w') as file:
        file.write(data)
    