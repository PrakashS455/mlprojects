from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    """
    This function reads the requirements file and returns a list of packages.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    
    # Remove any leading/trailing whitespace characters and empty lines
    requirements = [req.strip() for req in requirements if req.strip()]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='prakash',
    author_email='prakashakash212@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'))



  
