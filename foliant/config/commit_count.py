'''
Extension for Foliant to return number of commits in current git repo.

Resolves ``!commit_count`` YAML tag in the project config.
'''

from yaml import add_constructor
from subprocess import run, PIPE

from foliant.config.base import BaseParser


class Parser(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_constructor('!commit_count', self._resolve_commit_count_tag)

    def _check_git(self):
        '''True if current folder is a git repository. False otherwise'''
        r = run(['git', 'status'], stdout=PIPE, stderr=PIPE)
        if r.returncode == 128:  # not a git repository
            return False
        elif r.returncode == 0:
            return True
        else:
            raise RuntimeError(r.stderr.decode())

    def _get_commit_count(self, branch: str = ''):
        '''
        Run git rev-list --count command to get the number of commits in
        current repository. If branch param is not specified — returns
        number of commits in current branch. If is specified — number of
        commits in branch branch.
        '''
        if not self._check_git():
            self.logger.debug('Not a git repository. Returning 0 commit count.')
            return 0
        rev = branch if branch else 'HEAD'
        command = f'git rev-list --count {rev}'
        result = run(command, shell=True, stdout=PIPE, stderr=PIPE)
        if result.returncode != 0:
            err = result.stderr.decode()
            self.logger.debug(f'Failed while to run command: {command}\n{err}')
            return 0
        return int(result.stdout.decode())

    def _resolve_commit_count_tag(self, loader, node) -> str:
        '''
        Resolve the !commit_count yaml tag. This tag accepts up to 2 arguments:
        - branch_name — name of the branch to count commits in
        - correction — positive or negative number to adjust the result
        '''
        args = loader.construct_scalar(node).split()
        if len(args) > 2:
            raise ValueError("Up to 2 arguments are allowed: branch and/or commit correction")
        branch = ''
        correction = 0
        for arg in args:
            try:
                correction = int(arg)
            except ValueError:
                branch = arg
        commit_count = self._get_commit_count(branch)
        self.logger.debug(f'Resolving !commit_count tag. Factual commit count in branch {branch}: {commit_count}.\n'
                          f'Correction to be applied: {correction}')
        return commit_count + correction
