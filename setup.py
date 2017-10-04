from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='repository_template',
      version='0.1',
      description='Template for a minimal python repository file structure',
      long_description=readme(),
      url='http://github.com/BramVermaas/repository_template',
      author='Bram Vermaas',
      author_email='amavermaas@gmail.com',
      packages=find_packages(exclude=('tests', 'docs')),
      include_package_data=True,
      test_suite='nose2.collector.collector',
      tests_require=['nose2'])