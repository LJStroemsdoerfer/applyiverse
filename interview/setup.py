# load libs
from setuptools import setup
import interviewer

# catch the version
current_version = interviewer.__version__

# read in README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# define the setup
setup(name='interviewer',
      version=current_version,
      description='Preparation Bot for Job Interviews',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='',
      author='Lukas Jan Stroemsdoerfer',
      author_email='ljstroemsdoerfer@gmail.com',
      license='MIT',
      packages=['interviewer'],
      zip_safe=False)