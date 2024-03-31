from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="sistema_bancario",
    version="0.0.1",
    author="Tiago Santiago",
    author_email="tiagosantiago@yandex.com",
    description="Sistema bancario POO organizado em pacote",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="add githublink",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">3.8",
)
