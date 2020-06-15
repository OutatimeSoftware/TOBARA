import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TOBARA", 
    version="1.0.3",
    author="Miguel R. Ávila",
    author_email="miguelravila@outlook.com",
    description="TOBARA (The Only Boolean Algebra Reduction App) is a toolkit of Boolean function analysis whose main task is to reduce Boolean functions as much as possible. Our objetive is to determine information about the function like variables, terms and then reduce the function.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MiguelRAvila/projectTOBARA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
