import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ai_pkg",
    version="0.0.2",
    author="Muhammad Fakhrul Amin",
    author_email="aminfakhrul99@gmail.com",
    description="Simple ai_pkg python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mfakhrulam/Prak-Kecerdasan-Buatan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)