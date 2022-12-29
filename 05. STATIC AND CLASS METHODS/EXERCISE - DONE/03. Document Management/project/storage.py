from project.category import Category
from project.topic import Topic
from project.document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category_obj = ''
        for el in self.categories:
            if el.id == category_id:
                category_obj = el

        category_obj.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_obj = ''
        for el in self.topics:
            if el.id == topic_id:
                topic_obj = el

        topic_obj.topic = new_topic
        topic_obj.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document_obj = ''
        for el in self.documents:
            if el.id == document_id:
                document_obj = el

        document_obj.file_name = new_file_name

    def delete_category(self, category_id):
        category_obj = ''
        for el in self.categories:
            if el.id == category_id:
                category_obj = el

        self.categories.remove(category_obj)

    def delete_topic(self, topic_id):
        topic_obj = ''
        for el in self.topics:
            if el.id == topic_id:
                topic_obj = el

        self.topics.remove(topic_obj)

    def delete_document(self, document_id):
        document_obj = ''
        for el in self.documents:
            if el.id == document_id:
                document_obj = el

        self.documents.remove(document_obj)

    def get_document(self, document_id):
        document_obj = ''
        for el in self.documents:
            if el.id == document_id:
                document_obj = el

        return document_obj

    def __repr__(self):
        result = []
        for el in self.documents:
            result.append(repr(el))
        return "\n".join(result)

# 86/100
# 95/100
# 100/100