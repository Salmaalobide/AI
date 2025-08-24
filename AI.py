#!/usr/bin/env python
# coding: utf-8

# In[1]:


# استيراد المكتبات الأساسية
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# In[11]:



data = pd.read_csv("C:/Users/Salma/Downloads/heart.csv")

# عرض أول 5 صفوف من البيانات
print("أول 5 سجلات في البيانات:")
display(data.head())




# In[12]:


# فصل الميزات (Features) عن المتغير الهدف (Target)
X = data.drop('target', axis=1)  # كل الأعمدة ما عدا الهدف
y = data['target']  # عمود الهدف فقط

# تقسيم البيانات إلى مجموعتي تدريب واختبار (70% تدريب، 30% اختبار)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# عرض أبعاد البيانات بعد التقسيم
print("أبعاد بيانات التدريب:", X_train.shape)
print("أبعاد بيانات الاختبار:", X_test.shape)


# In[13]:


# إنشاء نموذج شجرة القرار
model = DecisionTreeClassifier(random_state=42)

# تدريب النموذج على بيانات التدريب
model.fit(X_train, y_train)

print("تم تدريب النموذج بنجاح!")


# In[14]:


# التنبؤ على بيانات الاختبار
predictions = model.predict(X_test)

# حساب دقة النموذج
accuracy = accuracy_score(y_test, predictions)
print(f"دقة النموذج: {accuracy:.2%}")

# عرض مصفوفة الارتباك
print("\nمصفوفة الارتباك:")
print(confusion_matrix(y_test, predictions))


# In[15]:


# تفسير مصفوفة الارتباك
conf_matrix = confusion_matrix(y_test, predictions)
print("\nتفسير مصفوفة الارتباك:")
print(f"القيم الحقيقية السلبية (True Negatives): {conf_matrix[0][0]}")
print(f"القيم الإيجابية الكاذبة (False Positives): {conf_matrix[0][1]}")
print(f"القيم السلبية الكاذبة (False Negatives): {conf_matrix[1][0]}")
print(f"القيم الحقيقية الإيجابية (True Positives): {conf_matrix[1][1]}")


# In[ ]:




