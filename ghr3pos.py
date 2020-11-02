#!/usr/bin/env python3
import argparse
from git import Git
import sys

__version__ = '0.1.0'

# disables default help
parser = argparse.ArgumentParser(description='Get the last 3 GitHub releases and/or pull requests of a repository.',
    usage='%(prog)s [-h] [-u USER] [-r REPO] [-R RELEASE] [-P PULLREQUEST]', add_help=False)
required = parser.add_argument_group('required arguments')
one_or_both = parser.add_argument_group('possible actions (at least one is required)')
optional = parser.add_argument_group('optional arguments')
# adds help back
optional.add_argument(
    '-h',
    '--help',
    action='help',
    default=argparse.SUPPRESS,
    help='show this help message and exit'
)

required.add_argument('-u', '--user', required=True,
                        help='GitHub username', metavar='')
required.add_argument('-r', '--repo', required=True,
                        help='GitHub repository', metavar='')
one_or_both.add_argument('-R', '--release', action='store_const', const=Git.get_rel,
                        help='show last 3 GitHub releases')
one_or_both.add_argument('-P', '--pullrequest', action='store_const', const=Git.get_pr,
                        help='show last 3 GitHub pull requests')
optional.add_argument('-v', '--version', action='version',
                        version=f'%(prog)s (version {__version__})')

def main(args=None):
    parsed = parser.parse_args(args=args)
    git = Git(user=parsed.user, repo=parsed.repo)
    if parsed.pullrequest:
        git.get_pr()
    if parsed.release:
        git.get_rel()
    if not parsed.release and not parsed.pullrequest:
        parser.error('no --release (-R) or --pullrequest (-P) flag given.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
