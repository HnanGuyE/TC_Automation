from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Truy cập trang web
url = "https://www.nike.com/vn/w/air-force-1-shoes-5sj3yzy7ok"
driver.get(url)

try:
    # Đợi tối đa 15s để sản phẩm xuất hiện
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.product-container'))
    )

    # Tìm các sản phẩm
    products = driver.find_elements(By.CSS_SELECTOR, '.product-container')
    print(f"🟢 Tìm thấy {len(products)} sản phẩm")

    for idx, product in enumerate(products, 1):
        try:
            name = product.find_element(By.CSS_SELECTOR, '.product-title a').text.strip()
        except:
            name = 'N/A'

        try:
            price = product.find_element(By.CSS_SELECTOR, '.ty-price-num').text.strip()
        except:
            price = 'N/A'

        try:
            sold = product.find_element(By.CSS_SELECTOR, '.product-view-and-rating .ty-right').text.strip()
        except:
            sold = 'N/A'

        print(f'\n📦 Sản phẩm #{idx}')
        print(f'Tên: {name}')
        print(f'Giá: {price}')
        print(f'Đã bán: {sold}')
except Exception as e:
    print("❌ Lỗi khi tải sản phẩm:", e)

driver.quit()
