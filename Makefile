install:
	python -m pip install --upgrade pip
		pip install -r requirements.txt
	
test:
	pytest

clean:
	python scripts/cleaning.py

analysis:
	python scripts/data_analysis.py

filter:
	python scripts/filtering.py



