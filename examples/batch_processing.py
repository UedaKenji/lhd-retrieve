"""
Example of batch processing multiple shots and channels.
"""

import pandas as pd
from pathlib import Path
from lhd_retrieve import LHDRetriever

def batch_retrieve_data(shots, channels, output_dir="data"):
    """
    Batch retrieve data for multiple shots and channels.
    
    Args:
        shots: List of shot numbers
        channels: List of channel names
        output_dir: Output directory for data files
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Initialize retriever
    retriever = LHDRetriever()
    
    # Process each shot
    for shot in shots:
        print(f"Processing shot {shot}...")
        shot_dir = output_path / f"shot_{shot}"
        shot_dir.mkdir(exist_ok=True)
        
        # Retrieve data for all channels
        results = retriever.retrieve_multiple_channels(
            shot=shot,
            channels=channels,
            time_range=(0.0, 20.0)  # First 20 seconds
        )
        
        # Save individual channel data
        for channel, data in results.items():
            csv_file = shot_dir / f"{channel}.csv"
            data.save_csv(str(csv_file))
            print(f"  Saved {channel} -> {csv_file}")
        
        # Create summary file
        summary_data = []
        for channel, data in results.items():
            summary_data.append({
                'shot': shot,
                'channel': channel,
                'points': len(data.data),
                'time_start': data.time[0] if len(data.time) > 0 else None,
                'time_end': data.time[-1] if len(data.time) > 0 else None,
                'data_min': data.data.min() if len(data.data) > 0 else None,
                'data_max': data.data.max() if len(data.data) > 0 else None,
                'units': data.units
            })
        
        summary_df = pd.DataFrame(summary_data)
        summary_file = shot_dir / "summary.csv"
        summary_df.to_csv(summary_file, index=False)
        print(f"  Summary -> {summary_file}")

def main():
    # Define shots and channels to process
    shots = [123456, 123457, 123458]  # Replace with actual shot numbers
    channels = [
        "THOMSON_TE",
        "THOMSON_NE", 
        "MAGNETICS_IP",
        "ECH_POWER"
    ]  # Replace with actual channel names
    
    try:
        batch_retrieve_data(shots, channels)
        print("Batch processing completed successfully")
    except Exception as e:
        print(f"Error during batch processing: {e}")

if __name__ == "__main__":
    main()