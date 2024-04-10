from django import template


register = template.Library()


bad_words = ['дурак','дед','критика','редиска','ЛГБТ','text','2']


@register.filter()
def wordchange(text):
   return ' '.join(['*' * len(i) if i in bad_words else i for i in text.split()])
