"""
Install teamwork.
"""

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': 'Simple parallel processing in Python.',
		'author': 'Matt Christie',
		'download_url': 'https://github.com/christiemj09/pyskeleton.git',
		'author_email': 'christiemj09@gmail.com',
		'version': '0.1',
		'install_requires': [],
		'packages': ['teamwork'],
		'scripts': [],
		'entry_points': {
		    'console_scripts': [],
		},
		'name': 'teamwork',
	}

	setup(**config)	

if __name__ == '__main__':
	main()
