import pytest
from lesson_09.database import SessionLocal, Subject


@pytest.fixture(scope="function")
def db_session():
    session = SessionLocal()
    session.begin_nested()
    try:
        yield session
    finally:
        session.rollback()
        session.close()


def test_add_subject(db_session):
    new_subject = Subject(
        subject_id=99999, subject_title="Автоматизация тестирования"
    )
    db_session.add(new_subject)
    db_session.commit()

    db_subject = (
        db_session.query(Subject).filter_by(subject_id=99999).first()
    )
    assert db_subject is not None
    assert db_subject.subject_title == "Автоматизация тестирования"


def test_update_subject(db_session):
    subject = Subject(subject_id=99998, subject_title="Временная Математика")
    db_session.add(subject)

    subject.subject_title = "Высшая математика"
    db_session.commit()

    updated_subject = (
        db_session.query(Subject).filter_by(subject_id=99998).first()
    )
    assert updated_subject.subject_title == "Высшая математика"


def test_delete_subject(db_session):
    subject = Subject(subject_id=99997, subject_title="Физика для теста")
    db_session.add(subject)
    db_session.commit()

    db_session.delete(subject)
    db_session.commit()

    deleted_subject = (
        db_session.query(Subject).filter_by(subject_id=99997).first()
    )
    assert deleted_subject is None
