from git import Git
import ghr3pos
import pytest
import sys
import subprocess
import types


@pytest.mark.vcr()
def test_main(capsys):
    assert ghr3pos.main(
        ['--user=britannic', '--repo=blacklist', '--release', '--pullrequest']) == 0
    assert capsys.readouterr() == ('\nThe last 3 pull requests for britannic in the blacklist repo are:\n\n\tTitle: Update README.md\n\tNumber: 18\n\n\tTitle: Updated script referenced in build\n\tNumber: 17\n\n\tTitle: Corrected script name referenced\n\tNumber: 16\n\nThe last 3 releases/versions for britannic in the blacklist repo are:\n\n\tRelease: Release 1.2.4.2 (August 14, 2020)\n\tVersion: v1.2.4.2\n\n\tRelease: Release 1.2.4.1 (August 10, 2020)\n\tVersion: v1.2.4.1\n\n\tRelease: Release 1.2.4.0 (August 9, 2020)\n\tVersion: v1.2.4.0\n', '')


@pytest.mark.vcr()
def test_main_user_not_found(capsys):
    assert ghr3pos.main(
        ['--user=ianfundere', '--repo=rpi-k3s', '--pullrequest']) == 0
    assert capsys.readouterr() == (
        '', '\nerror: unable to retrieve pull requests because either the username, ianfundere, and/or repo, rpi-k3s, do not exist.\n')


@pytest.mark.vcr()
def test_main_repo_not_found(capsys):
    assert ghr3pos.main(
        ['--user=ianhundere', '--repo=lauper', '--release']) == 0
    assert capsys.readouterr() == (
        '', '\nerror: unable to retrieve releases because either the username, ianhundere, and/or repo, lauper, do not exist.\n')


@pytest.mark.vcr()
def test_main_no_rel(capsys):
    assert ghr3pos.main(
        ['--user=ianhundere', '--repo=ran-jam', '--release']) == 0
    assert capsys.readouterr() == ('\nNo releases available\n', '')


@pytest.mark.vcr()
def test_main_no_pr(capsys):
    assert ghr3pos.main(
        ['--user=ianhundere', '--repo=scales-o-rama', '--pullrequest']) == 0
    assert capsys.readouterr() == ('\nNo pull requests available\n', '')


@pytest.mark.vcr()
def test_main_pr_ratelimited(capsys):
    assert ghr3pos.main(
        ['--user=ianhundere', '--repo=scales-o-rama', '--pullrequest']) == 0
    assert capsys.readouterr() == (
        '\n[PULLREQUEST] You\'ve hit your API rate limit, refer to https://developer.github.com/v3/#rate-limiting for more information.\n', '')


@pytest.mark.vcr()
def test_main_rel_ratelimited(capsys):
    assert ghr3pos.main(
        ['--user=ianhundere', '--repo=scales-o-rama', '--release']) == 0
    assert capsys.readouterr() == (
        '\n[RELEASE] You\'ve hit your API rate limit, refer to https://developer.github.com/v3/#rate-limiting for more information.\n', '')


def test_main_no_flags(capsys):
    with pytest.raises(SystemExit) as exc_info:
        ghr3pos.main(['--user=ianhundere', '--repo=scales-o-rama'])
    assert exc_info.value.args == (2,)
    assert capsys.readouterr() == (
        '', 'usage: ghr3pos.py [-h] [-u USER] [-r REPO] [-R RELEASE] [-P PULLREQUEST]\nghr3pos.py: error: no --release (-R) or --pullrequest (-P) flag given.\n')


def test_main_exit(capsys):
    v = subprocess.run(
        [sys.executable, '-m', ghr3pos.__name__],
        encoding='utf8',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    assert v.returncode == 2
    assert v.stdout == ''
    assert v.stderr == 'usage: ghr3pos.py [-h] [-u USER] [-r REPO] [-R RELEASE] [-P PULLREQUEST]\nghr3pos.py: error: the following arguments are required: -u/--user, -r/--repo\n'
