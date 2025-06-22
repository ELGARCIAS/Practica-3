from setuptools import find_packages, setup

package_name = 'practica3_polgarcia'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pol garcia',
    maintainer_email='polgarciafont@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'general = practica3_polgarcia.nodo_principal:main',
		'talker = practica3_polgarcia.publisher_member_function:main',
		'listener = practica3_polgarcia.subscriber_member_function:main',
        ],
    },
)
