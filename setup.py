import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TOBARA-pkg-MiguelRAvila", 
    version="0.0.1",
    author="Miguel R. Ávila",
    author_email="miguelravila@outlook.com",
    description="Nuestro sistema es una herramienta de análisis de funciones booleanas, cuya tarea principal es reducir lo máximo posible una función booleana. Con estos datos realizaremos una API que permita a cualquier usuario consultar estos elementos de cualquier función booleana que quieran introducir.",
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
