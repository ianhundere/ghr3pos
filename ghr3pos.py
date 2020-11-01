#!/usr/bin/env python3
from argparse import ArgumentParser, SUPPRESS
from git import Git

__version__ = '0.1.0'


def main(args):
    args.git = Git(args.user, args.repo)
    if args.pullrequest:
        args.git.get_pr()
    if args.release:
        args.git.get_rel()
    if not args.release and not args.pullrequest:
        parser.error('no --release (-R) or --pullrequest (-P) flag given.')


if __name__ == '__main__':
    # disables default help
    parser = ArgumentParser(description='Get the last 3 GitHub releases and/or pull requests of a repository.',
        usage='%(prog)s [-h] [-u USER] [-r REPO] [-R RELEASE] [-P PR]', add_help=False)
    required = parser.add_argument_group('required arguments')
    one_or_both = parser.add_argument_group('possible actions (at least one is required)')
    optional = parser.add_argument_group('optional arguments')
    # adds help back
    optional.add_argument(
        '-h',
        '--help',
        action='help',
        default=SUPPRESS,
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
    args = parser.parse_args()
    main(args)
