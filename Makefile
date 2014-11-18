VIRTUALENV?=virtualenv
REACTOR?=default

.PHONY: all env

PROJECT="foo bar"

all     : ; @echo building project '${PROJECT}' for development...

run     : ; @echo running project '${PROJECT}' for development...

dist    : ; @echo building project '${PROJECT}' for production...

install : ; @echo installing project '${PROJECT}' dependencies...; pip install -r requirements.txt --no-index --find-links file://packages

update : ; @echo updating project '${PROJECT}' dependencies...; pip install --upgrade --force-reinstall -r requirements.txt --no-index --find-links file://packages

bundle  : ; @echo not available

clean   : ; @echo removing files $1...

test    : ; @echo running tests...

env:
	$(VIRTUALENV) --no-site-packages env/
	env/bin/pip install -r requirements.txt --use-mirrors
