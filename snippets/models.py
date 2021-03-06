from django.contrib.admin import options
from django.db import models
from django.conf import settings
from pygments import formatter, highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0])for item in LEXERS])
STYLE_CHOICES = sorted([(item, item)for item in get_all_styles()])


class Snippet(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='snippets', 
        related_query_name='snippet',
        on_delete=models.CASCADE,
        )
    highlighted = models.TextField(default='')
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        max_length=100,
        default='python',
        choices=LANGUAGE_CHOICES,
    )
    style = models.CharField(
        max_length=100,
        default='friendly',
        choices=STYLE_CHOICES,
    )


    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else{}
        formatter = HtmlFormatter(
            style=self.style, 
            linenos=linenos, 
            full=True,
            **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
