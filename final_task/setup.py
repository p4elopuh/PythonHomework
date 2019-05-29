import setuptools


setuptools.setup(
    name="pycalc",
    version="0.1",
    author="Tatsiana Kavalchuk",
    author_email="p4elopuh@gmail.com",
    description="Pure-python command-line calculator",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'pycalc=pycalc.pycalc:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
