"""
Example: Retrieving LHD Magnetics data using proper Retrieve.exe format.
Command format: Retrieve DiagName ShotNo SubShotNo ChNo-Name [FileName] [options]
"""

from lhd_retrieve import LHDRetriever
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Initialize retriever (uses C:\LABCOM\Retrieve\bin by default)
    retriever = LHDRetriever()
    
    # Example 1: Single magnetic coil data
    print("=== Example 1: Single Magnetic Coil ===")
    try:
        data = retriever.retrieve_data(
            diag_name="Mag",      # Magnetics diagnostic
            shot=139400,          # Shot number
            subshot=1,            # Sub-shot (usually 1)
            channel="32",         # Magnetic coil channel
            time_axis=True,       # Generate time axis (-T option)
            voltage_conversion=False  # Don't convert to voltage
        )
        
        print(f"Retrieved {len(data.data)} data points")
        print(f"Time range: {data.time[0]:.6f} - {data.time[-1]:.6f} seconds")
        print(f"Data range: {data.data.min():.3e} - {data.data.max():.3e}")
        
        # Save data
        data.save_csv("mag_coil_32.csv")
        
        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(data.time, data.data)
        plt.xlabel('Time (s)')
        plt.ylabel('Magnetic Field')
        plt.title(f'Magnetics Shot {data.metadata["shot"]}.{data.metadata["subshot"]}, Channel {data.metadata["channel"]}')
        plt.grid(True)
        plt.show()
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Multiple magnetic coils
    print("\n=== Example 2: Multiple Magnetic Coils ===")
    try:
        channels = ["32", "33", "34"]  # Multiple coil channels
        multi_data = retriever.retrieve_multiple_channels(
            diag_name="Mag",
            shot=139400,
            subshot=1,
            channels=channels,
            time_axis=True
        )
        
        # Plot multiple channels
        plt.figure(figsize=(12, 8))
        for i, (channel, data) in enumerate(multi_data.items()):
            plt.subplot(len(channels), 1, i+1)
            plt.plot(data.time, data.data, label=f'Channel {channel}')
            plt.ylabel('Magnetic Field')
            plt.legend()
            plt.grid(True)
            if i == len(channels) - 1:
                plt.xlabel('Time (s)')
        
        plt.suptitle(f'Magnetics Shot 139400 - Multiple Channels')
        plt.tight_layout()
        plt.show()
        
        # Save each channel
        for channel, data in multi_data.items():
            filename = f"mag_shot_139400_ch_{channel}.csv"
            data.save_csv(filename)
            print(f"Saved {filename}")
            
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Voltage conversion
    print("\n=== Example 3: With Voltage Conversion ===")
    try:
        data_voltage = retriever.retrieve_data(
            diag_name="Mag",
            shot=139400,
            subshot=1,
            channel="32",
            time_axis=True,
            voltage_conversion=True  # Convert to voltage (-V option)
        )
        
        print(f"Voltage data range: {data_voltage.data.min():.6f} - {data_voltage.data.max():.6f} V")
        data_voltage.save_csv("mag_coil_32_voltage.csv")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()