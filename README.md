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
