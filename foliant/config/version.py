'''
Extension for Foliant to generate version string
from arbitrary lists of values.

Resolves ``!version`` YAML tag in the project config.

Replaces the list of values after the ``!version`` tag with
the string that joins these values using ``.`` delimeter.
'''

from yaml import add_constructor

from foliant.config.base import BaseParser


class Parser(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_constructor('!version', self._resolve_version_tag)

    def _resolve_version_tag(self, loader, node) -> str:
        components = loader.construct_sequence(node)

        self.logger.debug(f'Resolving !version tag. Custom version components: {components}')

        return '.'.join(str(c) for c in components)
