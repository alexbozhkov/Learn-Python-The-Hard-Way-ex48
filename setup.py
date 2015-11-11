try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Learn Python The Hard Way ex48',
    'author': 'Alexander Bozhkov',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'alexander.bojkov89@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'Learn Python The Hard Way ex48'
}

setup(**config)