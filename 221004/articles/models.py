from django.db import models

# DB μ€κ³νκΈ° π‘
class Article(models.Model):
    title = models.CharField(max_length=30) # λ¬Έμμ΄ νλ, κΈμμ μ ν: 30
    content = models.TextField() # νμ€νΈ νλ
    created_at = models.DateTimeField(auto_now_add=True) # λ μ§ λ° μκ° νλ, κ°μ²΄ μμ±μ μκ°μΌλ‘ μ€μ 
    updated_at = models.DateTimeField(auto_now=True) # λ μ§ λ° μκ° νλ, κ°μ²΄ μ μ₯μ μκ°μΌλ‘ μλ°μ΄νΈ

# μ€κ³ μ΄ν python3 manage.py makemirations && python3 manage.py migrate μ€ν π‘