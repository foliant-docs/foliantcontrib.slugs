'''
TODO
'''

import inspect
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
        node_value = node.value

        components = []

        components.append(node_value.replace(' ', '_'))

        version = self._project_config.get('version')

        if version:
            components.append(str(version))

        components.append(str(date.today()))

        slug = '-'.join(components)

        return slug
