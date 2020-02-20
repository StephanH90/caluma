from uuid import UUID, uuid4

import pytest
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.db.utils import DataError


def test_migrate_to_flat_answers(transactional_db):
    executor = MigrationExecutor(connection)
    app = "caluma_form"
    migrate_from = [(app, "0017_auto_20190619_1320")]
    migrate_to = [(app, "0019_remove_answer_value_document")]

    executor.migrate(migrate_from)
    old_apps = executor.loader.project_state(migrate_from).apps

    # Create some old data. Can't use factories here

    Document = old_apps.get_model(app, "Document")
    Form = old_apps.get_model(app, "Form")
    Answer = old_apps.get_model(app, "Answer")
    Question = old_apps.get_model(app, "Question")
    FormQuestion = old_apps.get_model(app, "FormQuestion")

    main_form = Form.objects.create(slug="main-form")
    sub_form = Form.objects.create(slug="sub-form")

    main_form_question = Question.objects.create(
        type="form", sub_form=sub_form, slug="main-form-question"
    )
    FormQuestion.objects.create(form=main_form, question=main_form_question)

    main_text_question = Question.objects.create(type="text", slug="main-text-question")
    FormQuestion.objects.create(form=main_form, question=main_text_question)

    sub_text_question = Question.objects.create(type="text", slug="sub_1_question_1")
    FormQuestion.objects.create(form=sub_form, question=sub_text_question)

    # Note: in this step, Document.family is (historically) a UUID4 field, and
    # not yet a foreign key.
    # We need to set a temporary family, because the signals are not available...
    main_document = Document.objects.create(form=main_form, family=uuid4())
    # ... then we set the correct family
    main_document.family = main_document.pk
    main_document.save()

    sub_document = Document.objects.create(form=sub_form, family=main_document.pk)
    sub_answer = Answer.objects.create(
        value="lorem ipsum", question=sub_text_question, document=sub_document
    )
    Answer.objects.create(
        value_document=sub_document, question=main_form_question, document=main_document
    )

    text_answer = Answer.objects.create(
        value="dolor sit", question=main_text_question, document=main_document
    )

    assert not sub_answer.document == main_document
    assert text_answer.document == main_document

    # Migrate forwards.
    executor.loader.build_graph()  # reload.
    executor.migrate(migrate_to)
    new_apps = executor.loader.project_state(migrate_to).apps

    # Test the new data.
    Answer = new_apps.get_model(app, "Answer")

    sub_answer = Answer.objects.get(value="lorem ipsum")
    text_answer = Answer.objects.get(value="dolor sit")

    assert Answer.objects.filter(question__type="form").count() == 0
    assert sub_answer.document.pk == main_document.pk
    assert text_answer.document.pk == main_document.pk


def test_migrate_to_form_question_natural_key_forward(transactional_db):
    executor = MigrationExecutor(connection)
    app = "caluma_form"
    migrate_from = [(app, "0023_auto_20190729_1448")]
    migrate_to = [(app, "0024_auto_20190919_1244")]

    executor.migrate(migrate_from)
    old_apps = executor.loader.project_state(migrate_from).apps

    # Create some old data. Can't use factories here

    Form = old_apps.get_model(app, "Form")
    Question = old_apps.get_model(app, "Question")
    FormQuestion = old_apps.get_model(app, "FormQuestion")

    form_1 = Form.objects.create(slug="form-1")

    question_1 = Question.objects.create(type="text", slug="question-1")
    form_question = FormQuestion.objects.create(form=form_1, question=question_1)

    assert isinstance(form_question.pk, UUID)

    # Migrate forwards.
    executor.loader.build_graph()  # reload.
    executor.migrate(migrate_to)
    new_apps = executor.loader.project_state(migrate_to).apps

    # Test the new data.
    FormQuestion = new_apps.get_model(app, "FormQuestion")

    form_question = FormQuestion.objects.first()

    assert form_question.pk == "form-1.question-1"


def test_migrate_to_form_question_natural_key_reverse(transactional_db):
    executor = MigrationExecutor(connection)
    app = "caluma_form"
    migrate_from = [(app, "0024_auto_20190919_1244")]
    migrate_to = [(app, "0023_auto_20190729_1448")]

    executor.migrate(migrate_from)
    old_apps = executor.loader.project_state(migrate_from).apps

    # Create some old data. Can't use factories here

    Form = old_apps.get_model(app, "Form")
    Question = old_apps.get_model(app, "Question")
    FormQuestion = old_apps.get_model(app, "FormQuestion")

    form_1 = Form.objects.create(slug="form-1")

    question_1 = Question.objects.create(type="text", slug="question-1")
    FormQuestion.objects.create(form=form_1, question=question_1)

    # Migrate backwards.
    executor.loader.build_graph()  # reload.
    with pytest.raises(DataError):
        executor.migrate(migrate_to)


