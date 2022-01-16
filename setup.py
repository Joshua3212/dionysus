from setuptools import setup, find_packages
import dionysus

install_requires = ["redis>=4.1.0", "schema>=0.7.5"]

# Conditional dependencies:


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="dionysus",
    version=dionysus.__version__,
    description=dionysus.__description__,
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Joshua3212/dionysus",
    author=dionysus.__author__,
    author_email="some@mail.com",
    license="MIT",
    packages=["dionysus", "dionysus.utils", "dionysus.adapters"],
    python_requires=">=3.7",
    install_requires=install_requires,
    project_urls={
        "GitHub": "https://github.com/Joshua3212/dionysus",
    },
)
