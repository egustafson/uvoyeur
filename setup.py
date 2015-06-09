## setuptools

from setuptools import setup, find_packages

setup(
    name = "uvoyeur",
    version = "0.1",
    author = "Eric Gustafson",
    author_email = "ericg-git@elfwerks.org",
    license = "Apache Software License",
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
    ],

    entry_points = {
        'console_scripts': [
            'uvoyeurd = uvoyeur.daemon:run'
        ],
    },
)
