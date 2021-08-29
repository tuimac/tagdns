from setuptools import setup, find_packages

setup(
    name="tagdns",
    version="1.0.0",
    url="https://github.com/tuimac/tagdns",
    author="tuimac",
    author_email="tuimac.devadm01@gmail.com",
    license="LICENSE.md",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Software Distribution"
    ],
    description="DNS Server",
    python_requires=">=3.7.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "boto3>=1.18.0",
        "setuptools"
    ],
    entry_points={
        "console_scripts": [
            "tagdns=main:main"
        ]
    }
)
