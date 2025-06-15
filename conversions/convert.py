#!/usr/bin/env python3
"""
TFLite to ONNX conversion script for Home Assistant wake words.
"""
import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple


def get_repo_root() -> Path:
    """Get the repository root directory."""
    return Path("/github/workspace" if os.getenv("GITHUB_ACTIONS") else ".")


def find_tflite_files(repo_root: Path) -> List[Path]:
    """Find all TFLite files in the repository, excluding .git directories."""
    tflite_files = []
    for tflite_file in repo_root.glob("**/*.tflite"):
        if ".git" not in str(tflite_file):
            tflite_files.append(tflite_file)
    return sorted(tflite_files)


def find_tflite_without_onnx(repo_root: Path) -> List[Path]:
    """Find all TFLite files that don't have a corresponding ONNX file."""
    tflite_files = find_tflite_files(repo_root)
    missing_onnx = []
    
    for tflite_file in tflite_files:
        onnx_file = tflite_file.with_suffix(".onnx")
        if not onnx_file.exists():
            missing_onnx.append(tflite_file)
    
    return missing_onnx


def print_missing_onnx_files(repo_root: Path) -> None:
    """Print a clean list of TFLite files without corresponding ONNX files."""
    missing_files = find_tflite_without_onnx(repo_root)
    
    if not missing_files:
        print("✅ All TFLite files have corresponding ONNX files!")
        return
    
    print(f"\n📋 Found {len(missing_files)} TFLite files without corresponding ONNX files:")
    print("=" * 70)
    
    for tflite_file in missing_files:
        relative_path = tflite_file.relative_to(repo_root)
        print(f"  • {relative_path}")
    
    print("=" * 70)


def convert_file(tflite_path: Path, onnx_path: Path) -> bool:
    """Convert a single TFLite file to ONNX format."""
    cmd = [
        "python", "-m", "tf2onnx.convert",
        "--tflite", str(tflite_path),
        "--output", str(onnx_path),
        "--opset", "15"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            print(f"⚠️  Error converting {tflite_path.name}:")
            print(f"   stdout: {result.stdout}")
            print(f"   stderr: {result.stderr}")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"⚠️  Conversion timeout for {tflite_path.name}")
        return False
        print(f"⚠️  Conversion timeout for {tflite_path.name}")
        return False


def needs_conversion(tflite_file: Path, onnx_file: Path) -> bool:
    """Check if a TFLite file needs to be converted to ONNX."""
    if not onnx_file.exists():
        return True
    return False


def convert_all_files(repo_root: Path, sample_only: bool = False) -> Tuple[int, int]:
    """Convert TFLite files to ONNX format."""
    tflite_files = find_tflite_files(repo_root)
    converted_count = 0
    failed_count = 0
    
    for tflite_file in tflite_files:
        onnx_file = tflite_file.with_suffix(".onnx")
        
        if not needs_conversion(tflite_file, onnx_file):
            continue
        
        print(f"Converting {tflite_file.name}...")
        
        if convert_file(tflite_file, onnx_file):
            print(f"Created {onnx_file.name}")
            converted_count += 1
        else:
            print(f"Failed to convert {tflite_file.name}")
            failed_count += 1
            
        if sample_only:
            break
    
    return converted_count, failed_count


def main(sample=False):
    """Main function."""
    repo_root = get_repo_root()
    print_missing_onnx_files(repo_root)
    converted_count, failed_count = convert_all_files(repo_root, sample_only=sample)
    
    print(f"\nConverted: {converted_count}, Failed: {failed_count}")
    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", action="store_true")
    args = parser.parse_args()
    sys.exit(main(sample=args.sample))
