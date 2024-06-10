from setuptools import setup, find_packages

setup(
    name='EasyBar',
    version='0.0.1',
    packages=find_packages(),
    package_data={'easybar': ['colour_sequence.json']},  # 指定要包含的文件
    install_requires=[],
    python_requires='>=3.6',
    author='University of Liverpool',
)
