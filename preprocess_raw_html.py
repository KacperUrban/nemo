from nemo_curator.utils.file_utils import get_all_files_paths_under
from nemo_curator.datasets import DocumentDataset
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
from concurrent.futures import ProcessPoolExecutor
import argparse


parser = argparse.ArgumentParser(
                    prog='FromHtmlToJsonl',
                    description='Process html to jsonl format')

parser.add_argument('filename')
args = parser.parse_args()
filename = args.filename
print(filename)
files = get_all_files_paths_under('data/raw/' + filename)
files = files[1:]

print(f"Number of files: {len(files)}")



def process_file(file: str) -> str:
    data_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        soup = BeautifulSoup(text, 'html.parser')
        data_dict['text'] = soup.get_text()
    return json.dumps(data_dict)

output_file = 'data/ready/' + filename + '.jsonl'

with ProcessPoolExecutor() as executor:
    results = list(tqdm(executor.map(process_file, files), total=len(files)))

with open(output_file, 'a') as output:
    output.write('\n'.join(results) + '\n')