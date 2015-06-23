from setuptools import setup, find_packages

VERSION = '0.1.1'


setup(
    name="mkdocs-bootstrap",
    version=VERSION,
    url='http://www.mkdocs.org',
    license='BSD',
    description='Bootstrap theme for MkDocs',
    author='Dougal Matthews',
    author_email='dougal@dougalmatthews.com.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'bootstrap = mkdocs_bootstrap',
        ]
    },
    zip_safe=False
)
