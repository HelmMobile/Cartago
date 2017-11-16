# Cartago

Cartago automates the download using Carthage and further addition of the frameworks to your xcode project.

We created Cartago for internal use as a part of our initial project generation tool to configure a fresh project with our template.

Cartago simply downloads the frameworks and then updates your project adding the new frameworks. It also updates the carthage script on your target Build Phases

# Usage

Just run
```
cartago
```
from your terminal inside the root folder of your project.

Cartago will need the '.xcodeproj' file and the 'Cartfile' file there

# Installation

If you have pip just run
```
pip install cartago
```
else run
```
sudo python setup.py install
```

# Notes

Cartago will perform

```
carthage update --platform iOS --no-use-binaries --cache-builds
```

behind the scenes

This is the command that we find it is faster and causes less trouble.

In the next version we will add the option to change the flags. Pull requests are welcome :)

Same thing with iOS support. Right now we look at the contents of 'Carthage/Build/iOS/' to figure out which frameworks to add to the project so adding Mac development support might be a little more tricky.






