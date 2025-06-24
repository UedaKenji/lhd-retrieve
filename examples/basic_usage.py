"""
Basic usage example for LHD data retrieval package.
"""

from lhd_retrieve import LHDRetriever
from lhd_retrieve.utils import check_windows_environment

def main():
    # Check if environment is compatible
    env_info = check_windows_environment()
    print("Environment Information:")
    for key, value in env_info.items():
        print(f"  {key}: {value}")
    
    # Initialize retriever
    # Option 1: Use default path (Retrieve.exe in PATH)
    try:
        retriever = LHDRetriever()
        print("\nUsing Retrieve.exe from PATH")
    except FileNotFoundError:
        # Option 2: Specify path to Retrieve.exe
        retrieve_path = r"C:\LHD\Retrieve"  # Adjust this path
        try:
            retriever = LHDRetriever(retrieve_path=retrieve_path)
            print(f"\nUsing Retrieve.exe from {retrieve_path}")
        except FileNotFoundError:
            print("\nRetrieve.exe not found. Please install or specify correct path.")
            return
    
    # Example parameters (replace with actual values)
    diag_name = "Mag"  # Diagnostic name
    shot_number = 139400  # Replace with actual shot number
    subshot_number = 1  # Sub-shot number (usually 1)
    channel_name = "32"  # Channel number or name
    
    try:
        # Show example command
        example_cmd = retriever.create_example_retrieval(diag_name, shot_number, subshot_number, channel_name)
        print(f"\nExample command: {example_cmd}")
        
        # Get available diagnostics
        print(f"\nGetting available diagnostics...")
        diagnostics = retriever.get_available_diagnostics()
        print(f"Available diagnostics: {diagnostics[:10]}...")  # Show first 10
        
        # Retrieve data for a specific channel
        print(f"\nRetrieving data for {diag_name} shot {shot_number}.{subshot_number} channel {channel_name}...")
        data = retriever.retrieve_data(
            diag_name=diag_name,
            shot=shot_number,
            subshot=subshot_number,
            channel=channel_name,
            time_axis=True,  # Generate time axis
            voltage_conversion=False  # Convert to voltage if needed
        )
        
        print(f"Retrieved {len(data.data)} data points")
        print(f"Time range: {data.time[0]:.3f} - {data.time[-1]:.3f} seconds")
        print(f"Data range: {data.data.min():.3f} - {data.data.max():.3f}")
        
        # Save data to CSV
        filename = f"{diag_name}_shot_{shot_number}_{subshot_number}_{channel_name}.csv"
        data.save_csv(filename)
        print(f"Data saved to {filename}")
        
        # Plot data (requires matplotlib)
        try:
            data.plot()
        except ImportError:
            print("Install matplotlib to enable plotting")
        
        # Retrieve multiple channels
        print("\nRetrieving multiple channels...")
        multi_channels = ["32", "33", "34"]  # Magnetic coil channels
        multi_data = retriever.retrieve_multiple_channels(
            diag_name=diag_name,
            shot=shot_number,
            subshot=subshot_number,
            channels=multi_channels,
            time_axis=True
        )
        
        for ch_name, ch_data in multi_data.items():
            print(f"Channel {ch_name}: {len(ch_data.data)} points")
        
    except Exception as e:
        print(f"Error during data retrieval: {e}")

if __name__ == "__main__":
    main()