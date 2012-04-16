from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='g24.sharingbox',
      version=version,
      description="Sharingbox for g24.at",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='Johannes Raggam',
      author_email='johannes@raggam.co.at',
      url='http://github.com/g24at/g24.sharingbox',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['g24',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
)
