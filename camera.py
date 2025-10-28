# Run v4l2 command to set pixelformat in Y16
import subprocess
subprocess.run([
    "v4l2-ctl",
    "--device=/dev/video2",
    "--set-fmt-video=width=160,height=120,pixelformat='Y16 '"
])
device = "/dev/video2"

# Query basic info
info = subprocess.run(["v4l2-ctl", "--device", device, "--all"],
                      capture_output=True, text=True)
print(info.stdout)

import cv2
import numpy as np

cap = cv2.VideoCapture('/dev/video2')
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' '))
cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)



while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Reinterpret raw 16-bit data
    data = frame.view(np.uint16)

    # For display only (do NOT use for quantitative analysis)
    data = cv2.normalize(data, None, 0, 255, cv2.NORM_MINMAX)
    data = np.uint8(data)
    data = cv2.applyColorMap(data, cv2.COLORMAP_INFERNO)
    disp = cv2.resize(data, None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST)

    # Use CV2 to show image
    cv2.imshow('Lepton Radiometric (Y16)', disp)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()