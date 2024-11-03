from setuptools import setup, find_packages

setup(
    name='nature-explorers',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'transformers',
        'scikit-fuzzy',
        # add any other dependencies
    ],
    entry_points={
        'console_scripts': [
            'nature-explorers=app:main',
        ],
    },
)
