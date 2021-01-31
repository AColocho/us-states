import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="unitedstates",
    version="0.0.1.7",
    author="Alejandro Colocho",
    author_email="a.colocho@outlook.com",
    description="Package that provides information about U.S states and territories.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AColocho/us-states",
    packages=setuptools.find_packages(),
    license="Boost Software License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)