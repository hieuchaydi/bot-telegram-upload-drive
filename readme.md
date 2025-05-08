# 📸 Telegram to Google Drive Bot

Bot này cho phép bạn **gửi ảnh qua Telegram**, và ảnh sẽ **được lưu trực tiếp lên Google Drive** theo ngày. Không lưu ảnh vào máy tính cá nhân.

---

## ✅ Tính năng

- Nhận ảnh từ Telegram tự động.
- Tạo thư mục theo ngày (`YYYY-MM-DD`) trên Google Drive.
- Upload ảnh trực tiếp lên Drive, không lưu tạm vào ổ đĩa.
- Gửi lại đường dẫn chia sẻ ảnh cho người dùng.

---

## 🛠️ Yêu cầu

- Python 3.8 trở lên
- Tài khoản Google Drive
- Bot Telegram và token truy cập
- File `credentials.json` từ Google API Console

---

## 📦 Hướng dẫn cài đặt

### 1. Tạo thư mục và môi trường ảo

```bash
mkdir telegram-drive-bot
cd telegram-drive-bot
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
sau đó :pip install -r requirements.txt
🤖 Tạo Bot Telegram
Truy cập @BotFather trên Telegram.

Gõ lệnh /newbot, đặt tên và username cho bot.

BotFather sẽ trả về một TOKEN. Lưu token này để cấu hình trong file bot.py.

🔐 Tạo Google OAuth Credentials
Truy cập: https://console.cloud.google.com/

Tạo project mới → Vào API & Services → Enable APIs & Services

Tìm và bật Google Drive API

Vào Credentials → Create Credentials → Chọn OAuth Client ID

Application type: Desktop App

Tải về file credentials.json

Đặt credentials.json trong thư mục gốc của dự án.

🚀 Chạy bot
bash
Sao chép
Chỉnh sửa
python bot.py
Lần đầu chạy sẽ mở trình duyệt yêu cầu đăng nhập tài khoản Google.

Sau khi xác thực, file token.json sẽ được tạo để lưu thông tin truy cập.

🧠 Cấu trúc thư mục dự án
bash
Sao chép
Chỉnh sửa
.
├── bot.py                # Mã bot Telegram
├── drive_uploader.py     # Xử lý Google Drive
├── credentials.json      # OAuth credentials từ Google (do bạn tải)
├── token.json            # Tự động tạo sau khi xác thực
├── requirements.txt      # Danh sách thư viện
└── README.md             # Tài liệu hướng dẫn
⚠️ Lưu ý
KHÔNG public các file credentials.json hoặc token.json lên GitHub.

Nếu gặp lỗi WinError 32, có thể do ảnh đang bị mở hoặc bị ghi cùng lúc → kiểm tra lại việc mở file trong chương trình khác.

Đảm bảo bot có quyền truy cập thư mục Google Drive.

🧩 Kế hoạch phát triển (tùy chọn)
✅ Hỗ trợ thêm video, PDF

✅ Giới hạn người gửi ảnh (chỉ cho phép admin)

✅ Giao diện web quản lý ảnh (dashboard)

📬 Liên hệ
Nếu bạn cần trợ giúp thêm, hãy tạo Issue trong GitHub repo.
lưu ý đoạn code :creds = flow.run_console() ở file drive_uploader.py nếu bạn chưa deploy mà chỉ chạy local thì chuyển doạn
 creds = flow.run_local_server(port=0) về để chạy local nhé 
