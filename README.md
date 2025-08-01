```bash
# run all tests
pytest

# run test with mark slow
pytest -m slow

# run tests with the mark regression
pytest -m regression

# run tets that are expected to fail
pytest -m xfail

#  run tests that are not marked as expected to fail
pytest -m "not xfail"

```