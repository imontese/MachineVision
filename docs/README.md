# Machine Vision Application using PLC  
   
Machine vision engine from scratch using Python and OpenCV, the famous library for image processing. The aim is to create a small vision engine that can be connected to your PLC and your machine without spending a fortune on expensive equipment and software.  
   
## Project Overview  
   
Our project is a bottle labeling quality control system. In chemical factories, it's vital to have a label on every single bottle, containing important information like expiration date and instructions. The program checks the label on every bottle, allowing it to pass if the label is present and rejecting it if not.  
   
## Requirements  
   
- PLC (any brand that supports communication protocols)  
- Mini PC (to run image processing algorithms)  
- Camera (webcam or budget industrial camera)  
    
### Emulation  
   
- Codesys Runtime: Free 2-hour PLC emulator with OPC UA support  
- Python: Free programming language and libraries  
- Camera: Standstill pictures in a directory to act as the camera  
- Sensors and actuators: Emulate signals and actions using the PLC emulator  
   
Using small GUI for the PLC using Codesys to control the system.  
   
## Getting Started  
   
1. Install the Codesys Runtime and set up the PLC emulator with OPC UA support.  
2. Install Python and the necessary libraries (e.g., OpenCV).  
3. Prepare a directory with standstill pictures to act as the camera.  
4. Emulate sensors and actuators using the PLC emulator.  
5. Create a GUI for the PLC using Codesys.  
   