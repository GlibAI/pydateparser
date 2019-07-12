from io import open

from setuptools import find_packages, setup

with open('pydateparser/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = []

setup(
    name='pydateparser',
    version=version,
    description='date and time parsing library.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='glib.ai',
    author_email='',
    maintainer='Samit Shah',
    maintainer_email='samit@glib.ai',
    url='https://github.com/GLibAi/pydateparser',
    license='MIT',

    keywords=[
        'date', 'time', 'datetime', 'parser'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
)
