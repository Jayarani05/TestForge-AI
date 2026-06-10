import os
import shutil
from git import Repo
from uuid import uuid4
from pathlib import Path


def clone_repository(repo_url: str) -> str:
    """
    Clone a GitHub repository to a temporary folder.
    
    Args:
        repo_url: GitHub repository URL
        
    Returns:
        Path to cloned repository
        
    Raises:
        ValueError: If URL is invalid or clone fails
    """
    
    # Validate URL
    if not repo_url or not isinstance(repo_url, str):
        raise ValueError("Invalid repository URL provided")
    
    if "github.com" not in repo_url.lower():
        raise ValueError("Only GitHub repositories are supported")
    
    # Generate unique folder name
    repo_id = str(uuid4())
    
    # Use temp_repos directory in Backend folder
    base_path = Path(__file__).parent.parent.parent
    temp_dir = base_path / "temp_repos"
    
    # Create temp_repos directory if it doesn't exist
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    clone_path = temp_dir / repo_id
    
    try:
        # Clone repository
        Repo.clone_from(repo_url, str(clone_path))
        return str(clone_path)
    
    except Exception as e:
        # Clean up on failure
        if clone_path.exists():
            shutil.rmtree(clone_path)
        
        error_msg = str(e)
        if "Authentication" in error_msg or "permission" in error_msg.lower():
            raise ValueError(f"Authentication failed. Check repository URL and access permissions.")
        elif "not found" in error_msg.lower() or "404" in error_msg:
            raise ValueError(f"Repository not found. Check the URL: {repo_url}")
        else:
            raise ValueError(f"Failed to clone repository: {error_msg}")