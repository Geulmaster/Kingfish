import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Kingfish",
    version="0.0.1",
    author="Eyal Geulayev",
    author_email="eyal.geulayev@gmail.com",
    description="My first published package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Geulmaster/Kingfish",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)