from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='vsensortag',
    version='1.0.0',
    description='Virtual SensorTag SDK for Python3',
    long_description=readme,
    author='Taichi Souma',
    author_email='bp15046@shibaura-it.ac.jp',
    license=license,
    install_requires=[''],
    url='https://github.com/bp15046/virtual-sensortag-sdk-python3.git',
    packages = find_packages()
)