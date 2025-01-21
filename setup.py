from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """_summary_
    This function will return list of pakages that are required for project

    Args:
        file_path (str): File path for requirement.txt

    Returns:
        List[str]: its will have list of pakage names
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements
    
setup(
    name='mlProject',
    version='0.0.1',
    author='Shivam Gupta',
    author_email='sg9967780426@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)