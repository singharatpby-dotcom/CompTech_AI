import os
from dotenv import load_dotenv
import google.generativeai as genai

def check_api_and_models():
    # โหลด API key จากไฟล์ .env
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("❌ ไม่พบ GOOGLE_API_KEY ในไฟล์ .env")
        return

    # ตั้งค่า API key
    genai.configure(api_key=api_key)

    try:
        print("✅ รายชื่อโมเดลที่ API key นี้สามารถใช้ได้:")
        for m in genai.list_models():
            print("-", m.name, ":", m.supported_generation_methods)

        # ทดสอบเรียก Gemini 1.5 Flash
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content("ทดสอบการเชื่อมต่อ Gemini 1.5 Flash")
        print("\n🎉 ผลลัพธ์จาก Gemini 1.5 Flash:")
        print(response.text)

    except Exception as e:
        print("❌ เกิดข้อผิดพลาด:", str(e))

if __name__ == "__main__":
    check_api_and_models()
