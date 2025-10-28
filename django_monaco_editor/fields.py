"""
Custom Django model fields with Monaco Editor widget.
"""
from django.db import models
from .widgets import MonacoEditorWidget


class MonacoField(models.TextField):
    """
    A TextField that renders with Monaco Editor in forms and Django Admin.
    
    Args:
        language: Programming language for syntax highlighting (e.g., 'python', 'javascript', 'json')
        theme: Editor theme ('vs', 'vs-dark', 'hc-black')
        height: Editor height in pixels or CSS value
        width: Editor width in CSS value
        readonly: Whether the editor should be read-only
        editor_options: Additional Monaco editor options as a dictionary
        
    Example:
        class MyModel(models.Model):
            code = MonacoField(
                language='python',
                theme='vs-dark',
                height=600,
                editor_options={'fontSize': 16}
            )
    """
    
    def __init__(self, *args, **kwargs):
        # Extract Monaco-specific parameters
        self.language = kwargs.pop('language', None)
        self.theme = kwargs.pop('theme', None)
        self.height = kwargs.pop('height', None)
        self.width = kwargs.pop('width', None)
        self.readonly = kwargs.pop('readonly', False)
        self.editor_options = kwargs.pop('editor_options', None)
        
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        """
        Override the default widget with MonacoEditorWidget.
        """
        # First, get the form field from parent
        formfield = super().formfield(**kwargs)
        
        # Then override its widget with MonacoEditorWidget
        formfield.widget = MonacoEditorWidget(
            language=self.language,
            theme=self.theme,
            height=self.height,
            width=self.width,
            readonly=self.readonly,
            editor_options=self.editor_options
        )
        
        return formfield
    
    def deconstruct(self):
        """
        Support for Django migrations.
        """
        name, path, args, kwargs = super().deconstruct()
        
        # Add Monaco-specific parameters to kwargs for migrations
        if self.language is not None:
            kwargs['language'] = self.language
        if self.theme is not None:
            kwargs['theme'] = self.theme
        if self.height is not None:
            kwargs['height'] = self.height
        if self.width is not None:
            kwargs['width'] = self.width
        if self.readonly:
            kwargs['readonly'] = self.readonly
        if self.editor_options is not None:
            kwargs['editor_options'] = self.editor_options
            
        return name, path, args, kwargs