# Ghr3pos

Get the last 3 GitHub releases and/or pull requests of a repository.
Requires the [Requests](http://docs.python-requests.org/) library. Should work on Python 3.6+.

### Features

-   Supports unathenticated requests
-   Handles edge cases such as:
    - Rate limiting
    - Non-existant user or repository
    - No available releases or pull requests

### Usage

First `pip3 install .`

General usage:

```
usage: get the last 3 GitHub releases and/or pull requests of a repository [-h] [-u USER] [-r REPO] [-R RELEASE] [-P PR]

required arguments:
  -u , --user        github username
  -r , --repo        github repository

optional arguments:
  -h, --help         show this help message and exit
  -R, --release      show last 3 github releases
  -P, --pullrequest  show last 3 github pull requests
  -v, --version      show program's version number and exit
```

Get last 3 GitHub releases:

`python3 ghr3pos.py -u <user> -r <repository> -R`

Get last 3 GitHub pull requests:

`python3 ghr3pos.py -u <user> -r <repository> -P`

Get last 3 GitHub requests and pull requests:

`python3 ghr3pos.py -u <user> -r <repository> -RP`
