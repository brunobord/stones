help:
	@echo "Help on Makefile"
	@echo
	@echo " * wordcount: count words - uses pandoc"
	@echo " * install: set the builder environment up."
	@echo " * html: build the html page in docs/"

install:
	virtualenv venv
	venv/bin/pip install markdown

wordcount: stones.md
	@pandoc -f markdown -t plain stones.md | wc -w

html: stones.md templates/base.html
	venv/bin/python scripts/build.py