def test_dynamic_option_unique_together(transactional_db):
    executor = MigrationExecutor(connection)
    app = "caluma_form"
    migrate_from = [(app, "0028_auto_20200210_0929")]
    migrate_to = [(app, "0029_dynamic_option_unique_together")]

    executor.migrate(migrate_from)
    old_apps = executor.loader.project_state(migrate_from).apps

    # Create some old data. Can't use factories here

    Document = old_apps.get_model(app, "Document")
    Form = old_apps.get_model(app, "Form")
    Question = old_apps.get_model(app, "Question")
    DynamicOption = old_apps.get_model(app, "DynamicOption")
    HistoricalDynamicOption = old_apps.get_model(
        "caluma_form", "HistoricalDynamicOption"
    )

    form = Form.objects.create(slug="main-form")

    question = Question.objects.create(type="text", slug="main-form-question")

    # we need to set a temporary family, because the signals are not available
    document = Document.objects.create(form=form, family=uuid4())
    # then we set the correct family
    document.family = document.pk
    document.save()

    d_option_1 = DynamicOption.objects.create(
        document=document, question=question, slug="foo"
    )
    d_option_2 = DynamicOption.objects.create(
        document=document, question=question, slug="foo"
    )

    # again no signals
    HistoricalDynamicOption.objects.create(
        document=document,
        question=question,
        history_type="+",
        created_at=d_option_1.created_at,
        modified_at=d_option_1.modified_at,
        history_date=d_option_1.modified_at,
        slug="foo",
        id=d_option_1.pk,
    )
    HistoricalDynamicOption.objects.create(
        document=document,
        question=question,
        history_type="+",
        created_at=d_option_2.created_at,
        modified_at=d_option_2.modified_at,
        history_date=d_option_2.modified_at,
        slug="foo",
        id=d_option_2.pk,
    )

    # Migrate forwards.
    executor.loader.build_graph()  # reload.
    executor.migrate(migrate_to)
    new_apps = executor.loader.project_state(migrate_to).apps

    # Test the new data.
    DynamicOption = new_apps.get_model(app, "DynamicOption")
    HistoricalDynamicOption = new_apps.get_model(
        "caluma_form", "HistoricalDynamicOption"
    )
    Document = new_apps.get_model(app, "Document")
    Question = new_apps.get_model(app, "Question")

    document = Document.objects.get(pk=document.pk)
    question = Question.objects.get(pk=question.pk)

    assert DynamicOption.objects.get(document=document, question=question, slug="foo")
    assert (
        HistoricalDynamicOption.objects.filter(
            document=document, question=question, slug="foo"
        ).count()
        == 1
    )


def test_migrate_to_family_as_pk(transactional_db, caplog):
    """Ensure correct behaviour when moving family to PK.

    Document family may not match an existing document.
    In this case, the family should be set to their own PK.
    """
    executor = MigrationExecutor(connection)
    app = "caluma_form"
    migrate_from = [(app, "0030_auto_20200219_1359")]
    migrate_to = [(app, "0031_auto_20200220_0910")]

    executor.migrate(migrate_from)
    old_apps = executor.loader.project_state(migrate_from).apps

    OldDocument = old_apps.get_model(app, "Document")
    OldForm = old_apps.get_model(app, "Form")

    form = OldForm.objects.create(slug="form-1")

    # We don't have any signals here, so have to do it ourselves
    root_doc = OldDocument.objects.create(form=form, family=uuid4())
    root_doc.family = root_doc.pk
    root_doc.save()

    other_doc = OldDocument.objects.create(form=form, family=root_doc.pk)
    unrelated_doc = OldDocument.objects.create(form=form, family=uuid4())

    # migration should log that our unrelated_doc needs fixing
    expected_msg = (
        f"Document pk={unrelated_doc.pk} (form={form.pk}) "
        f"missing it's family={unrelated_doc.family}. "
        f"Resetting to itself"
    )

    assert isinstance(other_doc.family, UUID)

    # Migrate forwards.
    executor.loader.build_graph()  # reload.
    executor.migrate(migrate_to)

    new_apps = executor.loader.project_state(migrate_to).apps

    # Test the new data.
    NewDocument = new_apps.get_model(app, "Document")

    new_root_doc = NewDocument.objects.get(pk=root_doc.pk)
    new_other_doc = NewDocument.objects.get(pk=other_doc.pk)
    new_unrelated_doc = NewDocument.objects.get(pk=unrelated_doc.pk)

    assert new_other_doc.family == new_root_doc
    assert new_unrelated_doc.family == new_unrelated_doc
    assert new_root_doc.family == new_root_doc
    assert expected_msg in caplog.messages
