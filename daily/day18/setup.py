from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()


setup(name='day18',
      version='1.0.0',
      description='Example Package',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/tutorialmaker/PracticePy',
      author='Hiroki Kojima',
      packages=find_packages(),
      include_package_data=True,
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      install_requires=['flask',
                        'python-dotenv',
                        'numpy'],
      )
