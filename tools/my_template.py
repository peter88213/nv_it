"""Provide a custom Template class that accepts spaces in placeholders."""
from string import Template


class MyTemplate(Template):

    idpattern = r'(?a:[\.\:_ a-z][\.\:_ a-z0-9]*)'

