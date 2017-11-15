#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import fnmatch
import sys
from pbxproj import XcodeProject
from pbxproj.pbxextensions.ProjectFiles import FileOptions
from pbxproj.pbxsections import PBXShellScriptBuildPhase
from PBXCarthageScriptBuildPhase import PBXCarthageScriptBuildPhase
import sys
import pdb

def askToUser(question):
    userInput = raw_input(question + " (Y/N)\n").lower()
    if userInput == "y" or userInput == "yes" or userInput == "":
        return True
    else:
        return False

def findFileWithExtension(extension, path):
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, '*.' + extension):
            return file
    return None

def addCarthageScript(frameworks):
    script = "/usr/local/bin/carthage copy-frameworks"
    shellBuildPhaseID = None

    inputFiles = []
    outputFiles = []
    for framework in frameworks:
        inputFile = "$(SRCROOT)/" + frameworksPath + framework
        outputFile = "$(BUILT_PRODUCTS_DIR)/$(FRAMEWORKS_FOLDER_PATH)/" + framework
        inputFiles.append(inputFile)
        outputFiles.append(outputFile)

    for target in xcodeProject.objects.get_targets():
        for build_phase_id in target.buildPhases:
            build_phase = xcodeProject.objects[build_phase_id]
            if not isinstance(build_phase, PBXShellScriptBuildPhase):
                continue

            if build_phase.shellScript == script:
                shellBuildPhaseID = build_phase_id
                del xcodeProject.objects[build_phase_id]
                target.remove_build_phase(build_phase)

    shellBuildPhase = PBXCarthageScriptBuildPhase.create(script=script, input_paths=inputFiles, output_paths=outputFiles)
    if shellBuildPhaseID == None:
        shellBuildPhaseID = shellBuildPhase.get_id()

    shellBuildPhase._id = shellBuildPhaseID
    xcodeProject.objects[shellBuildPhaseID] = shellBuildPhase
    for target in xcodeProject.objects.get_targets():
        target.add_build_phase(shellBuildPhase, None)


xcodeProject = None
frameworksPath = None

# Program start
def main():
    global xcodeProject, frameworksPath

    xcodeProjectFile = None
    # Open xcode project and get app name
    xcodeProjectFile = findFileWithExtension("xcodeproj", "./")
    if xcodeProjectFile != None:
        xcodeFileName = os.path.splitext(xcodeProjectFile)[0]
        xcodeProject = XcodeProject.load(xcodeFileName + ".xcodeproj/project.pbxproj")
    else:
        print "Cannot find any .xcodeproj at the current directory"
        sys.exit()

    # Download the frameworks
    os.system("carthage update --platform iOS --no-use-binaries --cache-builds")

    # # Add frameworks to the project
    frameworksPath = "Carthage/Build/iOS/"
    frameworksGroup = xcodeProject.get_or_create_group('Frameworks')
    file_options = FileOptions(embed_framework=False)
    frameworks = []

    for file in os.listdir(frameworksPath):
        if fnmatch.fnmatch(file, '*.framework'):
            frameworks.append(file)
            xcodeProject.add_file(frameworksPath + file, parent=frameworksGroup, force=False, file_options=file_options)

    library_path = os.path.join(u'$(SRCROOT)', frameworksPath)
    xcodeProject.remove_framework_search_paths([u'$(inherited)', library_path])
    xcodeProject.add_framework_search_paths([u'$(inherited)', library_path], recursive=False)

    # Add carthage script with new frameworks
    addCarthageScript(frameworks)

    # Close xcode project
    if xcodeProject != None:
        xcodeProject.save()

    print "\nFinished with success\n"
    print "..........................."
    print "   Made with ♡  by HELM"
    print "...........................\n"

if __name__ == "__main__":
    main()
