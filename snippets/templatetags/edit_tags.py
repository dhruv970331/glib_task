# from ..models import Snippet
import json
from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def get_config_object(snippet):
    config = {"lineNumbers":True,"mode":snippet.language}
    if snippet.indent_mode == "tabs":
        config["indentWithTabs"] = True
        config["tabSize"] = snippet.indent_value
        return config
    config["indentWithTabs"] = False
    config["indentUnit"] = snippet.indent_value
    return mark_safe(json.dumps(config))
