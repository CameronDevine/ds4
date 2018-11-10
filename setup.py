from distutils.core import setup

setup(
	version = '0.0.0',
	scripts = ['scripts/ds4imu.py'], 
	requires = ['numpy', 'ds4drv']
)
