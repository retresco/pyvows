vows test:
	@env PYTHONPATH=. python pyvows/console.py --cover --cover_package=pyvows --cover_package=pyvows.assertions --cover_threshold=80.0 tests/

setup:
	@pip install --requirement=REQUIREMENTS

publish:
	python setup.py sdist upload
