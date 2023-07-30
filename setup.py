import os
from subprocess import check_call

from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        # os.system("python -m spacy download en_core_web_trf")

setup(
    name='word_processor',
    version='0.0.3',
    packages=find_packages(),
    url='',
    license='',
    author='nikatlas',
    author_email='nikatlas@gmail.com',
    description='Variable name generator',
    install_requires=[
        'spacy',
        'nltk',
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)
