
Sub Main
    ' ========================================================
    ' 1. ELECTRIC FIELD (E-FIELD) - UNIFIED SCALE: 0 to 2700 V/m
    ' ========================================================
    ' --- 1.1 XY Cross Section (Z = 30 mm) ---
    SelectTreeItem("2D/3D Results\E-Field\e-field (f=9) [1]")
    With VectorPlot2D
        .Type "arrows"
        .SetDensity 45
        .PlaneNormal "z"
        .PlaneCoordinate 30.0
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 2700.0
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/efield_v2_vector_XY.png", 2400, 1500
    End With
    
    SelectTreeItem("2D/3D Results\E-Field\e-field (f=9) [1]\Abs")
    With ScalarPlot2D
        .Type "contour"
        .PlaneNormal "z"
        .PlaneCoordinate 30.0
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 2700.0
        .DrawContourLines False
        .Banding False
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/efield_v2_contour_XY.png", 2400, 1500
    End With

    ' --- 1.2 XZ Longitudinal Horizontal (Y = 5.08 mm) ---
    SelectTreeItem("2D/3D Results\E-Field\e-field (f=9) [1]")
    With VectorPlot2D
        .Type "arrows"
        .SetDensity 45
        .PlaneNormal "y"
        .PlaneCoordinate 5.08
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 2700.0
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/efield_v2_vector_XZ.png", 2400, 1500
    End With
    
    SelectTreeItem("2D/3D Results\E-Field\e-field (f=9) [1]\Abs")
    With ScalarPlot2D
        .Type "contour"
        .PlaneNormal "y"
        .PlaneCoordinate 5.08
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 2700.0
        .DrawContourLines False
        .Banding False
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/efield_v2_contour_XZ.png", 2400, 1500
    End With

    ' --- 1.3 YZ Longitudinal Vertical (X = 0 mm) ---
    SelectTreeItem("2D/3D Results\E-Field\e-field (f=9) [1]")
    With VectorPlot2D
        .Type "arrows"
        .SetDensity 45
        .PlaneNormal "x"
        .PlaneCoordinate 0.0
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 2700.0
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/efield_v2_vector_YZ.png", 2400, 1500
    End With
    
    SelectTreeItem("2D/3D Results\E-Field\e-field (f=9) [1]\Abs")
    With ScalarPlot2D
        .Type "contour"
        .PlaneNormal "x"
        .PlaneCoordinate 0.0
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 2700.0
        .DrawContourLines False
        .Banding False
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/efield_v2_contour_YZ.png", 2400, 1500
    End With

    ' ========================================================
    ' 2. MAGNETIC FIELD (H-FIELD) - UNIFIED SCALE: 0 to 5.2 A/m
    ' ========================================================
    ' --- 2.1 XY Cross Section (Z = 30 mm) ---
    SelectTreeItem("2D/3D Results\H-Field\h-field (f=9) [1]")
    With VectorPlot2D
        .Type "arrows"
        .SetDensity 45
        .PlaneNormal "z"
        .PlaneCoordinate 30.0
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 5.2
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/hfield_v2_vector_XY.png", 2400, 1500
    End With
    
    SelectTreeItem("2D/3D Results\H-Field\h-field (f=9) [1]\Abs")
    With ScalarPlot2D
        .Type "contour"
        .PlaneNormal "z"
        .PlaneCoordinate 30.0
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 5.2
        .DrawContourLines False
        .Banding False
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/hfield_v2_contour_XY.png", 2400, 1500
    End With

    ' --- 2.2 XZ Longitudinal Horizontal (Y = 5.08 mm) ---
    SelectTreeItem("2D/3D Results\H-Field\h-field (f=9) [1]")
    With VectorPlot2D
        .Type "arrows"
        .SetDensity 45
        .PlaneNormal "y"
        .PlaneCoordinate 5.08
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 5.2
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/hfield_v2_vector_XZ.png", 2400, 1500
    End With
    
    SelectTreeItem("2D/3D Results\H-Field\h-field (f=9) [1]\Abs")
    With ScalarPlot2D
        .Type "contour"
        .PlaneNormal "y"
        .PlaneCoordinate 5.08
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 5.2
        .DrawContourLines False
        .Banding False
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/hfield_v2_contour_XZ.png", 2400, 1500
    End With

    ' --- 2.3 YZ Longitudinal Vertical (X = 0 mm) ---
    SelectTreeItem("2D/3D Results\H-Field\h-field (f=9) [1]")
    With VectorPlot2D
        .Type "arrows"
        .SetDensity 45
        .PlaneNormal "x"
        .PlaneCoordinate 0.0
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 5.2
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/hfield_v2_vector_YZ.png", 2400, 1500
    End With
    
    SelectTreeItem("2D/3D Results\H-Field\h-field (f=9) [1]\Abs")
    With ScalarPlot2D
        .Type "contour"
        .PlaneNormal "x"
        .PlaneCoordinate 0.0
    End With
    With Plot2D3D
        .SetScalingMode "linear"
        .SetClampRange 0.0, 5.2
        .DrawContourLines False
        .Banding False
        .ExportImage "D:/CST Project/Slab_Waveguide_9GHz/img/hfield_v2_contour_YZ.png", 2400, 1500
    End With
End Sub
