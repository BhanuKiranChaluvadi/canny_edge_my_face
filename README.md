## canny_edge_my_face
Grabs images from computer camera and apply canny edge filter to the frames


Clone https://github.com/BhanuKiranChaluvadi/canny_edge_my_face

##	Dependency
pkg: cv_camera Clone https://github.com/OTL/cv_camera into your workspace


## Launch

```
roslaunch canny_edge_my_face edge_detection.launch
```

## commnets: 
edges = cv2.Canny(cv2_img,100,200)
tune last two parameters/arguments based on lighting conditions.
