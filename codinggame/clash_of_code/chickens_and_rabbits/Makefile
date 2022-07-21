test: black mypy pylint
	python -m pytest test.py

black:
	black -l 86 $$(find * -name '*.py')

mypy:
	mypy $$(find * -name '*.py') 

pylint:
	pylint $$(find * -name '*.py')
