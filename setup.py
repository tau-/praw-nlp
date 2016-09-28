from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='praw-nlp',
    version='0.0.1',
    author='Alex Troesch',
    author_email='ajtroesch@gmail.com',
    packages=find_packages(exclude=['docs']),
    url='https://github.com/tau-/praw-nlp',
    license='MIT',
    description='Scrape Reddit and classify text.',
    long_description=long_description,
    install_requires=[
    ]
)
