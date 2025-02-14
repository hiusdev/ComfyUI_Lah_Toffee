import random
from pathlib import Path


def get_random_video(folder_path):
    try:
        folder = Path(folder_path)

        # Check if the path exists and is a directory
        if not folder.exists() or not folder.is_dir():
            raise "❌ Invalid path or not a directory!"

        # Get a list of all video files in the folder
        video_files = (
            list(folder.glob("*.mp4"))
            + list(folder.glob("*.avi"))
            + list(folder.glob("*.mov"))
            + list(folder.glob("*.mkv"))
        )

        if not video_files:
            raise "❌ No video files found in the folder!"

        # Select a random video
        random_video = random.choice(video_files)

        # Return the full path
        return str(random_video.resolve())

    except Exception as e:
        return f"❌ Error while loading video: {str(e)}"


class LoadVideoRandom:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video_path": ("STRING", {"placeholder": "X://insert/path/"}),
                "seed": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "tooltip": "The random seed used for creating the noise.",
                    },
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("video",)
    FUNCTION = "load_videos"
    CATEGORY = "LahTeam/Video"

    def load_videos(self, video_path, seed):
        try:
            # Validate input (must be a non-empty string)
            if not video_path or not isinstance(video_path, str):
                raise "❌ Invalid video path!"

            # Call function to get a random video
            # video_path = r"{video_path}"
            random_video_path = get_random_video(video_path)

            return (random_video_path,)

        except Exception as e:
            return f"❌ Error while loading video: {str(e)}"
