# LHD Retrieve Package - Project Structure

## 📁 Directory Structure

```
retrieve/
├── 📄 README.md                    # Main project documentation
├── 📄 CLAUDE.md                    # Development guidance for Claude Code
├── 📄 setup.py                     # Package installation configuration
├── 📄 PROJECT_STRUCTURE.md         # This file - project organization guide
│
├── 📓 LHD_Usage_Examples.ipynb     # 🌟 Main usage examples notebook
├── 📓 lhd_retrieve_test.ipynb      # Comprehensive testing notebook
│
├── 📁 lhd_retrieve/                # 🎯 Main package directory
│   ├── 📄 __init__.py              # Package initialization
│   ├── 📄 core.py                  # Core LHDRetriever and LHDData classes
│   ├── 📄 utils.py                 # Utility functions and environment checks
│   └── 📄 wsl_utils.py             # WSL-specific utilities
│
├── 📁 examples/                    # 📋 Code examples directory
│   ├── 📄 basic_usage.py           # Basic usage example
│   ├── 📄 batch_processing.py      # Batch processing example
│   └── 📄 lhd_magnetics_example.py # Magnetics-specific example
│
├── 📁 tests/ (reserved)            # 🧪 Future unit tests directory
│
├── 📄 test_functionality.py        # Cross-platform functionality test
├── 📄 test_cleanup.py              # Temporary file cleanup test
│
└── 📁 docs/ (reserved)             # 📚 Future documentation directory
```

## 🎯 Key Files

### 🌟 Primary Usage Files
- **`LHD_Usage_Examples.ipynb`** - **START HERE** - Complete usage examples
- **`README.md`** - Project overview and quick start guide
- **`lhd_retrieve/`** - Main package code

### 🔧 Development Files
- **`CLAUDE.md`** - Development guidance for Claude Code
- **`test_*.py`** - Automated test scripts
- **`lhd_retrieve_test.ipynb`** - Comprehensive testing notebook

### 📋 Documentation Files  
- **`PROJECT_STRUCTURE.md`** - This file
- **`examples/`** - Standalone code examples

## 🚀 Quick Start Guide

### 1. For New Users
```bash
# Start with the main usage examples notebook
jupyter notebook LHD_Usage_Examples.ipynb
```

### 2. For Developers
```bash
# Review development guidance
cat CLAUDE.md

# Run functionality tests
python test_functionality.py
python test_cleanup.py
```

### 3. For Package Installation
```bash
# Install in development mode
pip install -e .

# Or install dependencies only
pip install numpy pandas matplotlib
```

## 📚 File Descriptions

### Core Package (`lhd_retrieve/`)

| File | Purpose | Key Components |
|------|---------|----------------|
| `__init__.py` | Package initialization | Exports main classes and utilities |
| `core.py` | Main functionality | `LHDRetriever`, `LHDData` classes |
| `utils.py` | Utility functions | Environment checks, path detection |
| `wsl_utils.py` | WSL support | WSL detection, Windows tool access |

### Examples (`examples/`)

| File | Purpose | Use Case |
|------|---------|----------|
| `basic_usage.py` | Simple usage | Single channel retrieval |
| `batch_processing.py` | Batch operations | Multiple shots/channels |
| `lhd_magnetics_example.py` | Magnetics-specific | Detailed magnetics workflow |

### Testing

| File | Purpose | Coverage |
|------|---------|----------|
| `test_functionality.py` | Core functionality | Cross-platform testing |
| `test_cleanup.py` | File management | Temporary file cleanup |
| `lhd_retrieve_test.ipynb` | Interactive testing | Comprehensive test suite |

## 🔄 Workflow Recommendations

### For Data Analysis
1. **Start**: `LHD_Usage_Examples.ipynb`
2. **Customize**: Copy examples and modify parameters
3. **Scale up**: Use batch processing examples
4. **Advanced**: Implement custom analysis workflows

### For Development
1. **Setup**: Read `CLAUDE.md` and `README.md`
2. **Test**: Run `test_functionality.py`
3. **Develop**: Modify core package files
4. **Validate**: Run full test suite

### For Deployment
1. **Install**: `pip install -e .`
2. **Configure**: Set up Windows/WSL environment
3. **Test**: Verify with real LHD data
4. **Deploy**: Integrate with analysis pipelines

## 🧹 Maintenance

### Regular Cleanup
- Temporary test files are automatically cleaned up
- Generated CSV files should be managed by user
- Log files (if any) should be rotated

### Version Control
- Keep core package files under version control
- Exclude generated data files (`*.csv`, `*.dat`, etc.)
- Include documentation and examples

### Updates
- Core functionality: Update `lhd_retrieve/` files
- Documentation: Update notebooks and README
- Examples: Add new use cases to `examples/`

## 🎯 Project Goals

✅ **Achieved**
- Cross-platform LHD data retrieval (Windows/WSL)
- Automatic temporary file cleanup
- Comprehensive usage examples
- Robust error handling
- Memory-efficient data processing

🔄 **Future Enhancements**
- Unit test suite with pytest
- API documentation with Sphinx
- Performance optimization for large datasets
- Additional diagnostic support
- GUI interface development

## 📞 Support

- **Documentation**: Start with `LHD_Usage_Examples.ipynb`
- **Development**: See `CLAUDE.md`
- **Issues**: Create GitHub issues (if repository exists)
- **Examples**: Check `examples/` directory

---

**Ready for production LHD data analysis! 🚀**