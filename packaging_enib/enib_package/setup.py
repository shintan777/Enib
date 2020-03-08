import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enib-pkg-runtime-terrors", # Replace with your own username
    version="0.0.1",
    author="Archisha Chandel, Aditya Srivastav, Tanvi Shinde, Tanay Joshi",
    # author_email="author@example.com",
    description="Extract information from invoice",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/shintan777/Enib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)