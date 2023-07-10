from setuptools import setup, find_packages

setup(
    name="NoomSmartKeyboard",
    version="0.0.2",
    url="https://github.com/poommin2543/Noom-Smart-Keyboard",
    author="Noom Poommin",
    author_email="poommin2543@gmail.com",
    description="Description of my package",
    packages=find_packages(),    
    install_requires=[
        'pywin32',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        "Operating System :: Microsoft :: Windows",
    ],
)
