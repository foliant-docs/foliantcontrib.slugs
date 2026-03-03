"""
Extension for Foliant to generate slugs.

Resolves ``!time`` YAML tag in the project config
and replaces its node value with the current local time
in format %H-%M-%S.
"""

from yaml import add_constructor
from datetime import datetime

from foliant.config.base import BaseParser


class Parser(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_constructor("!time", self._resolve_time_tag)

    def _resolve_time_tag(self, loader, node) -> str:
        current_time = datetime.now().strftime("%H-%M-%S")

        self.logger.debug(f"Resolving !time tag. Current local time: {current_time}")

        return current_time
