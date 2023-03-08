def exists_word(word, instance):
    result = []

    for item in instance._data:
        nome_do_arquivo = item['nome_do_arquivo']
        linhas_do_arquivo = item['linhas_do_arquivo']

        for index, line in enumerate(linhas_do_arquivo):
            if word.lower() in line.lower():
                if not any(
                    item['arquivo'] == nome_do_arquivo
                    for item in result
                ):
                    result.append({
                        'palavra': word,
                        'arquivo': nome_do_arquivo,
                        'ocorrencias': [{'linha': index + 1}]
                    })
                result[nome_do_arquivo].append({'linha': index + 1})

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
