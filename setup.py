from distutils.core import setup
import gensim.downloader as api


api.load("glove-wiki-gigaword-50")


setup(name="easy_tools",
      version="0.1",
      description="Easy tools to facilitate faster pace in generating boilerplate code",
      author="A.Althobaiti",
      author_email="althobaiti@dot.com",
      url="",
      packages=["easy_tools"],
)
