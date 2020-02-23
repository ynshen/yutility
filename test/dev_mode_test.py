from yutility import DevMode
from pytest import raises


def test_DevMode_can_create():
    dev_mode = DevMode()
    with raises(ValueError):
        dev_mode = DevMode('not_exist')


def test_DevMode_can_add_path():
    dev_mode = DevMode()
    dev_mode.add_project('project1')
    with raises(NotADirectoryError):
        dev_mode.add_pkg_path(path='some/fake/path', project='project2')

    import os
    _HOME = os.getenv('HOME')
    dev_mode.add_pkg_path(path=_HOME, project='project2')

    assert 'project1' in dev_mode.pkg_path.keys()
    assert 'project2' in dev_mode.pkg_path.keys()
    assert dev_mode.pkg_path['project1'] == []
    assert dev_mode.pkg_path['project2'] == [_HOME]


def test_DevMode_can_switch_on_and_off():
    dev_mode = DevMode()
    dev_mode.add_project('project1')
    with raises(NotADirectoryError):
        dev_mode.add_pkg_path(path='some/fake/path', project='project2')
    dev_mode.on('project1')
    assert dev_mode.current_on == 'project1'
    dev_mode.off()


def test_DevMode_can_save():
    dev_mode = DevMode()
    dev_mode.add_project('project1')
    with raises(NotADirectoryError):
        dev_mode.add_pkg_path(path='some/fake/path', project='project2')
    dev_mode.on('project1')

    dev_mode.save()
