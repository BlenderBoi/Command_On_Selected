# CommandOnSelected

![Banner](https://user-images.githubusercontent.com/79613445/210192388-ebae22f3-6a5a-4486-ae98-37cfedb1d7e1.png)

Command On Selected Is A Simple Blender Addon that Allows you to Run Blender Operator to Selected Objects
While It is much better to use the Console if You know What you are doing, this is more "Non Coder Friendly" of Looping a Operator over Selected Objects

![CommandOnSelectedPanel](https://user-images.githubusercontent.com/79613445/210192392-0b9e7ca3-4a86-44aa-a068-738e052117d3.png)

What it Does Under the Hood is It will Make Each Selected Object into Active one by one and Run the Command You Provided

## Important

- This Currently Only Works In Object Mode

## Errors

![Errors](https://user-images.githubusercontent.com/79613445/210192395-8872a05d-74e0-4d08-a01d-8728f866a421.png)

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

![InfoEditor](https://user-images.githubusercontent.com/79613445/210192402-5ffcb708-8a9e-40e7-b7c1-2e235c1c9c81.png)


The Most Eaiest way to Access to the Command is Through the Info Editor
- Open the Info Editor
- Run the Operator you want to use
- Most Operator will appear in Info Editor (Some Will Not)
- Select the Last Command (Or the One you want)
- Copy and Paste to the Command Text Box in the Addon

![Copy](https://blenderboi.com/gallery/CommandOnSelected/CopyCommand.png)

## Method 2: Copy Python Command

![PythonCommand](https://user-images.githubusercontent.com/79613445/210192410-47aebefb-f2a3-490e-8cde-da04eb8e107b.png)



- First you need to Enable "Developer Extras" and "Python Tooltips" in Preferences
- After Enabled Python Tooltips, If you Hover an Operator, it will Display the Python Command
- After Enabled Developer Extras you can Right Click on the Operator and Copy Python Command

![CopyPython](https://user-images.githubusercontent.com/79613445/210192422-347352a7-7a79-4b59-a61a-5e140c1e092e.png)



