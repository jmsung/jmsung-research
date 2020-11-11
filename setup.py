from setuptools import setup

setup(
    name='jmsung-research',
    version='0.1',
    description='jmsung-research for utils, studies and projects',
    url='http://github.com/jmsung/jmsung-research',
    author='Jongmin Sung',
    author_email='jongmin.sung@gmail.com',
    packages=['utils'],
    install_requires=[
        'docopt',
        'tables',
        'pathlib',
        'ipdb',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'snek = utils.test.snek:main',
        ]
    }
)
