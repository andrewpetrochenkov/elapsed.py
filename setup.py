import setuptools

setuptools.setup(
    name='elapsed',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
