from setuptools import setup, find_packages

setup(
    name='django-saengine',
    version='0.0.4',
    author='bigtiger',
    author_email='chinafengheping@gmail.com',
    url='http://www.hshl.ltd',
    description=u'django session auth engine',
    packages=find_packages(),
    install_requires=[
        'six',
        'django>=1.7.7',
        'requests>=2.18.4',
        'django-restful>=0.0.4'
    ]
)
