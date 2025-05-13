#!/usr/bin/env python3
import argparse
from analyze import analyze_directory
import sys
from pathlib import Path

def format_size(size_kb):
    """Format size in KB to a human-readable format."""
    if size_kb < 1024:
        return f"{size_kb:.2f}KB"
    elif size_kb < 1024 * 1024:
        return f"{size_kb/1024:.2f}MB"
    else:
        return f"{size_kb/(1024*1024):.2f}GB"

def print_stats(metrics):
    """Print formatted statistics from the analysis."""
    print("\n=== Code Statistics ===\n")
    
    # Basic Metrics
    print("📊 Basic Metrics:")
    print(f"Total Size: {format_size(metrics['total_size_kb'])}")
    print(f"Total Files: {metrics['total_files']}")
    print(f"Total Lines: {metrics['total_lines']:,}")
    
    # Code Structure
    print("\n🏗️  Code Structure:")
    print(f"Functions: {metrics['total_functions']:,}")
    print(f"Classes: {metrics['total_classes']:,}")
    
    # File Distribution
    print("\n📁 File Distribution:")
    for folder in metrics['file_structure']:
        path = folder['path'] or 'Root'
        print(f"\n{path}:")
        for file in folder['files']:
            print(f"  {file['name']} ({file['lines']:,} lines, {format_size(file['size_kb'])})")

def main():
    parser = argparse.ArgumentParser(description='Code Architecture System - Code Analysis Tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show code metrics and statistics')
    stats_parser.add_argument('--path', default='.', help='Path to analyze (default: current directory)')
    
    args = parser.parse_args()
    
    if args.command == 'stats':
        path = Path(args.path)
        if not path.exists():
            print(f"Error: Path '{path}' does not exist", file=sys.stderr)
            sys.exit(1)
            
        metrics = analyze_directory(str(path))
        print_stats(metrics)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 