import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="us-states",
    version="1.0.0",
    author="Alejandro Colocho",
    author_email="a.colocho@outlook.com",
    description="Package that provides information about U.S states.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AColocho/us-states",
    packages=setuptools.find_packages(exclude=("tests")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Boost Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)