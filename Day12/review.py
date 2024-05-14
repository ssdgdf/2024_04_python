class Book:
    def __init__(self,title,writer):
        self.name = title
        self.writer = writer
    def dispaly_info(self):
        return f"책 제목:{self.name}  작가:{self.writer}"


b = Book("해리포터","롤랑")
print(b.dispaly_info())
