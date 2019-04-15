# camera-calibration
Camera calibration out of MP4 file to gain camera matrix and distortion coefficients.

# How to use
1. Create MP4 video file via your camera filming `Calibration_Grid.png` from different angles.
2. Save your video file to cloned repository.
3. ```python Calibration.py your_video_file.mp4```
4. Wait for the process to finish, camera matrinx and distortion coefficients will be printed.

# Example
Clone the repository:
```
git clone https://github.com/Maxim-CE/camera-calibration.git
cd camera-calibration
python Calibration.py WebCam.mp4
```
For calibrating `WebCam.mp4` you will receive the following output:
```
Camera matrix:
fx: 461.055785824
fy: 462.176713292
cx: 309.244676708
cy: 260.948393979

Distortion coefficients:
k1: 0.842991751189
k2: -7.12936636647
p1: 0.00304382955902
p2: 0.000725384370557
k3: 20.295080211
```
