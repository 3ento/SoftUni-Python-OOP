# from project.category import Category
# from project.document import Document
# from project.storage import Storage
# from project.topic import Topic
#
# import unittest
#
#
# class TestDocumentManagement(unittest.TestCase):
#     def setUp(self):
#         self.c = Category(1, "C")
#         self.t = Topic(1, "T", "C:\\user")
#         self.d = Document(1, 1, 1, "D")
#         self.s = Storage()
#
#     def test_category_init(self):
#         self.assertEqual(self.c.id, 1)
#         self.assertEqual(self.c.name, "C")
#
#     def test_document_init(self):
#         self.assertEqual(self.d.id, 1)
#         self.assertEqual(self.d.category_id, 1)
#         self.assertEqual(self.d.topic_id, 1)
#         self.assertEqual(self.d.file_name, "D")
#         self.assertEqual(self.d.tags, [])
#
#     def test_document_from_insances(self):
#         doc = Document.from_instances(1, self.c, self.t, "Doc")
#         self.assertEqual(doc.id, 1)
#         self.assertEqual(doc.category_id, 1)
#         self.assertEqual(doc.topic_id, 1)
#         self.assertEqual(doc.file_name, "Doc")
#         self.assertEqual(doc.tags, [])
#
#     def test_topic_init(self):
#         self.assertEqual(self.t.id, 1)
#         self.assertEqual(self.t.id, 1)
#         self.assertEqual(self.t.storage_folder, "C:\\user")
#
#
#
#
# if __name__ == "__main__":
#     unittest.main()