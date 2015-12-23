import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='django-substitution-user',
        version='0.1.3',
        description='Django substitution user',
        author='Alexey Baranov',
        author_email='atlantij@gmail.com',
        url='https://github.com/torchingloom/django-substitution-user',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        long_description='Django substitution user'
                         'Installation'
                         '  pip install django-substitution-user'
                         'Project page & docs'
                         '  https://github.com/torchingloom/django-substitution-user',
        classifiers=[
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Framework :: Django',
        ],
)
