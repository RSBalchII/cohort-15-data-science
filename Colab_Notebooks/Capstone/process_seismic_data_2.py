import obspy  # For reading MiniSEED format seismic data
import json  # For JSON data manipulation
import os  # For handling file paths and directories
import time  # For time measurement
from tqdm import tqdm  # For progress bar in loops

def convert_miniseed_to_json(miniseed_file, output_dir):
    try:
        # Read MiniSEED file using obspy
        st = obspy.read(miniseed_file)
        # Extract relevant data and metadata from the first Trace object
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
        # Determine the output file path
        output_file = os.path.join(output_dir, f"{os.path.basename(miniseed_file)}.json")
        # Write data to JSON file
        with open(output_file, 'w') as f:
            json.dump(data, f)
        return True
    except Exception as e:
        # Print error message if something goes wrong
        print(f"Error processing {miniseed_file}: {str(e)}")
        return False

def process_directory(input_dir, output_dir, max_files):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get list of all MiniSEED files and limit to max_files
    miniseed_files = [f for f in os.listdir(input_dir) if f.endswith('.miniseed')]
    miniseed_files = miniseed_files[:max_files]

    start_time = time.time()  # Start time for measuring process time

    # Process each MiniSEED file
    for file in tqdm(miniseed_files, desc="Processing files"):
        file_path = os.path.join(input_dir, file)
        success = convert_miniseed_to_json(file_path, output_dir)
        if not success:
            print(f"Failed to process {file}")

    end_time = time.time()  # End time for measuring process time
    elapsed_time = end_time - start_time

    # Print processing summary
    print(f"\nProcessing complete.")
    print(f"Number of files processed: {len(miniseed_files)}")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Average time per file: {elapsed_time / len(miniseed_files):.2f} seconds")

if __name__ == "__main__":
    # Specify input directory, output directory, and maximum number of files to process
    input_dir = "/path/to/miniseed/files"
    output_dir = "/path/to/output/json/files"
    max_files = 1  # The maximum number of files you want to process

    # Process the directory and convert files
    process_directory(input_dir, output_dir, max_files)