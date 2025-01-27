from setuptools import setup, find_packages

setup(
    name="libastral",
    version="0.1",
    packages=find_packages(),
    description="Библиотека с бесполезными функциями",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="McKryach",
    author_email="mckryach@gmail.com",
    url="https://github.com/McKryach/libastral",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)