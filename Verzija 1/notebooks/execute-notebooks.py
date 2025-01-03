from nbclient import NotebookClient
from nbformat import read

def execute_notebook(notebook_path):
    """Execute a Jupyter notebook and display the output."""
    with open(notebook_path) as f:
        notebook = read(f, as_version=4)
    
    # Create the client to execute the notebook
    client = NotebookClient(notebook)
    
    # Execute the notebook
    client.execute()

def run_notebooks_sequentially():
    """Execute all Jupyter notebooks in the specified order."""
    # List the notebooks in sequential order (ensure this order matches the notebooks in your directory)
    notebook_files = [
        'notebooks/1-data_input.ipynb',
        'notebooks/2-data_analysis.ipynb',
        'notebooks/3-statistika.ipynb',
        'notebooks/4-generator.ipynb',
        'notebooks/5-improvements.ipynb'
    ]

    # Execute each notebook in sequence
    for notebook_file in notebook_files:
        print(f"Executing {notebook_file}...")
        execute_notebook(notebook_file)
        print(f"{notebook_file} executed successfully!")

if __name__ == "__main__":
    run_notebooks_sequentially()