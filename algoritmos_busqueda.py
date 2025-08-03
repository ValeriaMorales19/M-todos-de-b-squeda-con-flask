def busqueda_secuencial(lista, valor):
    resultados = []
    comparaciones = 0
    for i, v in enumerate(lista):
        comparaciones += 1
        estado = 'Revisado'
        if v == valor:
            resultados.append({'indice': i, 'valor': v, 'estado': '¡Encontrado!'})
            break
        else:
            resultados.append({'indice': i, 'valor': v, 'estado': estado})
    return resultados, comparaciones

def busqueda_binaria(lista, valor):
    resultados = []
    comparaciones = 0
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        if lista[medio] == valor:
            for i in range(len(lista)):
                if i == medio:
                    resultados.append({'indice': i, 'valor': lista[i], 'estado': '¡Encontrado!'})
                elif izquierda <= i <= derecha:
                    resultados.append({'indice': i, 'valor': lista[i], 'estado': 'Revisado'})
                else:
                    resultados.append({'indice': i, 'valor': lista[i], 'estado': 'No revisado'})
            break
        elif lista[medio] < valor:
            for i in range(izquierda, medio+1):
                resultados.append({'indice': i, 'valor': lista[i], 'estado': 'Revisado'})
            izquierda = medio + 1
        else:
            for i in range(medio, derecha+1):
                resultados.append({'indice': i, 'valor': lista[i], 'estado': 'Revisado'})
            derecha = medio - 1
    if not any(r['estado'] == '¡Encontrado!' for r in resultados):
        resultados = [{'indice': i, 'valor': v, 'estado': 'No revisado'} for i, v in enumerate(lista)]
    return resultados, comparaciones