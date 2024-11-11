import json
from obspy import read

def process_seismic_data(file_path):
    # Read the MiniSEED file
    st = read(file_path)
    
    # Convert the stream to a dictionary format
    data = {
        "traces": [
            {
                "id": tr.id,
                "stats": tr.stats,
                "data": tr.data.tolist()
            } for tr in st
        ]
    }
    
    # Output the data as JSON
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    # Example usage
    input_file = "example.mseed"  # Replace with your file path
    output_json = process_seismic_data(input_file)
    print(output_json)

