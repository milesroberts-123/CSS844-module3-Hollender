# CSS844-module3-Hollender

s00_HollenderImageAnalysis_v8.ipynb - Contains python code to pre-process point clouds. Author: Miles Roberts
* Downsamples original point cloud
* Uses open3d to identify the wall of the cardboard box background, describes it with a plane equation (ax + by + cz + d = 0)
* Crops out plant based on the location of this plane
* Converts point cloud to a binary image by dividing up the bounding box of the plant into voxels, then labeling voxels that contain at least one point.
* Uses `skimage` to skeletonize the binary image
* Uses `sknw` to build a network based on this binary image
