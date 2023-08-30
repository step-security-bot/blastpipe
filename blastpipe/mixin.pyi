"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from . import public

"""Mixin ABC, Generic, and helper function."""

@public
class BaseMixin(ABC):
    """Abstract mixin class"""

    @classmethod
    @abstractmethod
    def extend_with(cls: Any, instance: Any) -> Any:
        """extend the instance with the mixin cls"""
        ...

_T = TypeVar('_T', bound='BaseMixin')

@public
class Mixin(Generic[_T], BaseMixin):  # type: ignore[misc]
    """Generic mixin class"""

    ...

@public
def mixin(cls: Any, base: Any) -> Any:
    """Helper function to extend the class with the base"""
    ...
