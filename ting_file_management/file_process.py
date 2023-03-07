from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in instance._data:
        if item['nome_do_arquivo'] == path_file:
            print(f"Arquivo {path_file} já foi processado anteriormente")
            return

    content = txt_importer(path_file)

    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(content),
        'linhas_do_arquivo': content
    }

    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    if len(instance._data) == 0:
        print("Não há elementos", file=sys.stdout)
        return
    deleted_file = instance.dequeue()
    print(
        f"Arquivo {deleted_file['nome_do_arquivo']} removido com sucesso",
        file=sys.stdout
    )


def file_metadata(instance, position):
    if not 0 <= position < len(instance._data):
        print("Posição inválida", file=sys.stderr)
        return

    data = instance.search(position)

    print(data, file=sys.stdout)
