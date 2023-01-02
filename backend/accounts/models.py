from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, nickname, name, location, area, phone, password=None):
        if not email:
            raise ValueError("must have user email")
        if not nickname:
            raise ValueError("must have user nickname")
        if not name:
            raise ValueError("must have user name")
        if not location:
            raise ValueError("must have user location")
        if not area:
            raise ValueError("must have user area")
        if not phone:
            raise ValueError("must have user phone number")

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            name=name,
            location=location,
            area=area,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, nickname, name, password=None):
        user = self.create_user(password=password, nickname=nickname, name=name)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    location_choice = (
        ("Seoul", "서울특별시"),
        ("Busan", "부산광역시"),
        ("Daegu", "대구광역시"),
        ("Incheon", "인천광역시"),
        ("Gwangju", "광주광역시"),
        ("Daejeon", "대전광역시"),
        ("Ulsan", "울산광역시"),
        ("Sejong", "세종특별자치시"),
        ("Gyeonggi", "경기도"),
        ("Gwangwon", "강원도"),
        ("Chungcheong_north", "충청북도"),
        ("Chungcheong_south", "충청남도"),
        ("Jeolla_north", "전라북도"),
        ("Jeolla_south", "전라남도"),
        ("Gyeongsang_north", "경상북도"),
        ("Gyeongsang_south", "경상남도"),
        ("Jeju", "제주도"),
    )

    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        default="", max_length=100, null=False, blank=False, unique=True
    )
    nickname = models.CharField(
        default="", max_length=100, null=False, blank=False, unique=True
    )
    name = models.CharField(default="", max_length=100, null=False, blank=False)
    location = models.CharField(
        default="서울특별시",
        max_length=100,
        null=False,
        blank=False,
        unique=False,
        choices=location_choice,
    )
    area = models.IntegerField(default=0, null=False, blank=False, unique=False)
    phoneNumberRegex = RegexValidator(
        regex=r"^01([0|1|6|7|8|9]?)([0-9]{3,4})([0-9]{4})$"
    )
    phone = models.CharField(
        validators=[phoneNumberRegex],
        default="",
        max_length=13,
        null=False,
        blank=False,
        unique=True,
    )

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = "nickname"
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ["email", "name", "location", "area", "phone"]

    def __str__(self):
        return self.nickname
