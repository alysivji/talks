import pytest

from app.main import db, save_to_db, TopWord

# Recall function being tested...
# def save_to_db(url: str, top_word: Tuple[str, int]) -> None:
#     record = TopWord()
#     record.url = url
#     record.word = top_word[0]
#     record.num_occurrences = top_word[1]

#     db.session.add(record)
#     db.session.commit()

#     db.session.refresh(record)
#     return record


@pytest.mark.talk_run
def test_save_to_db():
    # Arrange
    url = "http://test_url.com"
    most_common_word_details = ("Python", 42)

    savepoint = db.session.begin_nested()
    db.session.begin_nested()

    # Act
    word = save_to_db(url, most_common_word_details)

    # Assert
    inserted_record = TopWord.query.get(word.id)
    assert inserted_record.url == "http://test_url.com"
    assert inserted_record.word == "Python"
    assert inserted_record.num_occurrences == 42

    savepoint.rollback()


@pytest.mark.debug_example
@pytest.mark.skip
def test_drop_to_pdb():
    # Arrange
    url = "http://test_url.com"
    most_common_word_details = ("Python", 42)

    savepoint = db.session.begin_nested()
    db.session.begin_nested()

    # Act
    word = save_to_db(url, most_common_word_details)

    # Assert
    inserted_record = TopWord.query.get(word.id)
    assert inserted_record.url != "http://test_url.com"  # this is False
    assert inserted_record.word != "Python"  # this is False
    assert inserted_record.num_occurrences is None  # this is False

    savepoint.rollback()
