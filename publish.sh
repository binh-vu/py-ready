rm -rf build dist py_ready.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*


