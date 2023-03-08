def exists_word(word, instance):
    result = {}

    for item in instance._data:
        nome_do_arquivo = item['nome_do_arquivo']
        linhas_do_arquivo = item['linhas_do_arquivo']

        for index, line in enumerate(linhas_do_arquivo):
            if word.lower() in line.lower():
                if nome_do_arquivo not in result:
                    result[nome_do_arquivo] = {
                        'arquivo': nome_do_arquivo,
                        'ocorrencias': [],
                        'palavra': word,
                    }
                result[nome_do_arquivo]['ocorrencias'].append({
                    'linha': index + 1
                })

    return list(result.values())


def search_by_word(word, instance):
    result = {}

    for item in instance._data:
        nome_do_arquivo = item['nome_do_arquivo']
        linhas_do_arquivo = item['linhas_do_arquivo']

        for index, line in enumerate(linhas_do_arquivo):
            if word.lower() in line.lower():
                if nome_do_arquivo not in result:
                    result[nome_do_arquivo] = {
                        'arquivo': nome_do_arquivo,
                        'ocorrencias': [],
                        'palavra': word,
                    }
                result[nome_do_arquivo]['ocorrencias'].append({
                    'conteudo': line,
                    'linha': index + 1
                })

    return list(result.values())
