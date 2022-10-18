from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()


class Comment(models.Model):
    # 다대일(N:1) 관계 만들기💡 ForeignKey(to. on_delete, **option)💡
    # -> 댓글(N)은 하나의 게시글(1)을 가진다.
    # -> 게시글(1)은 댓글(N)을 가지지 않거나, 여러 댓글을 가진다.
    # -> related_name: 역참조 이름 설정💡
    # -> on_delete: 필수 인자로, 참조하는 객체를 어떻게 처리할지 설정💡
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=80)