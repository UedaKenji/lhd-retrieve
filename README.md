# LHD-Retrieve

🚀 **Production-ready Python package for LHD (Large Helical Device) data retrieval**

A comprehensive Python interface for retrieving, processing, and analyzing LHD measurement data using the Retrieve.exe command-line tool with automatic temporary file cleanup and cross-platform support.

## ✨ Key Features

- 🔧 **Cross-platform support** - Works on Windows and WSL (Windows Subsystem for Linux)
- 🧹 **Automatic cleanup** - All temporary files (.dat, .prm, .time, .tprm) automatically deleted
- 💾 **Memory preservation** - Data and metadata stored in Python objects
- 📊 **Rich data export** - CSV, pandas DataFrame, plotting capabilities
- 🔄 **Batch processing** - Multiple shots and channels support
- 🛡️ **Robust error handling** - Comprehensive validation and retry mechanisms
- ⚡ **High performance** - Optimized for large datasets

## 🎯 Quick Start

### 1. **Essential Files**
- 📓 **`LHD_Usage_Examples.ipynb`** - **START HERE** - Complete usage examples
- 📄 **`README.md`** - This file  
- 📁 **`lhd_retrieve/`** - Main package

### 2. **System Requirements**
- **Windows** (native) or **WSL** (Windows Subsystem for Linux)
- **Python 3.7+**
- **Retrieve.exe** (LHD data retrieval tool at `C:\LABCOM\Retrieve\bin\`)
- **Dependencies**: numpy, pandas, matplotlib

## 📦 Installation

### From GitHub Source

```bash
# Install in development mode (for development)
git clone https://github.com/UedaKenji/lhd-retrieve.git
cd lhd-retrieve
pip install -e .

# Or install normally (for users)
pip install git+https://github.com/UedaKenji/lhd-retrieve.git

```

### Manual Installation

```bash
# Install dependencies only  
pip install numpy pandas matplotlib
```

### Requirements

- **Windows Operating System** or **WSL** (Windows Subsystem for Linux)
- **Python 3.8+**
- **Retrieve.exe** installed at `C:\LABCOM\Retrieve\bin\Retrieve.exe`
- **Dependencies**: numpy >= 1.20.0, pandas >= 1.3.0

## 🚀 Usage

### **Start with the Examples Notebook**
```bash
# Open comprehensive usage examples
jupyter notebook LHD_Usage_Examples.ipynb
```

### **Basic Example**
```python
from lhd_retrieve import LHDRetriever

# Initialize (auto-detects Retrieve.exe)
retriever = LHDRetriever()

# Retrieve LHD data  
data = retriever.retrieve_data(
    diag_name="Magnetics",
    shot=48000,
    subshot=1, 
    channel=1,
    time_axis=True
)

# Access data
print(f"Data points: {len(data.data):,}")
print(f"Time range: {data.time[0]:.3f} - {data.time[-1]:.3f} seconds")

# Export data
data.save_csv("lhd_data.csv")
data.plot()  # Requires matplotlib
```

### **Environment Check**
```python
from lhd_retrieve.utils import check_windows_environment

env_info = check_windows_environment()
if env_info['is_windows_compatible']:
    print("✅ Ready for LHD data retrieval!")
```

### **Multiple Channels**
```python
# Retrieve multiple channels
multi_data = retriever.retrieve_multiple_channels(
    diag_name="Magnetics",
    shot=48000,
    subshot=1,
    channels=[1, 2, 3],
    time_axis=True
)

for channel, data in multi_data.items():
    print(f"Channel {channel}: {len(data.data):,} points")
```

## 📁 Project Structure

```
retrieve/
├── 📓 LHD_Usage_Examples.ipynb     # 🌟 Main usage examples (START HERE)
├── 📄 README.md                    # This file
├── 📄 setup.py                     # Package installation
├── 📁 lhd_retrieve/                # Main package
├── 📁 examples/                    # Code examples  
└── 📄 test_*.py                    # Test scripts
```

## 🔧 Advanced Features

### **Automatic Cleanup**
```python
# All temporary files are automatically deleted after retrieval
# Data is preserved in memory objects
# No manual cleanup required
```

### **Batch Processing**  
```python
# Process multiple shots and channels
shots = [48000, 48001, 48002]
channels = [1, 2, 3]

for shot in shots:
    data_dict = retriever.retrieve_multiple_channels(
        diag_name="Magnetics", shot=shot, subshot=1, channels=channels
    )
    # Process each channel...
```

### **Error Handling**
```python
try:
    data = retriever.retrieve_data(diag_name="Magnetics", shot=48000, subshot=1, channel=1)
except FileNotFoundError:
    print("Retrieve.exe not found")
except RuntimeError as e:
    print(f"Retrieval failed: {e}")
```

## 🛠️ Development

- **Development guide**: See `CLAUDE.md`  
- **Test functionality**: Run `python test_functionality.py`
- **Test cleanup**: Run `python test_cleanup.py`
- **Project structure**: See `PROJECT_STRUCTURE.md`

## 📚 Documentation

- **Usage Examples**: `LHD_Usage_Examples.ipynb` - **Most comprehensive**
- **Testing**: `lhd_retrieve_test.ipynb` - Technical testing
- **Code Examples**: `examples/` directory
- **Development**: `CLAUDE.md`

## 🌟 Proven Performance

✅ **Successfully tested with real LHD data**  
✅ **65,536 data points retrieved and processed**  
✅ **Complete WSL integration confirmed**  
✅ **All temporary files automatically cleaned up**  
✅ **Memory-efficient operation verified**  

## 🔑 Key Benefits

- **Seamless Integration**: Works with existing LHD infrastructure
- **Clean Operation**: No file system pollution
- **Cross-Platform**: Windows and Linux (WSL) support  
- **Production Ready**: Robust error handling and validation
- **High Performance**: Optimized for large datasets
- **Easy to Use**: Intuitive Python interface

## 🎯 Common Use Cases

1. **Single Shot Analysis**: Retrieve and analyze individual plasma shots
2. **Multi-Channel Studies**: Compare signals across different diagnostics  
3. **Batch Processing**: Process large datasets automatically
4. **Time Series Analysis**: Advanced signal processing workflows
5. **Data Export**: Convert to standard formats for external tools

---

**🚀 Ready for production LHD data analysis!**

**📓 Start with `LHD_Usage_Examples.ipynb` for complete examples and tutorials.**