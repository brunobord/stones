VENV=./venv
VENV_BIN=$(VENV)/bin

help:
	@echo "Help on Makefile"
	@echo
	@echo " * wordcount: count words - uses pandoc"
	@echo " * install: set the builder environment up."
	@echo " * html: build the html pages in docs/"
	@echo " * serve: serve the docs/ directory"

install:
	virtualenv --python=python3.8 venv
	$(VENV_BIN)/pip install markdown

wordcount: v1/stones.md v2/stones.md
	@echo "stones-v1" `pandoc -f markdown -t plain v1/stones.md | wc -w`
	@echo "stones-v2" `pandoc -f markdown -t plain v2/stones.md | wc -w`

html: v1/stones.md v2/stones.md templates/base.html
	mkdir -p docs/v2/ docs/v1
	$(VENV_BIN)/python scripts/build.py

serve:
	cd docs; ../$(VENV_BIN)/python -m http.server
