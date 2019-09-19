import pytest

from models.trie import Trie

__words = ["book", "bookcase", "booking", "booklet", "bookshelf", "boost",
           "boot", "booth", "border", "bore", "boring", "born", "borrow"]


@pytest.fixture(scope="module")
def trie_provider():
    trie = Trie()
    trie.insert_list(__words)

    return trie


def test__find_operation(trie_provider):
    trie = trie_provider

    assert trie.find('book')
    assert trie.find('booklet')

    assert not trie.find('boo')
    assert not trie.find('bor')
