'''
Extension for Foliant to generate slugs
from arbitrary lists of values.

Resolves ``!slug`` YAML tag in the project config.

Replaces the list of values after the ``!slug`` tag with
the string that joins these values using ``-`` delimeter.
Spaces in values are replaced with underscores.
'''

from yaml import add_constructor, load

from foliant.config.base import BaseParser


class Parser(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_constructor('!slug', self._resolve_slug_tag)

    def _resolve_slug_tag(self, loader, node) -> str:
        components = loader.construct_sequence(node)

        self.logger.debug(f'Resolving !slug tag. Custom slug components: {components}')

        return '-'.join(map(lambda component: str(component).replace(' ', '_'), components))
