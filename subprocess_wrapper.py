# type:ignore
import subprocess
import platform
from typing import Any


class SubprocessWrapper:
    def call(*args, **kwargs) -> int:
        if type(args[0]) == list and platform.system() == "Windows":
            if args[0][0].startswith("./tari"):
                args[0][0] += ".exe"
            elif args[0][0] == "npm":
                args[0][0] += ".cmd"
            return subprocess.call(" ".join(args[0]), *args[1:], **kwargs)
        else:
            return subprocess.call(*args, **kwargs)

    def Popen(*args, **kwargs) -> subprocess.Popen[Any]:
        if type(args[0]) == list and platform.system() == "Windows":
            if args[0][0].startswith("./tari"):
                args[0][0] += ".exe"
            elif args[0][0] == "npm":
                args[0][0] += ".cmd"
            return subprocess.Popen(" ".join(args[0]), *args[1:], **kwargs)
        else:
            return subprocess.Popen(*args, **kwargs)

    def run(*args, **kwargs) -> subprocess.CompletedProcess[str]:
        if type(args[0]) == list and platform.system() == "Windows":
            if args[0][0].startswith("./tari"):
                args[0][0] += ".exe"
            elif args[0][0] == "npm":
                args[0][0] += ".cmd"
            return subprocess.run(" ".join(args[0]), *args[1:], **kwargs)
        else:
            return subprocess.run(*args, **kwargs)


SubprocessWrapper.call(["cargo", "--version"])
