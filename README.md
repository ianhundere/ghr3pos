# Ghr3pos
 [![Build Status](https://travis-ci.com/ianhundere/ghr3pos.svg?branch=master)](https://travis-ci.com/ianhundere/ghr3pos)[![codecov](https://codecov.io/gh/ianhundere/ghr3pos/branch/master/graph/badge.svg?token=0VN3TSJU8A)](https://codecov.io/gh/ianhundere/ghr3pos)

Get the last 3 GitHub releases and/or pull requests of a repository.
Requires the [Requests](http://docs.python-requests.org/) library. Should work on Python 3.6+.

### Features

-   Supports unathenticated requests
-   Handles edge cases such as:
    -   Rate limiting
    -   Non-existant user or repository
    -   No available releases or pull requests

### Installation

`pip3 install .`

### Usage

General usage:

```
usage: ghr3pos.py [-h] [-u USER] [-r REPO] [-R RELEASE] [-P PULLREQUEST]

Get the last 3 GitHub releases and/or pull requests of a repository.

required arguments:
  -u , --user        GitHub username
  -r , --repo        GitHub repository

possible actions (at least one is required):
  -R, --release      show last 3 GitHub releases
  -P, --pullrequest  show last 3 GitHub pull requests

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      show program's version number and exit
```

Get last 3 GitHub releases:
`python3 ghr3pos.py -u <user> -r <repository> -R`

Get last 3 GitHub pull requests:
`python3 ghr3pos.py -u <user> -r <repository> -P`

Get last 3 GitHub requests and pull requests:
`python3 ghr3pos.py -u <user> -r <repository> -RP`

##### Troubleshooting

Upgrade pip with `pip3 install -U pip` if the following error occurs:

`Directory '.' is not installable. File 'setup.py' not found.`
