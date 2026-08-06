# GitHub User Analyzer

Analyze any GitHub profile using the GitHub REST API.

This project retrieves information from a GitHub user, performs several analyses, generates visualizations and exports the results automatically.

---

## Features

- Retrieve user information
- Retrieve public repositories
- Compute repository statistics
- Analyze programming languages
- Generate CSV datasets
- Generate JSON reports
- Generate high-quality visualizations

---

## Project Structure

```text
github-user-analyzer/

├── src/
│   ├── api.py
│   ├── analysis.py
│   ├── dataframe_analysis.py
│   ├── output.py
│   ├── transform.py
│   ├── visualization.py
│   └── main.py
│
├── output/
│   ├── repositories.csv
│   ├── report.json
│   └── figures/
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your_username/github-user-analyzer.git
```

Go to the project

```bash
cd github-user-analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python src/main.py torvalds
```

Example

```bash
python src/main.py 2Maikel3
```

---

## Output

The project automatically generates

```
output/

report.json

repositories.csv

figures/
```

---

## Generated Figures

- Top Starred Repositories
- Top Forked Repositories
- Stars by Language
- Forks by Language
- Repositories by Language
- Repository Size
- Repository Creation Timeline
- Watchers Distribution

---

## Technologies

- Python
- Requests
- Pandas
- Matplotlib
- GitHub REST API

---

## Skills Demonstrated

- REST APIs
- Data Extraction
- ETL
- Data Cleaning
- Data Analysis
- Data Visualization
- Software Architecture
- Python Best Practices

---

## Future Improvements

- GitHub authentication
- Pagination
- CLI using argparse
- Logging
- Unit testing
- GitHub Actions
- Interactive dashboard
- Export to Excel
- Export to SQLite

---

## License

MIT