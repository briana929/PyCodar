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
import ast

console = Console()

def format_size(size_kb):
    """Format size in KB to a human-readable format."""
    if size_kb < 1024:
        return f"{size_kb:.2f}KB"
    elif size_kb < 1024 * 1024:
        return f"{size_kb/1024:.2f}MB"
    else:
        return f"{size_kb/(1024*1024):.2f}GB"

def count_code_metrics(file_path: str) -> tuple:
    """Count code, comments, and empty lines in a Python file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Parse the file
        tree = ast.parse(content)
        
        # Count comments
        comment_lines = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
                comment_lines.add(node.lineno)
        
        # Count total lines and empty lines
        total_lines = len(content.splitlines())
        empty_lines = sum(1 for line in content.splitlines() if not line.strip())
        
        # Calculate code lines (total - comments - empty)
        code_lines = total_lines - len(comment_lines) - empty_lines
        
        return code_lines, len(comment_lines), empty_lines
    except:
        return 0, 0, 0

def create_metrics_table(metrics):
    """Create a rich table for basic metrics."""
    table = Table(box=box.ROUNDED, show_header=False, padding=(0, 2))
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Total Size", format_size(metrics['total_size_kb']))
    table.add_row("Total Files", str(metrics['total_files']))
    table.add_row("Total Directories", str(metrics['total_directories']))
    table.add_row("Total Lines", f"{metrics['total_lines']:,}")
    table.add_row("Code Lines", f"{metrics['total_code_lines']:,}")
    table.add_row("Comment Lines", f"{metrics['total_comment_lines']:,}")
    table.add_row("Empty Lines", f"{metrics['total_empty_lines']:,}")
    table.add_row("Functions", f"{metrics['total_functions']:,}")
    table.add_row("Classes", f"{metrics['total_classes']:,}")
    
    return table

def create_file_table(metrics):
    """Create a rich table for file distribution."""
    table = Table(box=box.ROUNDED, show_header=True, padding=(0, 2))
    table.add_column("Path", style="cyan")
    table.add_column("File", style="yellow")
    table.add_column("Code", style="green", justify="right")
    table.add_column("Comments", style="blue", justify="right")
    table.add_column("Empty", style="magenta", justify="right")
    table.add_column("Total", style="green", justify="right")
    table.add_column("Size", style="blue", justify="right")
    
    for folder in metrics['file_structure']:
        path = folder['path'] or 'Root'
        for file in folder['files']:
            table.add_row(
                path,
                file['name'],
                f"{file['code_lines']:,}",
                f"{file['comment_lines']:,}",
                f"{file['empty_lines']:,}",
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
            
        # Enhance the metrics with code analysis
        metrics = analyze_directory(str(path))
        
        # Add code metrics
        total_code_lines = 0
        total_comment_lines = 0
        total_empty_lines = 0
        total_directories = len([d for d in metrics['file_structure'] if d['path']])
        
        for folder in metrics['file_structure']:
            for file in folder['files']:
                if file['name'].endswith('.py'):
                    code_lines, comment_lines, empty_lines = count_code_metrics(
                        str(Path(folder['path']) / file['name']) if folder['path'] else file['name']
                    )
                    file['code_lines'] = code_lines
                    file['comment_lines'] = comment_lines
                    file['empty_lines'] = empty_lines
                    total_code_lines += code_lines
                    total_comment_lines += comment_lines
                    total_empty_lines += empty_lines
                else:
                    file['code_lines'] = 0
                    file['comment_lines'] = 0
                    file['empty_lines'] = 0
        
        metrics['total_code_lines'] = total_code_lines
        metrics['total_comment_lines'] = total_comment_lines
        metrics['total_empty_lines'] = total_empty_lines
        metrics['total_directories'] = total_directories
        
        print_stats(metrics)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 