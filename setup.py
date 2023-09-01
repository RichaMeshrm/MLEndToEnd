from setuptools import find_packages,setup #to create package of the ML project
from typing import List

hypen_e="-e ."
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() 
        #as there will be new line in requirements.txt
        requirements = [req.replace("\n","") for req in requirements]

        if hypen_e in requirements:
            requirements.remove(hypen_e)
    return requirements
setup(
    name='MLPROJECT',
    version='0.0.1',
    author='Richa',
    author_email='meshramricha@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt') 
    # install_requires = ['pandas','seaborn','numpy'] this is not dynamic as we make require multiple packages
    
)