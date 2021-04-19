# CSS844-module3-Hollender

s00_HollenderImageAnalysis_v8.ipynb - Contains python code to pre-process point clouds. Author: Miles Roberts
* Downsamples original point cloud
* Uses open3d to identify the wall of the cardboard box background, describes it with a plane equation (ax + by + cz + d = 0)
* Crops out plant based on the location of this plane
* Converts point cloud to a binary image by dividing up the bounding box of the plant into voxels, then labeling voxels that contain at least one point.
* Uses `skimage` to skeletonize the binary image
* Uses `sknw` to build a network based on this binary image

20210414_JK_Angle_Estimation.ipynb - Jupyter Notebook for estimating branch angles from .txt MDS skeletons outputted by plantscan3d. Author: Joshua Kaste
* imports nodes from skeleton
* Identifies branch points, and for each one:
* Extracts relevant node coordinates and finds vectors describing the basal axis and the two vectors coming off of the branch
* Figures out which one is 'branching', sets the other one as the reference, and then calculates the angle between them

20210414_JK_Angle_Estimation_V2.ipynb - Jupyter Notebook for estimating branch angles from .txt MDS skeletons outputted by plantscan3d. Author: Joshua Kaste
* same as above, except begins with code for loading in an Arabidopsis point cloud, segmenting the plant out, and then exporting it as an .asc file for processing in plantscan3D

20210415_JK_Attempting_Registration.ipynb - Jupyter notebook that demonstrates a first-pass attempt at global registration of Arabidopsis point clouds. Author: Joshua Kaste, with significant code from Miles Roberts
* Uses a variant of Miles' procedure and DBSCAN to isolate arabidopsis point cloud from surroundings in an original .ply image (note: not automated, requires checking)
* Does necessary pre-processing through the open3D library and then carries out RANSAC global registration + visualization of the result

2021-4-16_2D_Branch_Angle_Estimation_JK - Jupyter notebook for estimating branch angles using branch/tip point objects from plantCV. Author: Joshua Kaste, with pre-processing code by Thilani Jayakody
* identifies relevant branch/tip nodes and coordinates from plantCV output.
* Assumes location of base of branch based on x,y coordinates
* From this, identifies relevant branching point
* Calculates vectors describing the two segments coming off of the branching point
* Calculates angle between these vectors and reports out
* 
20210419_JK_Automated_2D_Branch_Angle_Estimator.ipynb - Jupyter notebook that builds on the 2021-4_16_2D_Branch_Angle_Estimation_JK
notebook by automating the extraction of Arabidopsis branches from an initial input image. Author: Joshua Kaste, with plantCV preprocessing code from Thilani Jayakody
* takes an input file of a picture of a blank piece of paper with green arabidopsis stems attached to it and segments these stems into individual images
* Uses methodology described in 2021-4-16_2D_Branch_Angle_Estimation_JK to calculate all branch angles and reports them out
