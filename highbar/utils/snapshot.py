"""Snapshot manifest for tracking dataset versions."""

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class FileSnapshot(BaseModel):
    """Snapshot of a single file."""

    path: str
    size: int
    checksum: str
    modified: str


class DatasetSnapshot(BaseModel):
    """Snapshot of a dataset."""

    name: str
    version: str
    created: str
    files: List[FileSnapshot]
    metadata: Dict[str, Any]


class SnapshotManifest:
    """Manage snapshots and manifests of legal datasets."""

    def __init__(self, manifest_path: str, **kwargs: Any) -> None:
        """Initialize snapshot manifest.

        Args:
            manifest_path: Path to manifest file
            **kwargs: Additional configuration parameters
        """
        self.manifest_path = Path(manifest_path)
        self.config = kwargs
        self.snapshots: List[DatasetSnapshot] = []
        self._load_manifest()

    def _load_manifest(self) -> None:
        """Load manifest from file."""
        if self.manifest_path.exists():
            with open(self.manifest_path, "r") as f:
                data = json.load(f)
                self.snapshots = [DatasetSnapshot(**s) for s in data.get("snapshots", [])]

    def _save_manifest(self) -> None:
        """Save manifest to file."""
        self.manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.manifest_path, "w") as f:
            data = {"snapshots": [s.model_dump() for s in self.snapshots]}
            json.dump(data, f, indent=2)

    def compute_checksum(self, file_path: Path) -> str:
        """Compute SHA256 checksum of a file.

        Args:
            file_path: Path to file

        Returns:
            Checksum string
        """
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def create_snapshot(
        self,
        name: str,
        version: str,
        paths: List[str],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> DatasetSnapshot:
        """Create a new dataset snapshot.

        Args:
            name: Dataset name
            version: Version string
            paths: List of file paths to include
            metadata: Optional metadata

        Returns:
            Created DatasetSnapshot
        """
        files = []
        for path_str in paths:
            path = Path(path_str)
            if path.exists() and path.is_file():
                files.append(
                    FileSnapshot(
                        path=str(path),
                        size=path.stat().st_size,
                        checksum=self.compute_checksum(path),
                        modified=datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
                    )
                )

        snapshot = DatasetSnapshot(
            name=name,
            version=version,
            created=datetime.now().isoformat(),
            files=files,
            metadata=metadata or {},
        )

        self.snapshots.append(snapshot)
        self._save_manifest()
        return snapshot

    def get_snapshot(self, name: str, version: str) -> Optional[DatasetSnapshot]:
        """Get a specific snapshot.

        Args:
            name: Dataset name
            version: Version string

        Returns:
            DatasetSnapshot if found
        """
        for snapshot in self.snapshots:
            if snapshot.name == name and snapshot.version == version:
                return snapshot
        return None

    def verify_snapshot(self, snapshot: DatasetSnapshot) -> Dict[str, bool]:
        """Verify integrity of a snapshot.

        Args:
            snapshot: Snapshot to verify

        Returns:
            Dictionary mapping file paths to verification status
        """
        results = {}
        for file_snap in snapshot.files:
            path = Path(file_snap.path)
            if not path.exists():
                results[file_snap.path] = False
            else:
                current_checksum = self.compute_checksum(path)
                results[file_snap.path] = current_checksum == file_snap.checksum
        return results
