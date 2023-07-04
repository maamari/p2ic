import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name = "p2ic",
    version = "0.0.1",
    author = "Karime Maamari",
    author_email = "maamari@usc.edu",
    description = ("Profiles to initial conditions"),
    license = "MIT",
    keywords = "initial conditions, profiles",
    url = "http://packages.python.org/ghsu",
    packages=['p2ic'],
    #long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',              
    install_requires=["selenium>=4.3.0",
                      "webdriver_manager>=3.8.2"],                    
    )
