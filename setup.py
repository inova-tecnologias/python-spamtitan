import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='python-spamtitan',
    version='1.0.0a1',
    packages=['spamtitan'],
    include_package_data=True,
    license='Apache License',
    description='Python classes to access Spamtitan API.',
    long_description=README,
    url='https://github.com/inova-tecnologias/python-spamtitan',
    author='Fernando Cainelli',
    author_email='fernando.cainelli@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache License',        
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries'
    ],
)