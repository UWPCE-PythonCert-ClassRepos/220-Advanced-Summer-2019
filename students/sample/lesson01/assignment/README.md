To place all your files where running and testing work smoothly

1. All modules go in src
2. All tests go in tests
3. cd in to tests
4. Run with python xxx.py
5. Lint with pytest --pylint
6. test with python -m pytest -vv --cov=. ../tests/

Note - I like to import a module I have written with import modulename
Then, I call a function in that module with modulename.functionname()

More typing - yes (but your editor / IDE will help). Clearer - YES!

See examples.