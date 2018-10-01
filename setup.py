from setuptools import setup, find_packages

VERSION = '1.0.1'

setup(
    name="mkdocs-bootstrap",
    version=VERSION,
    url='http://mkdocs.github.io/mkdocs-bootstrap/',
    license='BSD',
    description='Bootstrap theme for MkDocs',
    author='Dougal Matthews',
    author_email='dougal@dougalmatthews.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['mkdocs>=1.0'],
    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    entry_points={
        'mkdocs.themes': [
            'bootstrap = mkdocs_bootstrap',
        ]
    },
    zip_safe=False
)
