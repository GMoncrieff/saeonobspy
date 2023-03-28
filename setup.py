from setuptools import setup, find_packages

setup(
    name='saeonobspy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'geopandas',
        'requests',
        'shapely'
    ],
    url='https://github.com/GMoncrieff/saeonobspy',
    author='Glenn Moncrieff',
    author_email='glenn@saeon.ac.za',
    description='Python package to interact with the SAEON Observation Database API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
