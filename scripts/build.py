#!/usr/bin/env python
from string import Template
from os.path import dirname, abspath, join
from codecs import open
import markdown

root = abspath(dirname(__file__))
template_dir = join(root, '..', 'templates')
target_dir = join(root, '..', 'docs')

if __name__ == '__main__':
    with open(join(template_dir, 'base.html')) as fd:
        template = Template(fd.read())

    PATHS = (
        ('v1', 'stones.md'),
        ('v2', 'stones.md'),
        ('.', 'README.md'),
    )

    for source_dir, filename in PATHS:
        source_path = join(root, '..', source_dir, filename)
        target_path = join(target_dir, source_dir, 'index.html')
        with open(source_path, encoding="utf") as fd:
            raw = fd.read()
            marked = markdown.markdown(raw, output_format='html5')

        with open(target_path, 'w', encoding="utf") as fd:
            fd.write(template.substitute(body=marked))
