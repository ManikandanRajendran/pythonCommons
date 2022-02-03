import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='pythonCommons',
    version='0.0.1',
    author='Manikandan Rajendran',
    author_email='manikandan.rajendran@betwaygroup.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ManikandanRajendran/pythonCommons',
    project_urls = {
        "Bug Tracker": "https://github.com/ManikandanRajendran/pythonCommons/issues"
    },
    license='MIT',
    packages=['pythonCommons'],
    install_requires=['requests'],
)
