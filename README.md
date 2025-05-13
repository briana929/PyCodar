# Codar: A Radar for Your Code
**A simple tool for auditing and understanding your codebase.**

Get started with:
```bash
pip install git+https://github.com/QuentinWach/codar.git
```

Below, you can see the result for Codar when we use `codar stats`. Note that Codar ingores files and directories specified in `.gitignore` and `.codarignore` (where you can optionally ignore gitignore).

```bash
📊 Basic Metrics
╭─────────────────────┬───────────╮
│  Total Size         │  21.30KB  │
│  Total Files        │  4        │
│  Total Directories  │  1        │
│  Total Lines        │  600      │
│  Code Lines         │  408      │
│  Comment Lines      │  15       │
│  Empty Lines        │  85       │
│  Functions          │  16       │
│  Classes            │  0        │
╰─────────────────────┴───────────╯

🌳 File Structure
📁 Root
├── 📄 README.md
├── 📄 analyze.py
│   ├── 🔸 count_functions_and_classes
│   ├── 🔸 get_file_size_kb
│   ├── 🔸 count_lines
│   ├── 🔸 analyze_directory
│   └── 🔸 generate_report
├── 📄 cli.py
│   ├── 🔸 extract_code_structure
│   ├── 🔸 create_structure_tree
│   ├── 🔸 parse_ignore_file
│   ├── 🔸 should_ignore
│   ├── 🔸 get_ignore_patterns
│   ├── 🔸 format_size
│   ├── 🔸 count_code_metrics
│   ├── 🔸 create_metrics_table
│   ├── 🔸 create_file_table
│   ├── 🔸 print_stats
│   └── 🔸 main
└── 📄 setup.py

📁 File Distribution
╭────────┬──────────────┬────────┬────────────┬─────────┬─────────┬───────────╮
│  Path  │  File        │  Code  │  Comments  │  Empty  │  Total  │     Size  │
├────────┼──────────────┼────────┼────────────┼─────────┼─────────┼───────────┤
│  Root  │  README.md   │     0  │         0  │      0  │     27  │   1.25KB  │
│  Root  │  setup.py    │    26  │         0  │      1  │     27  │   0.78KB  │
│  Root  │  cli.py      │   264  │        10  │     58  │    332  │  12.25KB  │
│  Root  │  analyze.py  │   118  │         5  │     26  │    149  │   4.94KB  │
╰────────┴──────────────┴────────┴────────────┴─────────┴─────────┴───────────╯
```