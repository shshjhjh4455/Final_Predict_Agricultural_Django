from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, nickname, name, location, area, password=None):
        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        if not name:
            raise ValueError('must have user name')
        if not location:
            raise ValueError('must have user location')
        if not area:
            raise ValueError('must have user area')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            name = name,
            location = location,
            area = area,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, email, nickname, name, password=None):
        user = self.create_user(
            email,
            password = password,
            nickname = nickname,
            name = name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

location = (
    ("서울", "서울"),
    ("경기", "경기"),
    ("인천", "인천"),
    ("강원", "강원"),
    ("충북", "충북"),
    ("충남", "충남"),
    ("대전", "대전"),
    ("세종", "세종"),
    ("전북", "전북"),
    ("전남", "전남"),
    ("광주", "광주"),
    ("대구", "대구"),
    ("경북", "경북"),
    ("경남", "경남"),
    ("부산", "부산"),
    ("울산", "울산"),
    ("제주", "제주"),
    ("해외", "해외"),
)

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)
    location = models.CharField(default="서울", max_length=100, null=False, blank=False, unique=True, choices=location)
    area = models.FloatField(default=0, max_length=50, null=False, blank=False, unique=False)
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'nickname'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'name', "location", "area"]

    def __str__(self):
        return self.nickname