import re


def snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def camel_case(name):
    return "".join((p.title() if i else p) for i, p in enumerate(name.split("_")))
