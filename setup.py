from setuptools import setup, find_packages


def requirements(filename='requirements.txt'):
    return open(filename.strip()).readlines()


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='lxml-xpath-ipaddress',
    version='0.2.0',
    url='https://github.com/jeremyschulman/junospyez-ossh-server',
    description='LXML xpath extension library for ipaddress',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='jschulman@juniper.net',
    packages=find_packages(),
    install_requires=requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
