from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


setup(
    name='day20',
    version='1.0.0',
    description='Example Package',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/tutorialmaker',
    author='Hiroki Kojima',
    packages=find_packages(),
    install_requires=['flask']
)
