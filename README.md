# Cartago

Cartago automates the download using Carthage and further addition of the frameworks to your xcode project.

Cartago simply downloads the frameworks and then updates your project adding the new frameworks. It also updates the carthage script on your target Build Phases

# Usage

Just run
```bash
cartago
```
from your terminal inside the root folder of your project.

Cartago will need the `.xcodeproj` file and the `Cartfile` file there

# Installation

If you have pip just run
```bash
pip install cartago
```
else clone/download it and run
```bash
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

Same thing with iOS support. Right now we look at the contents of `Carthage/Build/iOS/` to figure out which frameworks to add to the project so adding Mac development support might be a little more tricky.

# License
```
Copyright 2017 Helm

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
