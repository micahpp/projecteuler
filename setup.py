from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='projec teuler',
      version='0.1.0',
      description='A package containing my solutions for Project Euler (see https://projecteuler.net)',
      long_description=readme,
      author='micah paul',
      url='https://github.com/micahpp/projecteuler',
      license=license,
      packages=find_packages(exclude=('tests', 'data'))
      )
