# innoq-blockchain-python
playground blockchain in python


# Dependencies / Conda env

Install conda / miniconda with python 3.6. Then create env call blockchain from yaml file

`conda env create -f environment.yml`

You can choose the env 'blockchain' after creating in PyCharm. To activate it on console use:
`source activate blockchain`

# Run flask application

    export FLASK_APP=springfield_chain/web_api/api.py
    flask run