import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    first_mock = {
        "nome_do_arquivo": "statics/novo_paradigma_globalizado-min.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": ["linhas"],
    }
    second_mock = {
        "nome_do_arquivo": "statics/arquivo_teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["linhas"],
    }

    priority_queue = PriorityQueue()

    with pytest.raises(IndexError):
        priority_queue.search(-1)

    priority_queue.enqueue(first_mock)
    priority_queue.enqueue(second_mock)
    assert len(priority_queue) == 2

    priority_queue.enqueue(first_mock)
    assert priority_queue.search(0) == second_mock
    assert priority_queue.search(1) == first_mock

    priority_queue.dequeue()
    assert len(priority_queue) == 2
