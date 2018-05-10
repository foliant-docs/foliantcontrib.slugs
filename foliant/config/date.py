'''
Extension for Foliant to generate slugs.

Resolves ``!date`` YAML tag in the project config
and replaces its node value with the current local date.
'''

from yaml import add_constructor, load
from datetime import date

from foliant.config.base import BaseParser


class Parser(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_constructor('!date', self._resolve_date_tag)

    def _resolve_date_tag(self, loader, node) -> str:
        current_date = str(date.today())

        self.logger.debug(f'Resolving !date tag. Current local date: {current_date}')

        return current_date
