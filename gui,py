import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import re
import requests
from scapy.all import *
import webbrowser

class CyberSecurityTool:
    def __init__(self, root):
        self.root = root
        self.root.title("أداة التوعية الأمنية - للحماية فقط")
        self.root.geometry("1200x800")

        # شريط التنقل
        self.tab_control = ttk.Notebook(root)
        self.tab_vuln_scan = ttk.Frame(self.tab_control)
        self.tab_wifi_sec = ttk.Frame(self.tab_control)
        self.tab_phishing_detect = ttk.Frame(self.tab_control)
        self.tab_ddos_protect = ttk.Frame(self.tab_control)
        self.tab_learn = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_vuln_scan, text="فحص الثغرات")
        self.tab_control.add(self.tab_wifi_sec, text="حماية الواي فاي")
        self.tab_control.add(self.tab_phishing_detect, text="كشف الصفحات المزيفة")
        self.tab_control.add(self.tab_ddos_protect, text="حماية من DDoS")
        self.tab_control.add(self.tab_learn, text="التعلم")
        self.tab_control.pack(expand=1, fill="both")

        # محتوى علامة التبويب: فحص الثغرات
        ttk.Label(self.tab_vuln_scan, text="ادخل عنوان IP أو نطاق للمسح:", font=("Arial", 12)).pack(pady=10)
        self.target_entry = ttk.Entry(self.tab_vuln_scan, width=50)
        self.target_entry.pack(pady=5)
        self.scan_button = ttk.Button(self.tab_vuln_scan, text="ابدأ الفحص", command=self.run_vuln_scan)
        self.scan_button.pack(pady=10)
        self.scan_output = tk.Text(self.tab_vuln_scan, height=20, width=120)
        self.scan_output.pack(pady=10)

        # محتوى علامة التبويب: حماية الواي فاي
        ttk.Label(self.tab_wifi_sec, text="اختر نوع الفحص:", font=("Arial", 12)).pack(pady=10)
        self.wifi_scan_type = ttk.Combobox(self.tab_wifi_sec, values=["فحص كلمات مرور ضعيفة", "كشف شبكات مزيفة"])
        self.wifi_scan_type.pack(pady=5)
        self.wifi_scan_button = ttk.Button(self.tab_wifi_sec, text="ابدأ الفحص", command=self.run_wifi_scan)
        self.wifi_scan_button.pack(pady=10)
        self.wifi_output = tk.Text(self.tab_wifi_sec, height=20, width=120)
        self.wifi_output.pack(pady=10)

        # محتوى علامة التبويب: كشف الصفحات المزيفة
        ttk.Label(self.tab_phishing_detect, text="ادخل رابط الصفحة للتحقق:", font=("Arial", 12)).pack(pady=10)
        self.url_entry = ttk.Entry(self.tab_phishing_detect, width=50)
        self.url_entry.pack(pady=5)
        self.check_url_button = ttk.Button(self.tab_phishing_detect, text="تحقق", command=self.detect_phishing)
        self.check_url_button.pack(pady=10)
        self.phishing_output = tk.Text(self.tab_phishing_detect, height=20, width=120)
        self.phishing_output.pack(pady=10)

        # محتوى علامة التبويب: حماية من DDoS
        ttk.Label(self.tab_ddos_protect, text="تعليمات الحماية من DDoS", font=("Arial", 12)).pack(pady=10)
        self.ddos_info = tk.Text(self.tab_ddos_protect, height=20, width=120)
        self.ddos_info.insert(tk.END, "1. استخدم جدار حماية (Firewall) لحجب الاتصالات المشبوهة.\n2. قم بتعيين حدود للطلبات (Rate Limiting).\n3. استخدم خدمات مثل Cloudflare لامتصاص الهجمات.")
        self.ddos_info.pack(pady=10)

        # محتوى علامة التبويب: التعلم
        ttk.Label(self.tab_learn, text="مصادر للتعلم الآمن:", font=("Arial", 12)).pack(pady=10)
        self.learn_resources = tk.Listbox(self.tab_learn, width=100, height=15)
        self.learn_resources.insert(1, "دورة CEH (Certified Ethical Hacker)")
        self.learn_resources.insert(2, "كتاب 'Hacking: The Art of Exploitation'")
        self.learn_resources.insert(3, "منصة TryHackMe للتدريب العملي")
        self.learn_resources.pack(pady=10)
        self.learn_button = ttk.Button(self.tab_learn, text="زيارة TryHackMe", command=lambda: webbrowser.open("https://tryhackme.com"))
        self.learn_button.pack(pady=10)

    # دالة فحص الثغرات (باستخدام Nmap)
    def run_vuln_scan(self):
        target = self.target_entry.get()
        if not target:
            messagebox.showerror("خطأ", "الرجاء إدخال عنوان الهدف")
            return

        self.scan_output.delete(1.0, tk.END)
        self.scan_output.insert(tk.END, f"يتم فحص {target}...\n")
        
        try:
            # استخدام Nmap لاكتشاف المنافذ المفتوحة والخدمات
            result = subprocess.run(['nmap', '-sV', '--script=vuln', target], capture_output=True, text=True)
            self.scan_output.insert(tk.END, result.stdout)
        except Exception as e:
            self.scan_output.insert(tk.END, f"حدث خطأ: {str(e)}")

    # دالة فحص الواي فاي
    def run_wifi_scan(self):
        scan_type = self.wifi_scan_type.get()
        self.wifi_output.delete(1.0, tk.END)

        if scan_type == "فحص كلمات مرور ضعيفة":
            self.wifi_output.insert(tk.END, "الكلمات الضعيفة الشائعة:\n- 12345678\n- admin123\n- password\n* تأكد من استخدام كلمة مرور قوية تحتوي على أحرف كبيرة وصغيرة وأرقام ورموز.")

        elif scan_type == "كشف شبكات مزيفة":
            self.wifi_output.insert(tk.END, "للتحقق من الشبكات المزيفة:\n1. تأكد من اسم الشبكة (SSID) الرسمي.\n2. تجنب الاتصال بشبكات مفتوحة (Open Networks).\n3. استخدم تطبيقات مثل 'Fing' لفحص الأجهزة المتصلة.")

    # دالة كشف الصفحات المزيفة
    def detect_phishing(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("خطأ", "الرجاء إدخال الرابط")
            return

        self.phishing_output.delete(1.0, tk.END)
        self.phishing_output.insert(tk.END, f"يتم تحليل {url}...\n")

        try:
            # التحقق من شهادة SSL
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                self.phishing_output.insert(tk.END, "تحذير: الصفحة غير متاحة أو مشبوهة!\n")

            # التحقق من عنوان URL الحقيقي
            parsed_url = requests.utils.urlparse(url)
            self.phishing_output.insert(tk.END, f"الโดمان الحقيقي: {parsed_url.netloc}\n")

            # التحذير من الصفحات المقلدة
            if "login" in url.lower() or "signin" in url.lower():
                self.phishing_output.insert(tk.END, "تحذير: هذا الرابط قد يكون صفحة تسجيل دخول مزيفة!\n")

        except requests.exceptions.RequestException as e:
            self.phishing_output.insert(tk.END, f"خطأ في الاتصال: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberSecurityTool(root)
    root.mainloop()
