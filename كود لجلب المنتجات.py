#!/usr/bin/env python
# coding: utf-8

# In[12]:



import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[13]:


# إعداد رؤوس HTTP لتجنب الحظر
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# استخدام موقع تدريب مناسب لل scraping
url = "https://webscraper.io/test-sites/e-commerce/allinone"

print("تم إعداد الرؤوس والرابط بنجاح ✅")


# In[14]:


# إرسال طلب HTTP إلى الموقع
try:
    response = requests.get(url, headers=headers, timeout=10)
    print(f"حالة الاتصال: {response.status_code}")
    
    if response.status_code == 200:
        print("تم الاتصال بالموقع بنجاح! ✅")
    else:
        print("فشل الاتصال بالموقع ❌")
        
except Exception as e:
    print(f"حدث خطأ أثناء الاتصال: {e}")


# In[16]:


# تحليل HTML باستخدام BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
print("تم تحليل الصفحة بنجاح ✅")

# عرض جزء من HTML للتحقق
print(soup.prettify()[:500])  # أول 500 حرف فقط


# In[17]:


# البحث عن عناصر المنتجات
products = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
print(f"تم العثور على {len(products)} منتج ✅")

# إذا لم نجد منتجات، نبحث بطرق أخرى
if len(products) == 0:
    products = soup.find_all("div", class_="product")
    print(f"محاولة ثانية: تم العثور على {len(products)} منتج")


# In[18]:


# قائمة لتخزين بيانات المنتجات
products_details = []

for i, product in enumerate(products):
    try:
        # استخراج اسم المنتج
        name_elem = product.find("a", class_="title")
        product_name = name_elem.text.strip() if name_elem else "غير متوفر"
        
        # استخراج السعر
        price_elem = product.find("h4", class_="price")
        product_price = price_elem.text.strip() if price_elem else "غير متوفر"
        
        # استخراج الوصف
        desc_elem = product.find("p", class_="description")
        product_desc = desc_elem.text.strip() if desc_elem else "غير متوفر"
        
        # إضافة إلى القائمة
        products_details.append({
            "رقم المنتج": i+1,
            "اسم المنتج": product_name,
            "السعر": product_price,
            "الوصف": product_desc
        })
        
        print(f"تم معالجة المنتج رقم {i+1} ✅")
        
    except Exception as e:
        print(f"خطأ في المنتج رقم {i+1}: {e}")
        continue

print(f"تم معالجة {len(products_details)} منتج من أصل {len(products)}")


# In[10]:


# قائمة لتخزين بيانات المنتجات
products_details = []

for category in categories:
    # الحصول على عنوان القسم
    category_title = category.find('h2')
    if category_title:
        category_title = category_title.text.strip()
        print(f"جاري معالجة قسم: {category_title}")
        
        # البحث عن المنتجات داخل القسم
        products = category.find_all("div", {'class': 'sc-5be6e5f0-1'})
        
        for product in products:
            # استخراج بيانات المنتج
            product_name = product.find("div", {'class': 'sc-5be6e5f0-2'})
            product_name = product_name.text.strip() if product_name else "غير متوفر"
            
            product_price = product.find("div", {'class': 'sc-5be6e5f0-3'})
            product_price = product_price.text.strip() if product_price else "غير متوفر"
            
            product_brand = product.find("div", {'class': 'sc-5be6e5f0-4'})
            product_brand = product_brand.text.strip() if product_brand else "غير متوفر"
            
            product_rating = product.find("div", {'class': 'sc-5be6e5f0-5'})
            product_rating = product_rating.text.strip() if product_rating else "لا يوجد تقييم"
            
            # إضافة المنتج إلى القائمة
            products_details.append({
                "القسم": category_title,
                "اسم المنتج": product_name,
                "السعر": product_price,
                "الماركة": product_brand,
                "التقييم": product_rating
            })


# In[19]:


# تحويل البيانات إلى DataFrame
if products_details:
    DataSet = pd.DataFrame(products_details)
    
    print("=" * 60)
    print("النتائج النهائية:")
    print("=" * 60)
    
    # عرض DataFrame
    display(DataSet)  # في Jupyter
    
    # عرض إحصائية بسيطة
    print(f"\nإجمالي المنتجات: {len(DataSet)}")
    print(f"أغلى منتج: {DataSet['السعر'].max()}")
    
else:
    print("لم يتم العثور على أي منتجات ❌")


# In[ ]:




