from setuptools.command.build_py import build_py
from setuptools import setup
from typing import Optional
import subprocess
import shutil
import sys
import os


def get_lrelease_command() -> Optional[str]:
    for i in ("lrelease", "pyside6-lrelease", "pyside5-lrelease"):
        if shutil.which(i) is not None:
            return i
    return None


class BuildTranslations(build_py):
    def run(self):
        command = get_lrelease_command()
        if command is None:
            print("lrelease not found", file=sys.stderr)
            sys.exit(1)
        translation_source_dir = os.path.join("jdAnimatedImageEditor", "translations")
        translation_bin_dir = os.path.join(self.build_lib, "jdAnimatedImageEditor", "translations")
        if not os.path.isdir(translation_bin_dir):
            os.makedirs(translation_bin_dir)
        for i in os.listdir(translation_source_dir):
            if i.endswith(".ts"):
                subprocess.run([command, os.path.join(translation_source_dir, i), "-qm", os.path.join(translation_bin_dir, i[:-3] + ".qm")])
        super().run()


with open(os.path.join(os.path.dirname(__file__), "jdAnimatedImageEditor", "version.txt"), "r", encoding="utf-8") as f:
    version = f.read().strip()

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()


setup(name="jdAnimatedImageEditor",
    version=version,
    description="A simple program for creating animated Images",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="JakobDev",
    author_email="jakobdev@gmx.de",
    url="https://gitlab.com/JakobDev/jdAnimatedImageEditor",
    download_url="https://gitlab.com/JakobDev/jdAnimatedImageEditor/-/releases",
    python_requires=">=3.9",
    include_package_data=True,
    install_requires=[
        "PyQt6",
        "requests",
        "pillow"
    ],
    packages=["jdAnimatedImageEditor"],
    entry_points={
        "console_scripts": ["jdanimatedimageeditor = jdAnimatedImageEditor:main"]
    },
    cmdclass={
        "build_py": BuildTranslations,
    },
    license="GPL v3",
    keywords=["JakobDev", "PyQt6"],
    project_urls={
        "Issue tracker": "https://gitlab.com/JakobDev/jdAnimatedImageEditor/-/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Environment :: Other Environment",
        "Environment :: X11 Applications :: Qt",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Natural Language :: German",
        "Topic :: Text Editors",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
    ]
)
