init:
	pip install -r requirements.txt

test:
	nosetests tests --all-modules -v

run: clean
	python src/hw1.py -r -s --data ./diabetes.csv

clean:
	rm -f graphs/**/*.png tex/*.aux tex/*.log tex/*.synctex.gz tex/*.pdf

.PHONY: init test run clean
