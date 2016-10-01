init:
	pip install -r requirements.txt

test:
	nosetests tests --all-modules -v

run: clean
	python hw1.py

clean:
	rm -f graphs/**/*.png tex/*.aux tex/*.log tex/*.synctex.gz tex/*.pdf

.PHONY: init test run clean
