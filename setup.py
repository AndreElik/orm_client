from setuptools import setup
REQUIRES = [
    'allure-pytest',
    'curlify',
    'sqlalchemy',
    'structlog',
    'records'
]
setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/AndreElik/orm_client.git',
    license='MIT',
    author='Andre',
    author_email='',
    install_requires=REQUIRES,
    description='orm_client'
)
