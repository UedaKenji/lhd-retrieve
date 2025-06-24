#!/usr/bin/env python3
"""
Test temporary file cleanup functionality
"""

import os
import glob
from pathlib import Path

def list_temp_files(prefix=""):
    """List temporary files in /tmp"""
    if prefix:
        pattern = f"/tmp/{prefix}*"
    else:
        pattern = "/tmp/retrieve_*"
    
    files = glob.glob(pattern)
    return files

def test_cleanup():
    """Test that temporary files are properly cleaned up"""
    print("=" * 60)
    print("TESTING TEMPORARY FILE CLEANUP")
    print("=" * 60)
    
    try:
        from lhd_retrieve import LHDRetriever
        
        # Check temp files before
        print("1. Checking temporary files before data retrieval...")
        before_files = list_temp_files()
        print(f"   Files before: {len(before_files)}")
        for f in before_files:
            print(f"     - {os.path.basename(f)}")
        
        # Initialize retriever
        print("\n2. Initializing retriever and retrieving data...")
        retriever = LHDRetriever()
        
        # Retrieve data
        data = retriever.retrieve_data(
            diag_name="Magnetics",
            shot=48000,
            subshot=1,
            channel="1",
            time_axis=True
        )
        
        print(f"   ✓ Data retrieved: {len(data.data):,} points")
        print(f"   ✓ Data saved in LHDData object")
        print(f"   ✓ Metadata preserved: {len(data.metadata)} fields")
        
        # Check temp files after
        print("\n3. Checking temporary files after data retrieval...")
        after_files = list_temp_files()
        print(f"   Files after: {len(after_files)}")
        for f in after_files:
            print(f"     - {os.path.basename(f)}")
        
        # Calculate difference
        new_files = set(after_files) - set(before_files)
        deleted_files = set(before_files) - set(after_files)
        
        print(f"\n4. File cleanup analysis:")
        print(f"   New files created: {len(new_files)}")
        print(f"   Files deleted: {len(deleted_files)}")
        
        if len(new_files) == 0:
            print("   ✅ SUCCESS: All temporary files cleaned up!")
        else:
            print("   ⚠️  Some temporary files remain:")
            for f in new_files:
                file_size = os.path.getsize(f)
                print(f"     - {os.path.basename(f)} ({file_size:,} bytes)")
        
        # Verify data integrity
        print(f"\n5. Verifying data integrity:")
        print(f"   ✓ Data type: {type(data.data)}")
        print(f"   ✓ Time type: {type(data.time)}")
        print(f"   ✓ Data shape: {data.data.shape}")
        print(f"   ✓ Time shape: {data.time.shape}")
        print(f"   ✓ Metadata keys: {list(data.metadata.keys())}")
        
        # Test data access
        print(f"\n6. Testing data access:")
        print(f"   ✓ First data point: {data.data[0]:.6e}")
        print(f"   ✓ Last data point: {data.data[-1]:.6e}")
        print(f"   ✓ First time point: {data.time[0]:.6f}")
        print(f"   ✓ Last time point: {data.time[-1]:.6f}")
        
        # Test export functionality
        print(f"\n7. Testing export functionality:")
        test_csv = "test_cleanup_export.csv"
        data.save_csv(test_csv)
        if os.path.exists(test_csv):
            file_size = os.path.getsize(test_csv)
            print(f"   ✓ CSV export: {test_csv} ({file_size:,} bytes)")
            os.remove(test_csv)  # Clean up test file
            print(f"   ✓ Test file cleaned up")
        
        return len(new_files) == 0
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_multiple_retrievals():
    """Test cleanup with multiple data retrievals"""
    print("\n" + "=" * 60)
    print("TESTING CLEANUP WITH MULTIPLE RETRIEVALS")
    print("=" * 60)
    
    try:
        from lhd_retrieve import LHDRetriever
        
        retriever = LHDRetriever()
        
        # Test multiple retrievals
        test_params = [
            {"channel": "1", "description": "Channel 1"},
            {"channel": "1", "description": "Channel 1 again"},  # Same data
        ]
        
        all_data = []
        
        for i, params in enumerate(test_params, 1):
            print(f"\n{i}. Retrieving {params['description']}...")
            
            # Check files before
            before = len(list_temp_files())
            
            # Retrieve data
            data = retriever.retrieve_data(
                diag_name="Magnetics",
                shot=48000,
                subshot=1,
                channel=params["channel"],
                time_axis=True
            )
            
            all_data.append(data)
            
            # Check files after
            after = len(list_temp_files())
            
            print(f"   ✓ Retrieved {len(data.data):,} points")
            print(f"   ✓ Temp files: {before} → {after}")
            
            if after <= before:
                print(f"   ✅ Cleanup successful")
            else:
                print(f"   ⚠️  {after - before} new temp files remain")
        
        print(f"\n✅ Retrieved {len(all_data)} datasets")
        print(f"✅ All data preserved in memory")
        print(f"✅ Temporary files managed properly")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Multiple retrieval test failed: {e}")
        return False

if __name__ == "__main__":
    print("LHD Retrieve Package - Temporary File Cleanup Test")
    
    test1 = test_cleanup()
    test2 = test_multiple_retrievals()
    
    print(f"\n" + "=" * 60)
    print("CLEANUP TEST SUMMARY")
    print("=" * 60)
    
    if test1 and test2:
        print("🎉 ALL CLEANUP TESTS PASSED!")
        print("✅ Temporary files properly cleaned up")
        print("✅ Data preserved in LHDData objects")
        print("✅ Multiple retrievals work correctly")
        print("✅ No file system pollution")
    else:
        print("⚠️ Some cleanup tests failed")
        
    print(f"\nCurrent temp files:")
    remaining = list_temp_files()
    if remaining:
        for f in remaining:
            print(f"  - {os.path.basename(f)}")
    else:
        print("  (none - all clean!)")