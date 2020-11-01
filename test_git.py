from git import Git
import ghr3pos
import pytest
import sys
import json
import types

with open('pulls.json') as f:
  pr_data = json.load(f)
with open('releases.json') as f:
  rel_data = json.load(f)

def test_sanity():
  assert True is True

@pytest.mark.vcr()
def test_main(capsys):
    assert ghr3pos.main(types.SimpleNamespace(user="britannic", repo="blacklist", pullrequest=True, release=True)) is None
    assert capsys.readouterr() == ('\nThe last 3 pull requests for britannic in the blacklist repo are:\n\n\tTitle: Update README.md\n\tNumber: 18\n\n\tTitle: Updated script referenced in build\n\tNumber: 17\n\n\tTitle: Corrected script name referenced\n\tNumber: 16\n\nThe last 3 releases/versions for britannic in the blacklist repo are:\n\n\tRelease: Release 1.2.4.2 (August 14, 2020)\n\tVersion: v1.2.4.2\n\n\tRelease: Release 1.2.4.1 (August 10, 2020)\n\tVersion: v1.2.4.1\n\n\tRelease: Release 1.2.4.0 (August 9, 2020)\n\tVersion: v1.2.4.0\n','')

def test_process_pr(capsys):
    user = 'britannic'
    repo = 'blacklist'
    git = Git(user, repo)
    data = pr_data
    git.process_pr(data)
    captured = capsys.readouterr()
    assert captured.out.startswith(f'\nThe last 3 pull requests for {user} in the {repo} repo are:\n')

def test_process_rel(capsys):
    user = 'britannic'
    repo = 'blacklist'
    git = Git(user, repo)
    data = rel_data
    git.process_rel(data)
    captured = capsys.readouterr()
    assert captured.out.startswith(f'\nThe last 3 releases/versions for {user} in the {repo} repo are:\n')
