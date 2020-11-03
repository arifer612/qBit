import setuptools

setuptools.setup(
    name="qBit",
    version="unreleased",
    author="arifer612",
    author_email="arifer1995@gmail.com",
    description="A human-readable qBittorrent torrent manager",
    url="https://github.com/arifer612/qBit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Natural Language :: English",
    ],
    python_requires='>=3.6',
)