'''
Extension for Foliant to generate slugs
from arbitrary lists of values.

Resolves ``!slug`` YAML tag in the project config.
Joins the values of list items into string, and appends
current date to this string.
'''

from yaml import BaseLoader, add_constructor, load
from datetime import date
from typing import Dict

from foliant.config.base import BaseParser


class Parser(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._project_config = self._get_project_config()

        add_constructor('!slug', self._resolve_slug_tag)

    def _get_project_config(self) -> Dict:
        with open(self.config_path) as project_config_file:
            project_config = {**self._defaults, **load(project_config_file, Loader=BaseLoader)}

            return project_config

    def _resolve_slug_tag(self, loader, node) -> str:
        components = loader.construct_sequence(node)

        components.append(date.today())

        return '-'.join(map(lambda component: str(component).replace(' ', '_'), components))
