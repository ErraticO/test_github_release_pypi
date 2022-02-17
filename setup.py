import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="print_text",
    version="0.0.1",
    author="wu di",
    author_email="",
    description="test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ErraticO/test_github_release_pypi",
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'add=print_text.add:make',
            'remove=print_text.remove:make'
            'update=print_text.update:make'
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
