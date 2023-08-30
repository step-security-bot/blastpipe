"""
This type stub file was generated by pyright.
"""

import re
from typing import Any, List, Optional, Protocol, TypeVar

from . import PYMAJOR, PYMINOR
from .mixin import Mixin

"""Backports starting from Python 3.9"""

class IsTemplatePre311(Protocol):
    """Protocol to check if a Template is pre-3.11"""

    delimiter: str
    idpattern: str
    braceidpattern: Optional[str]
    flags: int
    pattern: re.Pattern[str]
    template: str
    def safe_substitute(self: Any) -> Optional[str]:
        """Abstract method to be implemented by base"""
        ...
    def substitute(self: Any) -> Optional[str]:
        """Abstract method to be implemented by base"""
        ...

T = TypeVar('T', bound='string.Template')  # type: ignore[name-defined]

class TemplateGetIdentifiersMixin(Mixin[Any]):
    """Example Template mixin with preferred way of typing and using mixins"""

    delimiter: str
    idpattern: str
    braceidpattern: Optional[str]
    flags: int
    pattern: re.Pattern[str]
    template: str
    def safe_substitute(self: object) -> Optional[str]:
        """Abstract method to be implemented by base"""
        ...
    def substitute(self: object) -> Optional[str]:
        """Abstract method to be implemented by base"""
        ...
    def get_identifiers(self: IsTemplatePre311) -> List[str]:
        """Mixin method get_identifiers for older Template pre-3.11"""
        ...
    @classmethod
    def extend_with(cls: type[IsTemplatePre311], instance: T) -> T:
        """Extend the class with the mixin instance."""
        ...

if PYMAJOR >= 3 and PYMINOR < 11:
    Template = ...
else:
    Template = ...
