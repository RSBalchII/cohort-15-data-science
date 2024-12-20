import obspy
import json
import os
import time
from tqdm import tqdm

def convert_miniseed_to_json(miniseed_file, output_dir):
    try:
        st = obspy.read(miniseed_file)
        data = {
            'network': st[0].stats.network,
            'station': st[0].stats.station,
            'location': st[0].stats.location,
            'channel': st[0].stats.channel,
            'starttime': str(st[0].stats.starttime),
            'endtime': str(st[0].stats.endtime),
            'sampling_rate': st[0].stats.sampling_rate,
            'data': st[0].data.tolist()
        }
        output_file = os.path.join(output_dir, f"{os.path.basename(miniseed_file)}.json")
        with open(output_file, 'w') as f:
            json.dump(data, f)
        return True
    except Exception as e:
        print(f"Error processing {miniseed_file}: {str(e)}")
        return False

def process_files(input_dir, output_dir, num_files):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    miniseed_files = [f for f in os.listdir(input_dir) if f.endswith('.miniseed')]
    miniseed_files = miniseed_files[:num_files]  # Limit to the specified number of files
    
    start_time = time.time()
    
    for file in tqdm(miniseed_files, desc="Processing files"):
        file_path = os.path.join(input_dir, file)
        success = convert_miniseed_to_json(file_path, output_dir)
        if not success:
            print(f"Failed to process {file}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"\nProcessing complete.")
    print(f"Number of files processed: {len(miniseed_files)}")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Average time per file: {elapsed_time / len(miniseed_files):.2f} seconds")

if __name__ == "__main__":
    input_dir = "/path/to/miniseed/files"
    output_dir = "/path/to/output/json/files"
    num_files = 100  # Change this to the number of files you want to process
    
    process_files(input_dir, output_dir, num_files)
