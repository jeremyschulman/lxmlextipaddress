
PROJECT=$(shell python setup.py --name)
PROJECT_VERSION=$(shell python setup.py --version)
SOURCEDIR=$(subst -,_,$(PROJECT))
SOURCES=$(shell find $(SOURCEDIR) -name '*.py')

all:
	python setup.py sdist bdist_wheel

develop:
	python setup.py develop

clean:
	python setup.py clean
	rm -rf *.egg-info/ build/ dist/
	find . -name '*.pyc' -print | xargs rm


