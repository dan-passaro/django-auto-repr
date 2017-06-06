from setuptools import setup

setup(
    name='django-auto-repr',
    version='1.1',
    description='Give Django models a useful __repr__',
    url='https://github.com/dan-passaro/django-auto-repr',
    author='Dan Passaro',
    author_email='danpassaro@gmail.com',
    license='MIT',
    py_modules=['django_auto_repr'],
    install_requires=[
        'django',
    ]
)
