#!/usr/bin/python
"""
Visualize all 3D point cloud files in .ply format using open3d within a directory

Import Information:
Install open3d in a conda environment with the following command
pip install open3d  or try conda install -c open3d-admin open3d

Run the file with the command
python visualize_ply.py
"""
import numpy as np
import open3d as o3d    
import os

def main():
	for file in os.listdir("."):
		if file.endswith(".ply"):
    		# Read the point cloud
			cloud = o3d.io.read_point_cloud(file)
			
			# Summary of the point cloud     
			print(cloud)    
			
			# Convert to numpy array
			print(np.asarray(cloud.points)) 
			
			# Visualize the point cloud
			o3d.visualization.draw_geometries([cloud])

			# Segment background plane to isolate plant
			plane_model, inliers = cloud.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=1000)
			[a,b,c,d] = plane_model
			print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

			inlier_cloud = cloud.select_by_index(inliers)
			inlier_cloud.paint_uniform_color([1.0, 0, 0])
			outlier_cloud = cloud.select_by_index(inliers, invert=True)

			# Write outlier_cloud to a file
			o3d.io.write_point_cloud(file+"_no background.ply", outlier_cloud)

			# Visualize segmentation of plane
			o3d.visualization.draw_geometries([outlier_cloud])
			


		else:
			continue
if __name__ == "__main__":
    main()
