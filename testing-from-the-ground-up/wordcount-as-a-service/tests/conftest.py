from app.main import db, TopWord

import pytest


@pytest.fixture(scope="function")
def persisted_word():
    savepoint = db.session.begin_nested()
    db.session.begin_nested()

    word = TopWord(**{
        "url": "http://test_url.com",
        "word": "python",
        "num_occurrences": 42,
    })
    db.session.add(word)
    db.session.commit()
    db.session.refresh(word)

    yield word

    savepoint.rollback()
