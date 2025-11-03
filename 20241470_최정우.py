class Node:
    """단순 연결 리스트의 노드"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next



class Book:
    """도서 정보를 저장하는 클래스"""
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.book_id} | {self.title} | {self.author} | {self.year}"



class LinkedList:
    """단순 연결 리스트 구조"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, book):
        """리스트 끝에 도서 추가"""
        new_node = Node(book)
        if self.is_empty():
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def find_by_title(self, title):
        """책 제목으로 도서 검색"""
        cur = self.head
        while cur:
            if cur.data.title == title:
                return cur.data
            cur = cur.next
        return None

    def find_pos_by_title(self, title):
        """책 제목으로 노드 위치(이전 노드) 찾기"""
        prev = None
        cur = self.head
        while cur:
            if cur.data.title == title:
                return prev
            prev = cur
            cur = cur.next
        return None

    def remove_by_title(self, title):
        """책 제목으로 도서 삭제"""
        if self.is_empty():
            return False
        cur = self.head

         
        if cur.data.title == title:
            self.head = cur.next
            return True

     
        prev = self.find_pos_by_title(title)
        if prev and prev.next:
            prev.next = prev.next.next
            return True
        return False

    def display_books(self):
        """현재 등록된 모든 도서 출력"""
        if self.is_empty():
            print("현재 등록된 도서가 없습니다.")
            return
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next



class BookManagement:
    """도서 관리 기능 및 사용자 인터페이스"""
    def __init__(self):
        self.books = LinkedList()

  
    def add_book(self):
        try:
            book_id = input("책 번호: ").strip()
            title = input("책 제목: ").strip()
            author = input("저자: ").strip()
            year = input("출판 연도: ").strip()

         
            cur = self.books.head
            while cur:
                if cur.data.book_id == book_id:
                    print("이미 존재하는 책 번호입니다.")
                    return
                cur = cur.next

            new_book = Book(book_id, title, author, year)
            self.books.append(new_book)
            print("도서 추가 성공!")
        except Exception as e:
            print("도서 추가 실패:", e)

   
    def remove_book(self):
        title = input("삭제할 책 제목: ").strip()
        if not title:
            print("잘못된 입력입니다.")
            return
        success = self.books.remove_by_title(title)
        if success:
            print("도서 삭제 성공!")
        else:
            print("해당 제목의 도서를 찾을 수 없습니다.")

    
    def search_book(self):
        title = input("조회할 책 제목: ").strip()
        if not title:
            print("잘못된 입력입니다.")
            return
        book = self.books.find_by_title(title)
        if book:
            print(f"조회 결과: {book}")
        else:
            print("해당 제목의 도서를 찾을 수 없습니다.")

    
    def display_all(self):
        print("\n=== 전체 도서 목록 ===")
        self.books.display_books()

    
    def run(self):
        while True:
            print("\n=========================")
            print("      도서 관리 프로그램")
            print("=========================")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로)")
            print("3. 도서 조회 (책 제목으로)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")
            print("=========================")
            choice = input("원하는 메뉴를 선택하세요: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_all()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택하세요.")



if __name__ == "__main__":
    manager = BookManagement()
    manager.run()