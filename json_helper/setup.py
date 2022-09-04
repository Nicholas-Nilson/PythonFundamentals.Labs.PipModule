from setuptools import setup

setup(
    name='json_helper',
    version='0.1.0',
    description='A tool to import NOAA Location JSON responses to Pandas DataFrames',
    url='https://github.com/Nicholas-Nilson/PythonFundamentals.Labs.PipModule',
    author='Nicholas Nilson',
    license='LICENSE.rst',
    readme='README.md',
    packages=['json_helper'],
    install_requires=['pandas'
                      ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
