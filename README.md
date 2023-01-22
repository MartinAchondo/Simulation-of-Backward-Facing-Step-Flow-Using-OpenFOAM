## Simulation of Backward Facing Step Flow Using OpenFOAM

Every folder have the model used:
<pre> 
├── 2d_k_omega                   # 2D k-Omega SST
├── 2d_laminar_simple            # 2D Laminar 
├── 3d_k_epsilon                 # 3D k-epsilon
├── 3d_les_smagorinsky           # 3D LES Smagorinsky
├── 3d_les_wale                  # 3D LES WALE
├── Geometries
└── Meshes
</pre>

Every model have the same file structure:
<pre> 
├── ...
├── Model                      
│   ├── 0                     
│   ├── constant                            
│   ├── postCodes
│   ├── system
│   ├── Allclean
│   ├── Allrun            
│   ├── fieldsValues.py                       
│   └── plots.ipynb                
└── ...
</pre>
