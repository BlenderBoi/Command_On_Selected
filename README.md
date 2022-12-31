# CommandOnSelected

Command On Selected Is A Simple Blender Addon that Allows you to Run Blender Operator to Selected Objects
While It is much better to use the Console if You know What you are doing, this is more "Non Coder Friendly" of Looping a Operator over Selected Objects

![CommandOnSelected](https://blenderboi.com/gallery/CommandOnSelected/CommandOnSelectedPanel.png)

What it Does Under the Hood is It will Make Each Selected Object into Active one by one and Run the Command You Provided

## Important

- This Currently Only Works In Object Mode

## Errors

![Error](https://blenderboi.com/gallery/CommandOnSelected/Errors.png)

- Command On Selected is Extremely Prone to Error, Because Blender's Operator are Context Sensitive. 
- If You encounter Error, do not need Panic, It is to be expected, and It "most likely" won't break anything. 
- The Error reported in UI as popup is just there to alert you the Operator is not Working, nothing breaks. 
- The Execution of Command is Wrapped in a Try Block, If you want to check the Actual Error, it is printed in the console

## Command

- Depending on the Situation, running the command might only work on the specific object if you copy it from the info panel
- The Operator starts with "bpy.ops."
- Command on Selected only work on Operator that perform action on Active Object
- If the Operator is not the type that perform action on active object, it will just run the same command X times (Amount of Selected Object)

# Getting Commands

## Method 1: Using Info Editor

![Info](https://blenderboi.com/gallery/CommandOnSelected/InfoEditor.png)

The Most Eaiest way to Access to the Command is Through the Info Editor
- Open the Info Editor
- Run the Operator you want to use
- Most Operator will appear in Info Editor (Some Will Not)
- Select the Last Command (Or the One you want)
- Copy and Paste to the Command Text Box in the Addon

![Copy](https://blenderboi.com/gallery/CommandOnSelected/CopyCommand.png)

## Method 2: Copy Python Command

![PythonCommand](https://blenderboi.com/gallery/CommandOnSelected/PythonCommand.png)


- First you need to Enable "Developer Extras" and "Python Tooltips" in Preferences
- After Enabled Python Tooltips, If you Hover an Operator, it will Display the Python Command
- After Enabled Developer Extras you can Right Click on the Operator and Copy Python Command

![CopyPython](https://blenderboi.com/gallery/CommandOnSelected/CopyPython.png)

