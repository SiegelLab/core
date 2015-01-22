# Get started on Mac OS X

## First things

1. Update your Mac OS to the latest version 
2. Install Xcode (free) and the command line tools 

## Cool software you need  

This guide is written for someone running Mac OS X who is comfortable with running 
Bash commands in the Terminal. If you don't know what your `PATH` is or how to change 
it, or what your `.bashrc` is, it may be difficult
to follow the rest of this guide. Consult Matt Might's blog for [getting
started with Unix](http://matt.might.net/articles/basic-unix/) before going any
further. 

Install [Homebrew]() and use it to install some great apps: 

```bash
brew install git curl tree python3
```

Homebrew will symlink these into `/usr/local/bin/`. If
you don't already `/usr/local/bin/` in your PATH, add it now. 

To install the required Python packages, use 

```bash
pip3 install numpy scipy pandas 
pip install numpy scipy pandas
```

*Note* you really **must** install for both Python 2 and Python 3. 

## Clone and build Rosetta locally 

Change into the directory you want to install Rosetta into (recommendation: use `~/Applications`) and run

```bash
curl -Ok https://raw.githubusercontent.com/RosettaCommons/rosetta_clone_tools/master/get_rosetta.sh
bash get_rosetta.sh main
```

to get the main source repo (add `tools` at the end if you want the tools and/or `demos` if you want the demos). 

To compile (=build) Rosetta, try:

```bash
cd Rosetta/main/source
./scons.py cxx=clang mode=release bin 
```

And add the following to your `.bashrc`:

```bash
export PATH=$PATH:/usr/local/bin:~/Applications/Rosetta/main/source/bin
export ROSETTA3_DB=~/Applications/Rosetta/main/database
```

This will allow you to call Rosetta apps (like `rosetta_scripts`) from anywhere in your
shell, including scripts, without a path prefix, like 

```bash 
rosetta_scripts.macosclangrelease @ flags
```

It is recommended that you install into `~/Applications` (your user Applications folder) rather than `/Applications` (the system Applications folder). 

**Good job, you're done!**

