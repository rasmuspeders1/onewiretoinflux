from setuptools import setup
setup(
    name="onewiretoinflux",
    version="1.0.0",
    packages=['onewiretoinflux'],
    entry_points={
        'console_scripts': ['logtemperatures=onewiretoinflux.logtemperatures']
    },
    install_requires=['requests', 'influxdb']
)
