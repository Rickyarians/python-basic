# format untuk menyisipkan beda tipe data ke dalam string

a = 26
txt = "Ricky sekarang berumur {}"
print(txt.format(a))

# seperti function oper parameter

b = 3
txt1 = "Ricky sekarang berumur {} dan berpengalaman {} tahun"
print(txt1.format(a, b))

# berdasarkan index
txt2 = "Ricky Berpengalaman {1} dan berumur {0}"
print(txt2.format(a, b))