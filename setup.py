try:
    from setuptools import find_packages,setup
    import sys
except ImportError as e:
    print(e,sys)

HYPHEN_E_DOT = '-e. '
def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_Obj:
        requirements = file_Obj.readlines()
        requirements = [req.replace("\n"," ") for req in file_Obj]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
     name = "Machine Learning for predicting student performance"
    ,author = "Ayush Yajnik"
    ,author_email = "ayush.yajnik@yahoo.com"
    ,version = '0.0.1'
    ,packages = find_packages()
    ,install_requires = get_requirements('requirements.txt')

)