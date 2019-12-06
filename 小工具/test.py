import os


def get_aapt():
    if "ANDROID_HOME" in os.environ:
        root_dir = os.path.join(os.environ["ANDROID_HOME"], "build-tools")
        for path, subdir, files in os.walk(root_dir):
            if "aapt.exe" in files:
                return os.path.join(path, "aapt.exe")
    else:
        return "ANDROID_HOME not exist"

print(get_aapt())