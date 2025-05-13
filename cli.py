#!/usr/bin/env python3
import argparse
from analyze import analyze_directory
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

def format_size(size_kb):
    """Format size in KB to a human-readable format."""
    if size_kb < 1024:
        return f"{size_kb:.2f}KB"
    elif size_kb < 1024 * 1024:
        return f"{size_kb/1024:.2f}MB"
    else:
        return f"{size_kb/(1024*1024):.2f}GB"

def create_metrics_table(metrics):
    """Create a rich table for basic metrics."""
    table = Table(box=box.ROUNDED, show_header=False, padding=(0, 2))
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Total Size", format_size(metrics['total_size_kb']))
    table.add_row("Total Files", str(metrics['total_files']))
    table.add_row("Total Lines", f"{metrics['total_lines']:,}")
    table.add_row("Functions", f"{metrics['total_functions']:,}")
    table.add_row("Classes", f"{metrics['total_classes']:,}")
    
    return table

def create_file_table(metrics):
    """Create a rich table for file distribution."""
    table = Table(box=box.ROUNDED, show_header=True, padding=(0, 2))
    table.add_column("Path", style="cyan")
    table.add_column("File", style="yellow")
    table.add_column("Lines", style="green", justify="right")
    table.add_column("Size", style="blue", justify="right")
    
    for folder in metrics['file_structure']:
        path = folder['path'] or 'Root'
        for file in folder['files']:
            table.add_row(
                path,
                file['name'],
                f"{file['lines']:,}",
                format_size(file['size_kb'])
            )
    
    return table

def print_stats(metrics):
    """Print formatted statistics from the analysis."""
    console.print("\n")
    
    # Title
    console.print(Panel.fit(
        "[bold blue]Code Statistics[/bold blue]",
        border_style="blue"
    ))
    
    # Basic Metrics
    console.print("\n[bold cyan]📊 Basic Metrics[/bold cyan]")
    console.print(create_metrics_table(metrics))
    
    # File Distribution
    console.print("\n[bold cyan]📁 File Distribution[/bold cyan]")
    console.print(create_file_table(metrics))
    
    console.print("\n")

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
            console.print(f"[red]Error: Path '{path}' does not exist[/red]", file=sys.stderr)
            sys.exit(1)
            
        metrics = analyze_directory(str(path))
        print_stats(metrics)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 