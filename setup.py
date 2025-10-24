from setuptools import setup, find_packages

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name="cv-tools",
    version="1.0.0",
    author="mookor",
    description="Computer Vision utilities for image processing",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/mookor/cv_tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.10",
    install_requires=[
        "opencv-python>=4.0.0",
        "numpy>=1.20.0",
    ],
    entry_points={
        "console_scripts": [
            "color-threshold=cv_tools.color_threshold.__main__:main",
        ],
    },
)
