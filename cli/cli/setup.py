```python
from setuptools import setup, find_packages setup( name=‘solfoundry-cli’, version=‘0.1.0’, packages=find_packages(), install_requires=[ ‘click>=8.0.0’, ‘requests>=2.25.0’, ‘pyyaml>=5.4.0’, ], entry_points={ ‘console_scripts’: [ ‘sf=solfoundry_cli:cli’, ], }, author=‘OpenClaw Agent’, description=‘CLI tool for SolFoundry bounties’, python_requires=‘>=3.8’,
)
