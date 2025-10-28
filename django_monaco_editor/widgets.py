"""
Monaco Editor widget for Django forms.
"""

import json

from django import forms
from django.utils.safestring import mark_safe

from . import conf


class MonacoEditorWidget(forms.Textarea):
    """
    A widget that renders Monaco Editor instead of a standard textarea.

    Args:
        attrs: Standard widget attributes (id, class, etc.)
        language: Programming language for syntax highlighting (default from settings)
        theme: Editor theme ('vs', 'vs-dark', 'hc-black')
        height: Editor height in pixels or CSS value
        width: Editor width in CSS value
        readonly: Whether the editor should be read-only
        editor_options: Additional Monaco editor options
    """

    template_name = "django_monaco_editor/monaco_widget.html"

    def __init__(
        self, attrs=None, language=None, theme=None, height=None, width=None, readonly=False, editor_options=None
    ):
        super().__init__(attrs)

        # Get values from settings if not provided
        self.language = language or conf.get_config("language")
        self.theme = theme or conf.get_config("theme")
        self.height = height or conf.get_config("height")
        self.width = width or conf.get_config("width")
        self.readonly = readonly

        # Merge editor options: defaults <- settings <- custom
        self.editor_options = conf.get_editor_options()
        if editor_options:
            self.editor_options = conf._deep_merge(self.editor_options, editor_options)

    def get_context(self, name, value, attrs):
        """Build context for template rendering."""
        context = super().get_context(name, value, attrs)

        # Configuration for Monaco Editor
        monaco_config = {
            "language": self.language,
            "theme": self.theme,
            "value": value or "",
            "readOnly": self.readonly,
            **self.editor_options,
        }

        # Add serialized config to context
        context["widget"]["monaco_config"] = mark_safe(json.dumps(monaco_config))
        context["widget"]["monaco_cdn_path"] = conf.get_monaco_cdn_path()
        context["widget"]["editor_height"] = self._format_size(self.height)
        context["widget"]["editor_width"] = self._format_size(self.width)

        return context

    def _format_size(self, size):
        """Format size value to CSS-compatible string."""
        if isinstance(size, int):
            return f"{size}px"
        return str(size)

    @property
    def media(self):
        """
        Media class for Django Admin.
        Monaco Editor is loaded via CDN in the template.
        """
        return forms.Media(css={"all": ()}, js=())
