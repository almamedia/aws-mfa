from setuptools import setup

setup(
    name='aws-mfa',
    version='0.0.10',
    description='Manage AWS MFA Security Credentials',
    license='MIT',
    author='Brian Nuszkowski',
    author_email='brian@bnuz.co',
    packages=['awsmfa'],
    scripts=['aws-mfa'],
    url='https://github.com/broamski/aws-mfa',
    install_requires=['boto3>=1.2.3']
)
