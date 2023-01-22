from setuptools import setup, find_packages
import pathlib
from os import path

HERE = pathlib.Path(__file__).parent.resolve()
long_description = (HERE / 'README.md').read_text(encoding='utf-8')
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs]
setup(name='temperature_converter_Ivanova',
      	version='0.1',
      	description='Python libray to help with temperature conversion',
      	url='http://github.com/karinaiva48/TMS_Ivanova_tree/my_homework/HW_17',
      	author='Karina Ivanova',
      	author_email='karinaiva48@gmail.com',
	long_description=long_description,
   	long_description_content_type='text/markdown',
      	license='MIT',
 	packages=find_packages(),
   	python_requires='>=3.9, <4',
   	install_requires=install_requires,      
	zip_safe=False)