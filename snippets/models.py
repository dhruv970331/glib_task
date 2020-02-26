from django.db import models
# from pygments import highlight
# from pygments.formatters.html import HtmlFormatter
# from pygments.lexers import get_all_lexers, get_lexer_by_name
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

LANGUAGE_CHOICES = sorted([("python","python"),("javascript","javascript"),("clike","text/x-java"),("clike","c/c++")])
INDENT_CHOICES = [(2,2),(4,4),(8,8)]
INDTENT_MODE_CHOICES = [("tabs","Tabs"),("spaces","Spaces")]

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=50)
    indent_value = models.PositiveIntegerField(default=2,choices=INDENT_CHOICES)
    indent_mode = models.CharField(max_length=10,choices=INDTENT_MODE_CHOICES,default="spaces")
    code = models.TextField()
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    owner = models.ForeignKey(
        'accounts.User', related_name='snippets', on_delete=models.CASCADE)
    private = models.BooleanField()
    class Meta:
        ordering = ('created', )
        unique_together = ('owner','name')

