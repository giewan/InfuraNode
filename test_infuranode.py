# test_infuranode.py
"""
Tests for InfuraNode module.
"""

import unittest
from infuranode import InfuraNode

class TestInfuraNode(unittest.TestCase):
    """Test cases for InfuraNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfuraNode()
        self.assertIsInstance(instance, InfuraNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfuraNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
