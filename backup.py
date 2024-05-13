import sys
import menu
import os
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDateEdit, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QIcon
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
            self.window = QWidget()
            self.window.setWindowTitle("BookShelf")
            self.window.setWindowIcon(QIcon("C:\\Users\\ASUS\\Downloads\\BookShelf.png"))
            pixmap = QPixmap("C:\\Users\\ASUS\\Downloads\\images.jpg")
            self.window.setFixedSize(pixmap.size())
            self.window.setStyleSheet("background-image: url('C:\\Users\\ASUS\\Downloads\\images.jpg')")
            label = QLabel(self.window)
            label.setPixmap(pixmap)
            label.setGeometry(0,0, pixmap .width(), pixmap.height())
            layout = QVBoxLayout()
            self.label = QLabel('Selamat Datang di BookShelf')
            font = QFont("Comic Sans MS", 15)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setFont(font)
            self.label.setStyleSheet("font-weight: bold; color: black;")
            self.login_button = QPushButton('Login')
            self.login_button.setFont(font)
            self.login_button.setStyleSheet(" color: pink; background-color: white;")
            self.regist_button = QPushButton('Buat Akun')
            self.regist_button.setFont(font)
            self.regist_button.setStyleSheet(" color: pink; background-color: white;")
            layout.addWidget(self.label)
            layout.addWidget(self.login_button)
            layout.addWidget(self.regist_button)
            self.login_button.clicked.connect(self.loginUI)
            self.regist_button.clicked.connect(self.registUI)
            self.window.setLayout(layout)
            self.window.show()
    def loginUI(self):
            self.window = QWidget()
            self.window.setWindowTitle("Login Ke BookShelf")
            pixmap = QPixmap("C:\\Users\\ASUS\\Downloads\\images.jpg")
            self.window.setFixedSize(pixmap.size())
            self.window.setStyleSheet("background-image: url('C:\\Users\\ASUS\\Downloads\\images.jpg')")
            label = QLabel(self.window)
            label.setPixmap(pixmap)
            label.setGeometry(0, 0, pixmap.width(), pixmap.height())
            loginlayout = QVBoxLayout()
            self.user_label = QLabel('Masukkan Username')
            font = QFont("Comic Sans MS", 15)
            self.user_label.setAlignment(Qt.AlignCenter)
            self.user_label.setFont(font)
            self.login_user = QLineEdit()
            self.user_pass = QLabel('Masukkan Password')
            self.user_pass.setAlignment(Qt.AlignCenter)
            self.user_pass.setFont(font)
            self.login_pass = QLineEdit()
            self.button = QPushButton("Login")
            self.button.setFont(font)
            loginlayout.addWidget(self.user_label)
            loginlayout.addWidget(self.login_user)
            loginlayout.addWidget(self.user_pass)
            loginlayout.addWidget(self.login_pass)
            loginlayout.addWidget(self.button)
            self.button.clicked.connect(self.check_login)
            self.window.setLayout(loginlayout)
            self.window.show()

    def check_login(self):
            # Get the username and password from the input fields
            username = self.login_user.text()
            password = self.login_pass.text()

            # Connect to the database and select the data from the account table
            self.conn = sqlite3.connect('account.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM account WHERE username=?", (username,))
            user_data = self.cursor.fetchone()

            # Check if there is any data in the user_data variable
            if user_data:
                    # If there is data, check if the provided username and password match
                    if username == user_data[1] and password == user_data[2]:
                            self.menuUI()
                    else:
                            QMessageBox.warning(self.window, "Login Gagal", "Username atau password salah. Silahkan coba lagi.")
            else:
                    QMessageBox.warning(self.window, "Login Gagal", "Username atau password salah. Silahkan coba lagi.")

            # Don't forget to close the database connection
            self.conn.close()
    def registUI(self):
            self.regist_window = QWidget()
            self.regist_window.setWindowTitle("Buat Akun BookShelf")
            pixmap = QPixmap("C:\\Users\\ASUS\\Downloads\\images.jpg")
            self.regist_window.setFixedSize(pixmap.size())
            self.regist_window.setStyleSheet("background-image: url('C:\\Users\\ASUS\\Downloads\\images.jpg')")
            label = QLabel(self.regist_window)
            label.setPixmap(pixmap)
            label.setGeometry(0, 0, pixmap.width(), pixmap.height())
            registlayout = QVBoxLayout()
            self.user_label = QLabel('Username')
            font = QFont("Comic Sans MS", 15)
            self.user_label.setAlignment(Qt.AlignCenter)
            self.user_label.setFont(font)
            self.regist_user = QLineEdit()
            self.user_pass = QLabel('Password')
            self.user_pass.setAlignment(Qt.AlignCenter)
            self.user_pass.setFont(font)
            self.regist_pass = QLineEdit()
            self.regist_confirm = QLabel('Confirm Password')
            self.regist_confirm.setAlignment(Qt.AlignCenter)
            self.regist_confirm.setFont(font)
            self.regist_confirm_pass = QLineEdit()
            self.regist_button = QPushButton("Buat Akun")
            self.regist_button.setFont(font)
            self.conn = sqlite3.connect('account.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                             CREATE TABLE IF NOT EXISTS account (
                                 id INTEGER PRIMARY KEY,
                                 username TEXT,
                                 password TEXT
                             )
                         ''')
            self.conn.commit()
            registlayout.addWidget(self.user_label)
            registlayout.addWidget(self.regist_user)
            registlayout.addWidget(self.user_pass)
            registlayout.addWidget(self.regist_pass)
            registlayout.addWidget(self.regist_confirm)
            registlayout.addWidget(self.regist_confirm_pass)
            registlayout.addWidget(self.regist_button)
            self.regist_button.clicked.connect(self.work)
            self.regist_window.setLayout(registlayout)
            self.regist_window.show()

    def work(self):
            username = self.regist_user.text()
            password = self.regist_pass.text()
            confirm_password = self.regist_confirm_pass.text()

            if not all([username.strip(), password.strip(), confirm_password.strip()]):
                    self.showMessage("Username dan Password Tidak Boleh Kosong")
                    return

            if len(username) < 8:
                    self.showMessage("Username minimal 8 karakter")
                    return

            if len(password) < 8:
                    self.showMessage("Password minimal 8 karakter")
                    return

            if password != confirm_password:
                    self.showMessage("Masukkan Password Yang Sesuai")
                    return

            try:
                    self.cursor.execute('INSERT INTO account (username, password) VALUES (?,?)', (username, password))
                    self.conn.commit()
                    self.regist_user.clear()
                    self.regist_pass.clear()
                    self.regist_confirm_pass.clear()
                    self.show_success_message()
            except sqlite3.Error as e:
                    print(f"Error: {e}")

    def showMessage(self, message):
            QMessageBox.information(self, "Error", message)

    def show_success_message(self):
            self.success_window = QWidget()
            self.success_window.setWindowTitle("Registrasi Berhasil")
            self.success_label = QLabel("Registrasi Berhasil")
            self.close_button = QPushButton("OK")
            layout = QVBoxLayout()
            layout.addWidget(self.success_label)
            layout.addWidget(self.close_button)
            self.close_button.clicked.connect(self.initUI)
            self.success_window.setLayout(layout)
            self.success_window.show()

    def menuUI(self):
            self.menu_window = QWidget()
            self.menu_window.setWindowTitle('Bookshelf')
            pixmap = QPixmap("C:\\Users\\ASUS\\Downloads\\images.jpg")
            self.menu_window.setFixedSize(pixmap.size())
            self.menu_window.setStyleSheet("background-image: url('C:\\Users\\ASUS\\Downloads\\images.jpg')")
            label = QLabel(self.menu_window)
            label.setPixmap(pixmap)
            label.setGeometry(0, 0, pixmap.width(), pixmap.height())
            menuLayout = QVBoxLayout()
            self.label = QLabel('Ingin Apa Hari Ini?')
            font = QFont("Comic Sans MS", 15)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setFont(font)
            self.pinjam = QPushButton('Peminjaman Buku')
            self.pinjam.setFont(font)
            self.kembalikan = QPushButton('Pengembalian Buku')
            self.kembalikan.setFont(font)
            self.cari = QPushButton('Informasi Buku')
            self.cari.setFont(font)
            menuLayout.addWidget(self.label)
            menuLayout.addWidget(self.pinjam)
            menuLayout.addWidget(self.kembalikan)
            menuLayout.addWidget(self.cari)
            self.pinjam.clicked.connect(self.borrowUI)
            self.kembalikan.clicked.connect(self.restoreUI)
            self.cari.clicked.connect(self.searchUI)
            self.menu_window.setLayout(menuLayout)
            self.menu_window.show()

    def booksdb(self):
            with sqlite3.connect('books.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    judul TEXT,
                    pengarang TEXT,
                    genre TEXT,
                    tahun_terbit INTEGER,
                )
            ''')
                    cursor.execute('''CREATE TABLE IF NOT EXISTS borrow (
                                        id INTEGER PRIMARY KEY,
                                        buku_id INTEGER NOT NULL,
                                        judul TEXT NOT NULL,
                                        status TEXT NOT NULL,
                                        tanggal_pinjam DATE ,
                                        tanggal_kembali DATE NOT NULL,
                                        FOREIGN KEY (buku_id) REFERENCES books (id))''')
                    books_data = [
                            ("Laut Bercerita", "Leila Salikha Chudori", "Fiksi", 2017),
                            ("Butterflies", "ALE", "Slice of Life, Fluff", 2021),
                            ("Sherlock Holmes, A Study in Scarlet – Penelusuran Benang Merah", "Arthur Conan Doyle", "Fiksi Kriminal", 1887),
                            ("Hello, Cello", "Nadia Ristavani", "Romance Comedy", 2022),
                            ("Akidah Akhlak", "Dewi Arlifah Cahyani", "Religi", 2022),
                            ("Buku Siswa Aktif dan Kreatif Belajar Kimia", "Nana Sutesna, dkk.", "Pelajaran", 2016)
                    ]
                    cursor.executemany('INSERT INTO books (judul, pengarang, genre, tahun_terbit) VALUES (?, ?, ?, ?)', books_data)
                    conn.commit()
    def borrowUI(self):
            self.borrow_window = QWidget()
            self.borrow_window.setWindowTitle('Peminjaman Buku')
            pixmap = QPixmap("C:\\Users\\ASUS\\Downloads\\images.jpg")
            self.borrow_window.setFixedSize(pixmap.size())
            self.borrow_window.setStyleSheet("background-image: url('C:\\Users\\ASUS\\Downloads\\images.jpg')")
            label = QLabel(self.borrow_window)
            label.setPixmap(pixmap)
            label.setGeometry(0, 0, pixmap.width(), pixmap.height())
            borrowlayout = QVBoxLayout()
            self.namabuku = QLabel('Judul Buku')
            font = QFont("Comic Sans MS", 15)
            self.namabuku.setAlignment(Qt.AlignCenter)
            self.namabuku.setFont(font)
            self.buku = QLineEdit()
            self.pinjam = QLabel('Tanggal Peminjaman')
            self.pinjam.setAlignment(Qt.AlignCenter)
            self.pinjam.setFont(font)
            self.tanggalpinjam = QDateEdit()
            self.tanggalpinjam.setFont(font)
            self.borrow_OK = QPushButton('Pinjam')
            self.borrow_OK.setFont(font)
            borrowlayout.addWidget(self.namabuku)
            borrowlayout.addWidget(self.buku)
            borrowlayout.addWidget(self.pinjam)
            borrowlayout.addWidget(self.tanggalpinjam)
            borrowlayout.addWidget(self.borrow_OK)
            self.borrow_OK.clicked.connect(self.peminjaman)
            self.borrow_window.setLayout(borrowlayout)
            self.borrow_window.show()

    def peminjaman(self):
            judul_buku = self.buku.text()
            tanggal_pinjam = self.tanggalpinjam.date().toString("dd-MM-yyyy")
            status = "Dipinjam"
            conn = sqlite3.connect('books.db')
            cursor = conn.cursor()

            try:
                    # Check if the book is already borrowed
                    cursor.execute("SELECT * FROM borrow WHERE judul=? AND status=?", (judul_buku, status))
                    books_data = cursor.fetchone()
                    if books_data:
                            QMessageBox.warning(self, "Peringatan",
                                                f"Buku {judul_buku} sedang dipinjam oleh peminjam lain.")
                            return

                    # Check if the book is available
                    cursor.execute(
                            "SELECT * FROM books WHERE judul=? AND NOT EXISTS (SELECT 1 FROM borrow WHERE judul=? AND status=?)",
                            (judul_buku, judul_buku, "Dipinjam"))
                    books_data = cursor.fetchone()
                    if not books_data:
                            QMessageBox.warning(self, "Peringatan", f"Buku {judul_buku} tidak tersedia untuk dipinjam.")
                            return

                    # Insert data peminjaman ke tabel borrow
                    cursor.execute(
                            "INSERT INTO borrow (judul, status, tanggal_pinjam, tanggal_kembali) VALUES (?, ?, ?, ?)",
                            (judul_buku, status, tanggal_pinjam, None))
                    conn.commit()

                    # Tampilkan pesan bahwa buku berhasil dipinjam
                    QMessageBox.information(self, "Sukses", f"Buku {judul_buku} berhasil dipinjam pada tanggal {tanggal_pinjam}")
                    self.menuUI()

            except sqlite3.Error as e:
                    QMessageBox.critical(self, "Error", f"Terjadi kesalahan saat memproses peminjaman: {e}")

            finally:
                    conn.close()

    def restoreUI(self):
            self.restore_window = QWidget()
            self.restore_window.setWindowTitle('Pengembalian Buku')
            pixmap = QPixmap("C:\\Users\\ASUS\\Downloads\\images.jpg")
            self.restore_window.setFixedSize(pixmap.size())
            self.restore_window.setStyleSheet("background-image: url('C:\\Users\\ASUS\\Downloads\\images.jpg')")
            label = QLabel(self.restore_window)
            label.setPixmap(pixmap)
            label.setGeometry(0, 0, pixmap.width(), pixmap.height())
            restorelayout = QVBoxLayout()
            self.namabuku = QLabel('Judul Buku')
            font = QFont("Comic Sans MS", 15)
            self.namabuku.setAlignment(Qt.AlignCenter)
            self.namabuku.setFont(font)
            self.buku = QLineEdit()
            self.kembali = QLabel('Tanggal Pengembalian')
            self.kembali.setAlignment(Qt.AlignCenter)
            self.kembali.setFont(font)
            self.tanggalkembali = QDateEdit()
            self.tanggalkembali.setFont(font)
            self.restore_OK = QPushButton('Kembalikan')
            self.restore_OK.setFont(font)
            restorelayout.addWidget(self.namabuku)
            restorelayout.addWidget(self.buku)
            restorelayout.addWidget(self.kembali)
            restorelayout.addWidget(self.tanggalkembali)
            restorelayout.addWidget(self.restore_OK)
            self.restore_OK.clicked.connect(self.pengembalian)
            self.restore_window.setLayout(restorelayout)
            self.restore_window.show()

    def pengembalian(self):
            judul_buku = self.buku.text()
            tanggal_kembali = self.tanggalkembali.date().toString("dd-MM-yyyy")  # Mengambil tanggal saat ini sebagai tanggal pengembalian
            status = "Tersedia"  # Status buku setelah pengembalian

            conn = sqlite3.connect('books.db')
            cursor = conn.cursor()

            try:
                    # Periksa apakah buku sedang dipinjam
                    cursor.execute("SELECT * FROM borrow WHERE judul=? AND status=?", (judul_buku, "Dipinjam"))
                    borrowed_book = cursor.fetchone()

                    if not borrowed_book:
                            QMessageBox.warning(self, "Peringatan", f"Buku {judul_buku} tidak sedang dipinjam.")
                            return

                    # Hapus data peminjaman dari tabel borrow
                    cursor.execute("DELETE FROM borrow WHERE id=?", (borrowed_book[0],))

                    # Update status buku menjadi "Tersedia" di tabel books
                    cursor.execute("UPDATE borrow SET status=? WHERE judul=?", (status, judul_buku))

                    conn.commit()
                    QMessageBox.information(self, "Sukses",
                                            f"Buku {judul_buku} berhasil dikembalikan pada tanggal {tanggal_kembali}")
                    self.menuUI()

            except sqlite3.Error as e:
                    QMessageBox.critical(self, "Error", f"Terjadi kesalahan saat memproses pengembalian: {e}")

            finally:
                    conn.close()

    def searchUI(self):
            self.search_window = QWidget()
            self.search_window.setWindowTitle('Pencarian Buku')
            pixmap = QPixmap("C:\\Users\\ASUS\\Downloads\\images.jpg")
            self.search_window.setFixedSize(pixmap.size())
            self.search_window.setStyleSheet("background-image: url('C:\\Users\\ASUS\\Downloads\\images.jpg')")
            label = QLabel(self.search_window)
            label.setPixmap(pixmap)
            label.setGeometry(0, 0, pixmap.width(), pixmap.height())
            searchlayout = QVBoxLayout()
            self.namabuku = QLabel('Judul Buku')
            font = QFont("Comic Sans MS", 15)
            self.namabuku.setAlignment(Qt.AlignCenter)
            self.namabuku.setFont(font)
            self.buku = QLineEdit()
            self.searchbutton = QPushButton('Cari')
            self.searchbutton.setFont(font)
            searchlayout.addWidget(self.namabuku)
            searchlayout.addWidget(self.buku)
            searchlayout.addWidget(self.searchbutton)
            self.searchbutton.clicked.connect(self.pencarian)
            self.search_window.setLayout(searchlayout)
            self.search_window.show()

    def pencarian(self):
            judul_buku = self.buku.text()

            conn = sqlite3.connect('books.db')
            cursor = conn.cursor()

            try:
                    # Lakukan pencarian berdasarkan judul buku
                    cursor.execute("SELECT * FROM books WHERE judul=?", (judul_buku,))
                    book_data = cursor.fetchone()

                    if book_data:
                            # Jika buku ditemukan, tampilkan informasinya
                            status = self.get_book_status(judul_buku)
                            QMessageBox.information(self.search_window, "Informasi Buku",
                                                    f"Judul: {book_data[1]}\n"
                                                    f"Pengarang: {book_data[2]}\n"
                                                    f"Genre: {book_data[3]}\n"
                                                    f"Tahun Terbit: {book_data[4]}\n"
                                                    f"Status: {status}")
                            self.menuUI()
                    else:
                            # Jika buku tidak ditemukan, tampilkan pesan
                            QMessageBox.warning(self.search_window, "Peringatan",
                                                f"Buku dengan judul {judul_buku} tidak ditemukan.")

            except sqlite3.Error as e:
                    QMessageBox.critical(self.search_window, "Error",
                                         f"Terjadi kesalahan saat melakukan pencarian: {e}")

            finally:
                    conn.close()

    def get_book_status(self, judul_buku):
            conn = sqlite3.connect('books.db')
            cursor = conn.cursor()

            try:
                    # Cek status buku berdasarkan judul
                    cursor.execute("SELECT status FROM borrow WHERE judul=? AND status=?", (judul_buku, "Dipinjam"))
                    borrowed_book = cursor.fetchone()

                    if borrowed_book:
                            return "Dipinjam"
                    else:
                            return "Tersedia"

            except sqlite3.Error as e:
                    print(f"Error: {e}")

            finally:
                    conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
