from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='bonjour_monde',
      version='0.1',
      description='A skeleton python package',
      long_description=readme(),
      url='http://github.com/stephengaw/bonjour-monde',
      author='Stephen Gaw',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=[],
      zip_safe=False
      )
