from setuptools import setup

setup(
    # Needed to silence warnings
    name='Measurements',
    url='https://github.com/rodelafue/package_demo',
    author='Rodrigo De la Fuente',
    author_email='radelafu@udec.edu',
    # Needed to actually package something
    packages=['measure'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.5',
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.rst').read(),
    # if there are any scripts
    scripts=['scripts/hello.py'],
)