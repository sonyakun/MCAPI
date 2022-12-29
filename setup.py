import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MineAPI",
    version="0.0.1",
    install_requires=[
        "aiohttp",
        "asyncio"
    ],
    author="sonyakun",
    author_email="sonyakun217@gmail.com",
    description="A MCServer API Wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sonyakun/MCAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)