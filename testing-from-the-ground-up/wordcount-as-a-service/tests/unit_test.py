import pytest

from app.word_counter import find_top_word

# Recall function being tested...
# def find_top_word(words: List[str]) -> Tuple[str, int]:
#     """Return top word and number of occurrences"""
#     word_counter = Counter(words)
#     return word_counter.most_common(1)[0]


@pytest.mark.talk_run
def test_find_top_word():
    words = ["foo", "bar", "bat", "baz", "foo", "baz", "foo"]

    result = find_top_word(words)

    assert result[0] == "foo"
    assert result[1] == 3
