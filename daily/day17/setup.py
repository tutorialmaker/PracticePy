from setuptools import setup


setup(name='day17',
      version='1.0.0',
      description='Example Package',
      url='https://github.com/tutorialmaker/PracticePy',
      author='Hiroki Kojima',
      packages=['day17', 'day17.tests'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      )
