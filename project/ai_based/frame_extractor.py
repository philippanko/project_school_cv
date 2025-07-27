import cv2
import os
import argparse
import math

def extract_frames(video_path, output_dir, num_frames):
    # Open the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Couldn't open video.")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_frames / fps

    print(f"Video FPS: {fps}")
    print(f"Total frames: {total_frames}")
    print(f"Duration: {duration:.2f} seconds")

    if num_frames > total_frames:
        print(f"Warning: Requested {num_frames} frames, but video has only {total_frames}.")

    # Calculate frame indexes to capture
    step = total_frames / num_frames
    frame_indices = [int(i * step) for i in range(num_frames)]

    os.makedirs(output_dir, exist_ok=True)
    saved = 0

    for i in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break

        if i in frame_indices:
            filename = os.path.join(output_dir, f"frame_{saved:04d}.jpg")
            cv2.imwrite(filename, frame)
            saved += 1

            if saved >= num_frames:
                break

    cap.release()
    print(f"Saved {saved} frames to {output_dir}")

if __name__ == "__main__":
    video_path = "viideo — сделано в Clipchamp.mp4"
    output_dir = "dataset/train/background"
    num_frames = 40
    extract_frames(video_path, output_dir, num_frames)
