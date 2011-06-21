from setuptools import find_packages, setup
setup(
    name='TracWikiBaseline', version='1.1',
    packages=find_packages(exclude=['*.tests*']),
    entry_points = """
        [trac.plugins]
        wikibaseline = wikibaseline
    """,
)
