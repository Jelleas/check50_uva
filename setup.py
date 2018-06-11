from setuptools import find_packages, setup

setup(
    author="JelleAs",
    author_email="jelle.van.assema@gmail.com",
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    description="This is check50 UvA, an extension of check50.",
    install_requires=["check50", "jupyter"],
    keywords=["check", "check50"],
    name="check50.uva",
    packages=["check50.uva", "check50.uva.python"],
    include_package_data=True,
    url="https://github.com/jelleas/check50_uva",
    version="0.0.1"
)
