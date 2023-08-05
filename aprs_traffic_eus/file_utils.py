def normalize_characters(xmlFileNameIn, xmlFileNameOut):
    with open(xmlFileNameIn, 'r') as file:
        data = file.read()
        data = data.replace('í', 'i')
        data = data.replace('Á', 'A')
        data = data.replace('Ó', 'O')
        data = data.replace('Ú', 'U')
        data = data.replace('ú', 'u')
  
    with open(xmlFileNameOut, 'w') as file:
        file.write(data)
    