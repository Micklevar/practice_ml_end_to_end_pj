from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]: #file_path:str = requirements.txt
    """
    Esta funcion regresa la lista de requirements
    """
    requirements=[] #Lista vacia que se llenara con las librerias de requirements
    with open(file_path) as file_obj: #Toma la direccion de file_path y abre el archivo para leerlo
        requirements=file_obj.readlines() #Se toma el valor de cada linea y se almacena en la lista
        [req.replace("\n","")for req in requirements] #Se quita el \n de los valores, ("pandas\n" -> "pandas")

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup( #Metadatos de instalacion
    name = "ml_project",
    version = "0.0.1",
    author = "Alejandro Santos",
    author_email = "alejandrosantosgg1930@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)