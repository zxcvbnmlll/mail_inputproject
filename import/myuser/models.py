from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):  # 이 함수 추가
        return self.username  # User object 대신 나타낼 문자
    # 저장되는 시점의 시간을 자동으로 삽입해준다.

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'test_user'