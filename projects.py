import os
import json
import logging
from operator import itemgetter

from urllib.request import urlopen
from urllib.request import HTTPError


from pelican import signals

from github import Github



class GithubProjects(object):

    def __init__(self, gen):
        github = Github(os.getenv('GITHUB_TOKEN'))
        self.named_user = github.get_user(gen.settings['GITHUB_USER'])
        self.repos = self.named_user.get_repos(sort='pushed')

    def process(self):
        return [
            r for r in self.repos if not r.private and not r.fork
        ]

def initialize(gen):
    if not 'GITHUB_USER' in gen.settings.keys():
        logger.warning('GITHUB_USER not set')
    else:
        gen.plugin_instance = GithubProjects(gen)
        gen.context['github_projects'] = gen.plugin_instance.process()


def register():
    signals.generator_init.connect(initialize)
