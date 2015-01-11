from ws.gitpersona.persona import cmd
import os
import pytest
import ws.gitpersona.persona


@pytest.fixture(scope='session')
def personas(request):
    cmd('git config --global persona.testhome'
        ' "First Last <home@example.com>"')
    cmd('git config --global persona.testwork'
        ' "First Last <work@example.com>"')

    def teardown():
        cmd('git config --global --unset persona.testhome')
        cmd('git config --global --unset persona.testwork')
    request.addfinalizer(teardown)


@pytest.fixture
def repository(request, tmpdir):
    cwd = os.getcwd()
    request.addfinalizer(lambda: os.chdir(cwd))
    os.chdir(str(tmpdir))
    cmd('git init')


def test_list_personas(personas):
    personas = ws.gitpersona.persona.list_personas()
    assert personas['testhome'] == {
        'name': 'First Last', 'email': 'home@example.com'}
    assert personas['testwork'] == {
        'name': 'First Last', 'email': 'work@example.com'}


def test_set_persona(repository):
    ws.gitpersona.persona.set_persona(
        {'name': 'First Last', 'email': 'home@example.com'})
    assert 'First Last' == cmd('git config user.name')
    assert 'home@example.com' == cmd('git config user.email')
