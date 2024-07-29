from django.db import models

# Create your models here.
# model을 database에 저장하지 않음
# 다른 model에서 재사용하기 위한 model


class CommonModel(models.Model):
    """Common Mode Definition"""

    # auto_now_add는 필드의 값을 해당 object가 처음 생성되었을 때 시간으로 설정
    created_at = models.DateTimeField(auto_now_add=True)
    # object가 저장될 때마다 해당 필드를 현재 date로 설정
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract = True 이면 Django가 이 model을 봐도
        # 데이터베이스에 저장하지 않음
        abstract = True
