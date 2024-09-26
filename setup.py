from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements

setup(
    name='Diamond Price Prediction',
    version= '0.0.1',
    author= 'vivek saroj',
    author_email= 'viveksaroj098@gmail.com',
    description='Used to predict price of diamond in open market',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)