def imprimirdicionario(lista_de_erros):
    for key, value in lista_de_erros.items():
        for item in value:
            print(f'Imprimindo dict: {item} - {key}')

def validar_numero(campo_mensagem, valor, lista_de_erros):
    for letra in valor:
        if letra.isdigit():
            print('antes de validar')
            imprimirdicionario(lista_de_erros)
            lista_de_erros[campo_mensagem].append('Campo não pode conter números')   
            break

def validar_origem_destino_iguais(campo_mensagem, origem, destino, lista_de_erros):
    imprimirdicionario(lista_de_erros)
    print('antes destino')
    if origem == destino:                      
            lista_de_erros[campo_mensagem].append('Origem e destino são iguais')    