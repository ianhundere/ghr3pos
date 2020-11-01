import requests
import sys


class Git:
    def __init__(self, user, repo):
        self.user = user
        self.repo = repo

    def eprint(self, *args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)

    def pr_response(self):
        return requests.get(f'https://api.github.com/repos/{self.user}/{self.repo}/pulls?state=all')

    def get_pr(self):
        response = self.pr_response()
        data = response.json()
        try:
            self.process_pr(data)
        except:
            if 'Not Found' in data.values():
                self.eprint(f'\nerror: unable to retrieve pull requests because either the username, {self.user}, and/or repo, {self.repo}, do not exist.')
            elif not response:
                print(f'\n[PULLREQUEST] You\'ve hit your API rate limit, refer to https://developer.github.com/v3/#rate-limiting for more information.')

    def process_pr(self, data):
        pulls = data[0:3]
        if not pulls:
            print('\nNo pull requests available')
        elif pulls:
            print(f'\nThe last 3 pull requests for {self.user} in the {self.repo} repo are:')
            for pull in pulls:
                print('\n' + '\t' + 'Title: ' + pull['title'] + '\n\t' + 'Number: ' + str(pull['number']))

    def rel_response(self):
        return requests.get(f'https://api.github.com/repos/{self.user}/{self.repo}/releases?state=all')

    def get_rel(self):
        response = self.rel_response()
        data = response.json()
        try:
            self.process_rel(data)
        except:
            if 'Not Found' in data.values():
                self.eprint(f'\nerror: unable to retrieve releases because either the username, {self.user}, and/or repo, {self.repo}, do not exist.')
            elif not response:
                print(f'\n[RELEASE] You\'ve hit your API rate limit, refer to https://developer.github.com/v3/#rate-limiting for more information.')

    def process_rel(self, data):
        releases = data[0:3]
        if not releases:
            print('\nNo releases available')
        elif releases:
            print(f'\nThe last 3 releases/versions for {self.user} in the {self.repo} repo are:')
            for release in releases:
                print('\n' + '\t' + 'Release: ' + release['name'] + '\n\t' + 'Version: ' + release['tag_name'])
