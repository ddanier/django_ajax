from setuptools import setup, find_packages

setup(
    name = "django_ajax",
    version = "0.1.1-1",
    description = 'Utility app to support AJAX development in Django',
    author = 'David Danier',
    author_email = 'david.danier@team23.de',
    url = 'https://github.com/ddanier/django_ajax',
    long_description=open('README.rst', 'r').read(),
    packages = [
        'django_ajax',
        'django_ajax.templatetags',
    ],
    install_requires = [
        'Django >=1.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)

