from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='pewn',
    version='0.0.1',
    description='📦 Another Python library for downloading files from URL.',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    url='https://github.com/5elenay/pewn/',
    author='5elenay',
    author_email='',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/5elenay/pewn/issues",
    },
    classifiers=classifiers,
    keywords=["python", "download", "pewn", "async", "download-file"],
    packages=find_packages(),
    python_requires='>=3.6.0',
    install_requires=["aiohttp", "aiofiles"]
)
