from setuptools import setup
setup(
    name="onewiretoinflux",
    version="1.0.0",
    scripts=['logtemperatures.py']
    install_requires=['requests', 'influxdb']
)
