import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apexe3", 
    version="0.0.1",
    author="Usman Khan",
    author_email="usman@apexe3.com",
    description="API Wrapper and utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),

    install_requires=[
        'certifi==2020.6.20',
        'chardet==3.0.4',    
        'eventemitter==0.2.0',   
        'idna==2.10',    
        'numpy==1.19.2',   
        'pandas==1.1.3', 
        'PyEventEmitter==1.0.5',    
        'python-dateutil==2.8.1', 
        'requests==2.24.0',   
        'setuptools==41.2.0',   
        'urllib3==1.25.11',  
        'websocket-client==0.57.0',   
        'wheel==0.33.1' 
    ],
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    python_requires='>=3.8<3.9',  # works for 3.8x  but unstable on 3.9x
)