# coding: utf-8

# In[ ]:


"""The setup script."""

from setuptools import setup, find_packages

requirements = [
    'Click',
    'pandas',
    'requests',
    'Bio',
    'biopython',
    'coverage',
    'flask',
]

test_requirements = ['pytest>=3', ]

setup(
    author="Hassan Elsayed",
    author_email= 's0haelsa@uni-bonn.de',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Cross Verification of Protein Information Package",
    entry_points={
        'console_scripts': [
            'project_package=project_package.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='DBCV',
    name='DBCV',
    packages=find_packages(include=['DBCV', 'DBCV.*']),
    test_suite='tests',
    tests_require=test_requirements,
    version='0.1.0',
    zip_safe=False,
)
# ...path project_package> pip install ../
