"""
Configuration module for Django Monaco Editor.
"""

from django.conf import settings

# Default settings for Monaco Editor
DEFAULTS = {
    "language": "python",
    "theme": "vs-dark",
    "height": 400,
    "width": "100%",
    "monaco_cdn_version": "0.53.0",
    "monaco_cdn_url": "https://cdn.jsdelivr.net/npm/monaco-editor@{version}/min/vs",
    "editor_options": {
        "automaticLayout": True,
        "minimap": {"enabled": True},
        "scrollBeyondLastLine": False,
        "fontSize": 14,
        "tabSize": 4,
        "wordWrap": "off",
        "lineNumbers": "on",
        "renderWhitespace": "none",
        "folding": True,
        "links": True,
        "colorDecorators": True,
    },
}


def get_config(key, default=None):
    """
    Get configuration value from Django settings or fall back to defaults.

    Usage in settings.py:
        MONACO_EDITOR_CONFIG = {
            'language': 'javascript',
            'theme': 'vs',
            'height': 500,
            'editor_options': {
                'fontSize': 16,
                'minimap': {'enabled': False},
            }
        }
    """
    monaco_settings = getattr(settings, "MONACO_EDITOR_CONFIG", {})

    if default is None:
        default = DEFAULTS.get(key)

    return monaco_settings.get(key, default)


def get_monaco_cdn_path():
    """Get the full CDN path for Monaco Editor."""
    cdn_url_template = get_config("monaco_cdn_url")
    version = get_config("monaco_cdn_version")
    return cdn_url_template.format(version=version)


def get_editor_options():
    """Get merged editor options (defaults + settings)."""
    default_options = DEFAULTS["editor_options"].copy()
    settings_options = get_config("editor_options", {})

    # Deep merge dictionaries
    return _deep_merge(default_options, settings_options)


def _deep_merge(base, override):
    """Deep merge two dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result
