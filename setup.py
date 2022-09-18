import os
import setuptools


def requirements(file="requirements.txt"):
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return [i.strip() for i in r]
    else:
        return []

def readme(file="README.md"):
    if os.path.isfile(file):
        with open(file, encoding="utf8") as r:
            return r.read()
    else:
        return ""

setuptools.setup(
    name="MUKUNDX",
    version="0.0.2",
    description="A Simple Python module to do many things if need support then join @META_CHATS | or contact @LEGEND_MUKUND",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="Legend Mukund",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Source": "https://github.com/Legend-Mukund/MUKUNDX"
    },
    python_requires=">=3.6",
    py_modules=['MUKUNDX'],
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=requirements()
)
