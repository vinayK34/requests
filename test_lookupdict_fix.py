#!/usr/bin/env python3
"""
Test script to verify the LookupDict fix works correctly.
This demonstrates that __getitem__, __getattr__, and get() now use the same storage.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from requests.structures import LookupDict

def test_lookupdict_consistency():
    """Test that LookupDict now consistently uses the same storage for all access methods."""
    
    # Create a LookupDict instance
    ld = LookupDict("test_lookup")
    
    # Set some values using dictionary-style assignment
    ld['key1'] = 'value1'
    ld['key2'] = 'value2'
    
    print("Testing LookupDict consistency...")
    print(f"ld['key1'] = {ld['key1']}")
    print(f"ld.key1 = {ld.key1}")
    print(f"ld.get('key1') = {ld.get('key1')}")
    
    # Test that all access methods return the same value
    assert ld['key1'] == ld.key1 == ld.get('key1') == 'value1'
    print("✓ Dictionary, attribute, and get() access all return the same value")
    
    # Test unknown key behavior (should return None, not raise KeyError)
    print(f"ld['unknown'] = {ld['unknown']}")
    print(f"ld.unknown = {ld.unknown}")
    print(f"ld.get('unknown') = {ld.get('unknown')}")
    
    # All should return None for unknown keys
    assert ld['unknown'] is None
    assert ld.unknown is None
    assert ld.get('unknown') is None
    print("✓ Unknown keys consistently return None")
    
    # Test setting via attribute access
    ld.new_key = 'new_value'
    print(f"After setting ld.new_key = 'new_value':")
    print(f"ld['new_key'] = {ld['new_key']}")
    print(f"ld.new_key = {ld.new_key}")
    print(f"ld.get('new_key') = {ld.get('new_key')}")
    
    assert ld['new_key'] == ld.new_key == ld.get('new_key') == 'new_value'
    print("✓ Attribute assignment works consistently with dictionary access")
    
    print("\nAll tests passed! LookupDict now properly implements dict contract.")

if __name__ == "__main__":
    test_lookupdict_consistency()