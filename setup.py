from setuptools import setup
f=open("README.md", "r")
text = f.read()
f.close()
setup(
    author="Matt Antalek Jr",
    name="uniprotmapper",
    packages=["uniprotmapper"],
    license="MIT",
    author_email="matthew.antalek@northwestern.edu",
    version="0.0.4dev",
    url="https://github.com/themantalope/uniprotmapper",
    description="A little package for running mapping requests through UniProt's online API.",
    long_description=text,
    classifiers=["Topic :: Scientific/Engineering :: Bio-Informatics"]
)
