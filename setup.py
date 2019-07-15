from setuptools import setup


SHORT_DESCRIPTION = 'Extension for Foliant documentation tools to generate custom slugs.'

try:
    with open('README.md', encoding='utf8') as readme:
        LONG_DESCRIPTION = readme.read()

except FileNotFoundError:
    LONG_DESCRIPTION = SHORT_DESCRIPTION


setup(
    name='foliantcontrib.slugs',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    version='1.0.0',
    author='Artemy Lomov',
    author_email='artemy@lomov.ru',
    url='https://github.com/foliant-docs/foliantcontrib.slugs',
    packages=['foliant.config'],
    license='MIT',
    platforms='any',
    install_requires=[
        'foliant>=1.0.4'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ]
)
