import os
import shutil
from git import Repo
from uuid import uuid4


TEMP_DIR = "temp_repos"


def clone_repository(repo_url: str):

    os.makedirs(TEMP_DIR, exist_ok=True)

    repo_id = str(uuid4())

    clone_path = os.path.join(
        TEMP_DIR,
        repo_id
    )

    Repo.clone_from(
        repo_url,
        clone_path
    )

    return clone_path