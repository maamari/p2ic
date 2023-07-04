from setuptools import setup

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setup(
    name='p2ic',
    version='0.0.1',
    description='Generate initial conditions from density and vdisp profiles',
    py_modules=["p2ic"],
#    package_dir={'': ''},
    extras_require={
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
#    long_description=long_description,
#    long_description_content_type="text/markdown",
    author="Karime Maamari",
    author_email="maamari@usc.edu",
    url="https://github.com/maamari/p2ic"
)
