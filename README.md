# CommandOnSelected

Command On Selected Is A Simple Blender Addon that Allows you to Run Blender Operator to Selected Objects
While It is much better to use the Console if You know What you are doing, this is more "Non Coder Friendly" of Looping a Operator over Selected Objects

![CommandOnSelected](https://user-images.githubusercontent.com/79613445/148007872-d3dfe7a2-a016-4989-ac09-65fd77925a42.gif)

What it Does Under the Hood is It will Make Each Selected Object into Active one by one and Run the Command You Provided

## Important

- This Currently Only Works In Object Mode

## Errors

![Error](https://user-images.githubusercontent.com/79613445/148008992-ab20ec6f-f254-45d9-8a26-15cb930fc1f9.png)

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

![Info](https://user-images.githubusercontent.com/79613445/148009323-bd09ed24-9d93-4230-a619-a467e413bd2e.png)

The Most Eaiest way to Access to the Command is Through the Info Editor
- Open the Info Editor
- Run the Operator you want to use
- Most Operator will appear in Info Editor (Some Will Not)
- Select the Last Command (Or the One you want)
- Copy and Paste to the Command Text Box in the Addon

![Copy Info](https://user-images.githubusercontent.com/79613445/148009742-ded588c6-de77-4b22-8d63-b98089bfb267.png)

## Method 2: Copy Python Command

![Preferences](https://user-images.githubusercontent.com/79613445/148007876-46264630-e8d3-4341-9fbc-f7ddb65f45f7.png)

- First you need to Enable "Developer Extras" and "Python Tooltips" in Preferences
- After Enabled Python Tooltips, If you Hover an Operator, it will Display the Python Command
- After Enabled Developer Extras you can Right Click on the Operator and Copy Python Command

![CopyPythonCommand](https://user-images.githubusercontent.com/79613445/148009889-a58c0e90-ee72-40e7-bb85-7d31ef81f30b.png)
