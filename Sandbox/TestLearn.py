from agentforge.modules.LearnDoc import FileProcessor

filepath = "Book of Thoth.pdf"


def learn_file(file_path):
    fp = FileProcessor()
    fp.process_file(file_path)


if __name__ == "__main__":
    learn_file(filepath)
