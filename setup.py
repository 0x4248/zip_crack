import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zip_crack",
    url="https://github.com/0x4248/zip_crack/",
    author="0x4248",
    packages=["zip_crack"],
    install_requires=[""],
    version="1.0.0",
    license="GNU",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A simple data corruption engine written in python",
)
