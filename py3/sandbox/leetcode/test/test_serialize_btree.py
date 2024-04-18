from unittest import TestCase

from leetcode.serialize_btree import Codec


class TestCodec(TestCase):
    def test_serde(self):
        ser = Codec()
        deser = Codec()

        #root = tree_array_to_treenode([5,3,6,2,4,None,None,1])
        root = [5,3,6,2,4,None,None,1]
        self.assertEqual(root, deser.deserialize(ser.serialize(root)))
        print(ser.serialize(root))
