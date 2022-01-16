from setuptools import setup, find_packages

install_requires = ["redis>=4.1.0", "schema>=0.7.5"]

# Conditional dependencies:


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="dionysus",
    version="0.1.1",
    description="Tiny framework for interacting with redis pubsub and other protocols using custom adapters",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Joshua3212/dionysus",
    author="Joshua3212",
    author_email="some@mail.com",
    license="MIT",
    packages=["app", "utils", "adapters"],
    python_requires=">=3.7",
    install_requires=install_requires,
    project_urls={
        "GitHub": "https://github.com/Joshua3212/dionysus",
    },
)
