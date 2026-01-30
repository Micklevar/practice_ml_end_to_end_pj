from setuptools import find_packages, setup

setup(
    name = "ml_project",
    version = "0.0.1",
    author = "Alejandro Santos",
    author_email = "alejandrosantosgg1930@gmail.com",
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
)