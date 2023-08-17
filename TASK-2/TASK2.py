import cv2

# Open the video file for reading
cap = cv2.VideoCapture("car.mp4")

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create VideoWriter objects for output videos
#slow_output = cv2.VideoWriter("SlowMotionVideo.mp4", cv2.VideoWriter_fourcc(*'mp4v'), int(fps / 2), (frame_width, frame_height))
#reverse_output = cv2.VideoWriter("ReverseVideo.mp4", cv2.VideoWriter_fourcc(*'mp4v'), int(fps), (frame_width, frame_height))
output = cv2.VideoWriter("SlowMotionReverseVideo.mp4", cv2.VideoWriter_fourcc(*'mp4v'), int(fps / 2), (frame_width, frame_height))

frame_list = []

# Read and store frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_list.append(frame)

# Slow motion
#for frame in frame_list:
#    output.write(frame)
#    cv2.imshow("SlowMotion&Reverse", frame)
#    if cv2.waitKey(int(1000 / (fps / 3))) & 0xFF == ord("q"):
#        break

# Reverse playback
for frame in reversed(frame_list):
    output.write(frame)
    cv2.imshow("SlowMotion&Reverse", frame)
    k = cv2.waitKey(9)
    if k == ord("q"):
        break

# Release resources
cap.release()
output.release()
cv2.destroyAllWindows()

print("Your Slow  Motion Reverse Video is ready")
