from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="NoomSmartKeyboard",
    version="1.0.0",
    url="https://github.com/poommin2543/Noom-Smart-Keyboard",
    author="Noom Poommin",
    author_email="poommin2543@gmail.com",
    description="Description of my package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),    
    install_requires=[
        'pywin32',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
)
