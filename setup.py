import setuptools


def def_requirements():
    """Check PIP Requirements"""
    with open("requirements.txt") as file_content:
        pip_lines = file_content.read().splitlines()
    return pip_lines


def def_readme():
    """Check Readme Markdown"""
    readme = ""
    with open("README.md") as file_content:
        readme = file_content.read()
    return readme


setuptools.setup(
    name="lichesspy",
    version="2.0.0",
    author="Niffecs",
    author_email="Niffecs@gmail.com",
    description="Python wrapper for lichess",
    long_description=def_readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Niffecs/lichesspy",
    packages=["lichesspy"],
    package_data={"lichesspy": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=def_requirements(),
)
