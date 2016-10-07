init:
	pip install -r requirements.txt

pca:
	python src/hw1.py --pca --data ./diabetes.csv

kmeans:
	python src/hw1.py --kmeans --data ./diabetes.csv

clean:
	rm -f graphs/**/*.png tex/*.aux tex/*.log tex/*.synctex.gz

.PHONY: init test run clean
