"""Provides an easy way to configure git username on a per repository basis.
"""
from setuptools import setup, find_packages
import glob
import os.path


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)


setup(
    name='ws.gitpersona',
    version='1.0',

    install_requires=[
        'setuptools',
    ],

    entry_points={
        'console_scripts': [
            'git-persona = ws.gitpersona.persona:main'
        ],
    },

    author='Wolfgang Schnerring <wosc@wosc.de>',
    author_email='wosc@wosc.de',
    license='BSD',
    url='https://github.com/wosc/git-persona/',

    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.txt',
        'CHANGES.txt',
    )),

    namespace_packages=['ws'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    data_files=[('', glob.glob(project_path('*.txt')))],
    zip_safe=False,
)
