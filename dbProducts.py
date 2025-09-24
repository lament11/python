#라이브러리를 사용하면 선언부가 늘어난다!
import sqlite3
import random

class ProductDatabase:
    def __init__(self, db_name="MyProduct.db"):
        self.db_name = db_name
        self.create_table()
    
    def create_table(self):
        """제품 테이블 생성"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Products (
                        productID INTEGER PRIMARY KEY,
                        productName TEXT NOT NULL,
                        productPrice INTEGER NOT NULL
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            print(f"테이블 생성 중 오류 발생: {e}")

    def insert_product(self, product_name, product_price):
        """제품 추가"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO Products (productName, productPrice)
                    VALUES (?, ?)
                ''', (product_name, product_price))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"제품 추가 중 오류 발생: {e}")
            return None

    def update_product(self, product_id, product_name=None, product_price=None):
        """제품 정보 수정"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                updates = []
                values = []
                if product_name is not None:
                    updates.append("productName = ?")
                    values.append(product_name)
                if product_price is not None:
                    updates.append("productPrice = ?")
                    values.append(product_price)
                
                if updates:
                    values.append(product_id)
                    query = f"UPDATE Products SET {', '.join(updates)} WHERE productID = ?"
                    cursor.execute(query, values)
                    conn.commit()
                    return cursor.rowcount > 0
                return False
        except sqlite3.Error as e:
            print(f"제품 수정 중 오류 발생: {e}")
            return False

    def delete_product(self, product_id):
        """제품 삭제"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Products WHERE productID = ?", (product_id,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"제품 삭제 중 오류 발생: {e}")
            return False

    def select_all_products(self):
        """모든 제품 조회"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Products")
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"제품 조회 중 오류 발생: {e}")
            return []

    def generate_sample_data(self, count=100000):
        """샘플 데이터 생성"""
        product_types = ['스마트폰', '노트북', '태블릿', 'TV', '냉장고', '세탁기', '에어컨', '청소기']
        brands = ['삼성', 'LG', '애플', '샤오미', '소니', '파나소닉', '다이슨']
        
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                for _ in range(count):
                    product_name = f"{random.choice(brands)} {random.choice(product_types)} {random.randint(1, 100)}"
                    product_price = random.randint(100000, 5000000)
                    cursor.execute('''
                        INSERT INTO Products (productName, productPrice)
                        VALUES (?, ?)
                    ''', (product_name, product_price))
                conn.commit()
            print(f"{count}개의 샘플 데이터가 성공적으로 생성되었습니다.")
        except sqlite3.Error as e:
            print(f"샘플 데이터 생성 중 오류 발생: {e}")

def main():
    # 데이터베이스 인스턴스 생성
    db = ProductDatabase()
    
    # 샘플 데이터 생성
    db.generate_sample_data()
    
    # 데이터 조회 예시
    print("\n처음 5개 제품 조회:")
    products = db.select_all_products()[:5]
    for product in products:
        print(f"ID: {product[0]}, 이름: {product[1]}, 가격: {product[2]:,}원")

if __name__ == "__main__":
    main()