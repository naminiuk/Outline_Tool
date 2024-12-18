# Blender Outline Tool Addon

## **Overview**

The **Blender Outline Tool Addon** allows users to quickly apply an outline to selected objects with a single click. It automates the process of adding a **Solidify modifier** and a **custom backface-culling emission material**, which would otherwise require repetitive manual work. This addon supports **real-time adjustments** for outline **thickness** and **color**, and it works seamlessly with multiple selected objects.

## **Key Features**

-    **One-Click Outline Application**: Apply outlines to multiple selected objects at once.
-    **Custom Color Control**: Easily change the outline color using a color picker.
-    **Adjustable Thickness**: Control the outline thickness with a slider.
-    **Live Updates**: See thickness and color changes instantly in the viewport.
-    **Undo Support**: All actions can be undone with Ctrl + Z.
-    **Dynamic Material Naming**: Automatically generates unique outline materials for each object.

## **Installation**

1.  Download the Python script (`Outline_Tool 1.0.0.py`).
2.  Open Blender and go to **Edit** → **Preferences** → **Add-ons**.
3.  Click **Install...** and select the downloaded file.
4.  Enable the addon by checking the box next to **Outline Tool**.

## **How to Use**

1.  **Select Objects**: Select one or more mesh objects in the 3D Viewport.
2.  **Open Outline Tool Panel**: Go to the **Outline Tool** tab in the **N-Panel** (press **N** to open it).
3.  **Adjust Settings**:
    -   **Outline Thickness**: Use the slider to set the outline thickness.
    -   **Outline Color**: Use the color picker to set the outline color.
4.  **Apply Outline**: Click the **Apply Outline** button to apply the outline to the selected objects.

## **How It Works**

1.  **Material Generation**:
    
    -   A custom **Emission material** is created for each selected object.
    -   The material name is dynamically generated (e.g., `Outline_Cube`, `Outline_Sphere`).
    -   The material uses **backface culling** to achieve the "outline" effect.
2.  **Solidify Modifier**:
    
    -   A **Solidify** modifier is added to each object.
    -   The **thickness** is set based on the slider value.
    -  **"Flip Normals"** is on by default
    -   The outline is pushed outward to create the visual effect.
3.  **Live Updates**:
    
    -   Changes to **thickness** and **color** are applied in real time.
    -   No need to reapply—just adjust the slider or color, and it updates automatically.

Outlines generated with this addons are compatible only with Eevee.
