#!/usr/bin/env python
from string import Template
from os.path import dirname, abspath, join
import markdown

root = abspath(dirname(__file__))
template_dir = join(root, '..', 'templates')
target_dir = join(root, '..', 'docs')

if __name__ == '__main__':
    with open(join(template_dir, 'base.html')) as fd:
        template = Template(fd.read())

    with open(join(root, '..', 'stones.md')) as fd:
        raw = fd.read()
        marked = markdown.markdown(raw, output_format='html5')

    with open(join(target_dir, 'index.html'), 'w') as fd:
        fd.write(template.substitute(body=marked))
