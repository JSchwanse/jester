from setuptools import setup, find_packages

setup(
    name="Jester",
    author="jswa",
    description="Private Python library to create and maintain business object endpoints.",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent"
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content"
    ],
    python_requires='>=3.12',
    setup_requires=['setuptools-git-versioning'],
    version_config={
        "dirty_template": "{tag}",
    },
    install_requires=[
        'J_Core @ file:///C:/Users/jswa/Documents/Own%20Progz/j_core/dist/J_Core-0.0.0-py3-none-any.whl'
    ]
)
