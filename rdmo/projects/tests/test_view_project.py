import os

import pytest
from django.urls import reverse
from rdmo.views.models import View

from ..models import Project

users = (
    ('owner', 'owner'),
    ('manager', 'manager'),
    ('author', 'author'),
    ('guest', 'guest'),
    ('user', 'user'),
    ('anonymous', None),
)

status_map = {
    'list': {
        'owner': 200, 'manager': 200, 'author': 200, 'guest': 200, 'user': 200, 'anonymous': 302,
    },
    'detail': {
        'owner': 200, 'manager': 200, 'author': 200, 'guest': 200, 'user': 403, 'anonymous': 302
    },
    'create_get': {
        'owner': 200, 'manager': 200, 'author': 200, 'guest': 200, 'user': 200, 'anonymous': 302
    },
    'create_post': {
        'owner': 302, 'manager': 302, 'author': 302, 'guest': 302, 'user': 302, 'anonymous': 302
    },
    'update_get': {
        'owner': 200, 'manager': 200, 'author': 403, 'guest': 403, 'user': 403, 'anonymous': 302
    },
    'update_post': {
        'owner': 302, 'manager': 302, 'author': 403, 'guest': 403, 'user': 403, 'anonymous': 302
    },
    'delete_get': {
        'owner': 200, 'manager': 403, 'author': 403, 'guest': 403, 'user': 403, 'anonymous': 302
    },
    'delete_post': {
        'owner': 302, 'manager': 403, 'author': 403, 'guest': 403, 'user': 403, 'anonymous': 302
    },
    'export': {
        'owner': 200, 'manager': 403, 'author': 403, 'guest': 403, 'user': 403, 'anonymous': 302
    },
    'import': {
        'owner': 302, 'manager': 302, 'author': 302, 'guest': 302, 'user': 302, 'anonymous': 302
    },
    'import_error': {
        'owner': 400, 'manager': 400, 'author': 400, 'guest': 400, 'user': 400, 'anonymous': 302
    }
}

urlnames = {
    'list': 'projects',
    'detail': 'project',
    'create': 'project_create',
    'update': 'project_update',
    'delete': 'project_delete'
}


export_formats = ('rtf', 'odt', 'docx', 'html', 'markdown', 'tex', 'pdf')

project_pk = 1


@pytest.mark.parametrize('username,password', users)
def test_list(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse(urlnames['list'])
    response = client.get(url)
    assert response.status_code == status_map['list'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_detail(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse(urlnames['detail'], args=[project_pk])
    response = client.get(url)
    assert response.status_code == status_map['detail'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_create_get(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse(urlnames['create'])
    response = client.get(url)
    assert response.status_code == status_map['create_get'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_create_post(db, client, username, password):
    client.login(username=username, password=password)
    project = Project.objects.get(pk=project_pk)

    url = reverse(urlnames['create'])
    data = {
        'title': 'A new project',
        'description': 'Some description',
        'catalog': project.catalog.pk
    }
    response = client.post(url, data)
    assert response.status_code == status_map['create_post'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_update_get(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse(urlnames['update'], args=[project_pk])
    response = client.get(url)
    assert response.status_code == status_map['update_get'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_update_post(db, client, username, password):
    client.login(username=username, password=password)
    project = Project.objects.get(pk=project_pk)

    url = reverse(urlnames['update'], args=[project_pk])
    data = {
        'title': project.title,
        'description': project.description,
        'catalog': project.catalog.pk
    }
    response = client.post(url, data)
    assert response.status_code == status_map['update_post'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_delete_get(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse(urlnames['delete'], args=[project_pk])
    response = client.get(url)
    assert response.status_code == status_map['delete_get'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_delete_update_post(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse(urlnames['delete'], args=[project_pk])
    response = client.post(url)
    assert response.status_code == status_map['delete_post'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_export_xml(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_export_xml', args=[project_pk])
    response = client.get(url)
    assert response.status_code == status_map['export'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_export_csv(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_export_csv', args=[project_pk, 'csv'])
    response = client.get(url)
    assert response.status_code == status_map['export'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_export_csvsemicolon(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_export_csv', args=[project_pk, 'csvsemicolon'])
    response = client.get(url)
    assert response.status_code == status_map['export'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_import_get(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_import')
    response = client.get(url)
    assert response.status_code == status_map['import'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_import_post(db, settings, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_import')
    xml_file = os.path.join(settings.BASE_DIR, 'xml', 'project.xml')
    with open(xml_file, encoding='utf8') as f:
        response = client.post(url, {'uploaded_file': f})
    assert response.status_code == status_map['import'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_import_empty_post(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_import')
    response = client.post(url)
    assert response.status_code == status_map['import'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_import_error_post(db, settings, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_import')
    xml_file = os.path.join(settings.BASE_DIR, 'xml', 'error.xml')
    with open(xml_file, encoding='utf8') as f:
        response = client.post(url, {'uploaded_file': f})
    assert response.status_code == status_map['import_error'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_answers(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_answers', args=[project_pk])
    response = client.get(url)
    assert response.status_code == status_map['detail'][username], response.content


@pytest.mark.parametrize('username,password', users)
@pytest.mark.parametrize('export_format', export_formats)
def test_project_answers_export(db, client, username, password, export_format):
    client.login(username=username, password=password)

    url = reverse('project_answers_export', args=[project_pk, export_format])
    response = client.get(url)
    assert response.status_code == status_map['detail'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_view(db, client, username, password):
    client.login(username=username, password=password)
    views = View.objects.all()

    for view in views:
        url = reverse('project_view', args=[project_pk, view.pk])
        response = client.get(url)
        assert response.status_code == status_map['detail'][username], response.content


@pytest.mark.parametrize('username,password', users)
@pytest.mark.parametrize('export_format', export_formats)
def test_project_view_export(db, client, username, password, export_format):
    client.login(username=username, password=password)
    views = View.objects.all()

    for view in views:
        url = reverse('project_view_export', args=[project_pk, view.pk, export_format])
        response = client.get(url)
        assert response.status_code == status_map['detail'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_questions(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_questions', args=[project_pk])
    response = client.get(url)
    assert response.status_code == status_map['detail'][username], response.content


@pytest.mark.parametrize('username,password', users)
def test_project_error(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse('project_error', args=[project_pk])
    response = client.get(url)
    assert response.status_code == status_map['detail'][username], response.content
