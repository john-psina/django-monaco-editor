# Django Monaco Editor

Integration of Monaco Editor (VSCode's code editor) for Django forms and admin.

## 🚀 Features

- **Easy Integration**: Simply use `MonacoField` instead of `TextField`
- **Flexible Configuration**: Programming language, themes, sizes, editor options
- **Settings Support**: Global configuration via settings.py
- **CDN Loading**: Package stays lightweight
- **Multiple Editors**: Works with multiple editors on the same page
- **Django Admin Integration**: Support for inline forms and dynamic forms
- **Automatic Layout**: Adapts to window resizing

## 📦 Installation

Install the package from PyPI:

```bash
pip install django-monaco-editor
```

Add `django_monaco_editor` to `INSTALLED_APPS` in `settings.py`:

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'django.contrib.admin',
    # ...
    'django_monaco_editor',
]
```

## 🎯 Basic Usage

### In Models

```python
# myapp/models.py
from django.db import models
from django_monaco_editor.fields import MonacoField

class Snippet(models.Model):
    title = models.CharField(max_length=200)

    # Simple Python code (uses default settings)
    python_code = MonacoField(blank=True)

    # JSON with light theme
    config_json = MonacoField(
        language='json',
        theme='vs',
        blank=True,
        help_text="Enter configuration in JSON format"
    )
    
    # JavaScript with custom settings
    js_code = MonacoField(
        language='javascript',
        theme='vs-dark',
        height=600,
        editor_options={
            'fontSize': 16,
            'minimap': {'enabled': False},
            'wordWrap': 'on'
        }
    )

    def __str__(self):
        return self.title
```

### Register in Django Admin

```python
# myapp/admin.py
from django.contrib import admin
from .models import Snippet

admin.site.register(Snippet)
```

## ⚙️ Configuration in settings.py

You can set global configuration for all Monaco editors:

```python
# settings.py

MONACO_EDITOR_CONFIG = {
    # Default programming language
    'language': 'python',
    
    # Editor theme: 'vs', 'vs-dark', 'hc-black'
    'theme': 'vs-dark',
    
    # Editor dimensions
    'height': 400,  # pixels or CSS value like '100%'
    'width': '100%',
    
    # Monaco Editor CDN version
    'monaco_cdn_version': '0.53.0',
    
    # Custom CDN URL (optional)
    'monaco_cdn_url': 'https://cdn.jsdelivr.net/npm/monaco-editor@{version}/min/vs',
    
    # Monaco Editor options
    'editor_options': {
        'automaticLayout': True,
        'fontSize': 14,
        'tabSize': 4,
        'wordWrap': 'off',
        'lineNumbers': 'on',
        'minimap': {
            'enabled': True
        },
        'scrollBeyondLastLine': False,
        'renderWhitespace': 'none',
        'folding': True,
        'links': True,
        'colorDecorators': True,
    }
}
```

## 🎨 MonacoField Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `language` | `str` | `'python'` | Programming language for syntax highlighting |
| `theme` | `str` | `'vs-dark'` | Editor theme: `'vs'`, `'vs-dark'`, `'hc-black'` |
| `height` | `int` or `str` | `400` | Editor height (in pixels or CSS) |
| `width` | `int` or `str` | `'100%'` | Editor width (in pixels or CSS) |
| `readonly` | `bool` | `False` | Whether the editor is read-only |
| `editor_options` | `dict` | `{}` | Additional Monaco Editor options |

### Supported Languages

Monaco Editor supports many programming languages:

`python`, `javascript`, `typescript`, `json`, `html`, `css`, `scss`, `less`, `xml`, `markdown`, `sql`, `shell`, `bash`, `powershell`, `yaml`, `dockerfile`, `go`, `rust`, `java`, `c`, `cpp`, `csharp`, `php`, `ruby`, `swift`, `kotlin`, and many more.

## 📚 Usage Examples

### Different Programming Languages

```python
class CodeSnippet(models.Model):
    python_code = MonacoField(language='python')
    javascript_code = MonacoField(language='javascript')
    html_code = MonacoField(language='html')
    css_code = MonacoField(language='css')
    json_config = MonacoField(language='json')
    sql_query = MonacoField(language='sql')
```

### Custom Sizes

```python
class Document(models.Model):
    # Large editor
    content = MonacoField(height=800, width='100%')
    
    # Small editor
    note = MonacoField(height=200)
```

### Additional Editor Options

```python
class Settings(models.Model):
    config = MonacoField(
        language='json',
        editor_options={
            'fontSize': 16,
            'wordWrap': 'on',
            'minimap': {'enabled': False},
            'lineNumbers': 'off',
            'glyphMargin': False,
            'folding': False,
            'lineDecorationsWidth': 0,
            'lineNumbersMinChars': 0
        }
    )
```

### Read-Only Mode

```python
class Log(models.Model):
    log_content = MonacoField(
        readonly=True,
        theme='vs',
        height=600
    )
```

## 🔧 Using the Widget Directly

You can also use the widget directly in forms:

```python
from django import forms
from django_monaco_editor.widgets import MonacoEditorWidget

class CodeForm(forms.Form):
    code = forms.CharField(
        widget=MonacoEditorWidget(
            language='python',
            theme='vs-dark',
            height=500
        )
    )
```


## 📄 License

MIT License