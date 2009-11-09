from django import forms
from django.utils.translation import ungettext, ugettext_lazy as _
from django.contrib.comments.forms import CommentForm

class CommentFormWithHelp(CommentForm):
    url           = forms.URLField(label=_("Site"), required=False)
    email         = forms.EmailField(label=_("Email address"),
                                    help_text=_("will not be displayed"))

