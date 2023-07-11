def normalize_characters(xmlFileNameIn, xmlFileNameOut):
    with open(xmlFileNameIn, 'r') as file:
        data = file.read()
        data = data.replace('í', 'i')
        data = data.replace('Á', 'A')
        data = data.replace('Ó', 'O')
  
    with open(xmlFileNameOut, 'w') as file:
        file.write(data)
    