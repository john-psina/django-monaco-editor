"""
Django Monaco Editor - Monaco Editor integration for Django forms and admin.
"""

__version__ = "1.1.1"

from .fields import MonacoField
from .widgets import MonacoEditorWidget

__all__ = ["MonacoField", "MonacoEditorWidget"]
