# innoq-blockchain-python

playground blockchain in Python


# Dependencies / Conda env

Install conda / miniconda with Python 3.6. Then create an environment called "blockchain" from the YAML file:

```
$ conda env create -f environment.yml
```

You can then select the "blockchain" environment in PyCharm. To activate it on console use:

```
$ . activate blockchain
```


# Tests

Using [pytest](https://pytest.org):

```
$ py.test -s --tb=short test
```
