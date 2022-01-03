# ----------------------------------
#          TEST
# ----------------------------------

test:
	@coverage run -m  pytest tests/*.py
	@coverage report -m --skip-empty --omit='*__init__*'

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr owlapp-*.dist-info
	@rm -fr owlapp.egg-info

install:
	@pip install . -U

# ----------------------------------
#             API
# ----------------------------------

run_api:
	uvicorn owlapp.fast:app --reload
