from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.fields.related import ForeignKey


# ユーザ作成管理マネージャーカスタマイズ
class UserManager(BaseUserManager):

    def create_user(self, user_name, email, password=None, **extra_fields):

        if not email:
            raise ValueError('email is must')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, user_name='',):
        user = self.create_user(user_name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# ユーザー
class User(AbstractBaseUser, PermissionsMixin):

    user_name = models.CharField(
        'user_name',
        max_length=150,
        blank=True,
        null=True,
        unique=True,
    )
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.email


# カテゴリモデル
class Category(models.Model):
    category_id = models.AutoField(
        'category_id',
        primary_key=True,
        db_column='category_id')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='user_category')
    order = models.IntegerField(default=9999, db_column='order', )
    name = models.CharField(
        max_length=50,
        blank=True,
        null=False,
        default='',
        db_column='name')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category_id) + ' ' + self.name

    class Meta:
        db_table = 'category'


# レシピ画像アップロード関数
def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['recipe_images', str(instance.user.id) + '_'+str(instance.recipe_title) + str(".")+str(ext)])


# レシピモデル
class Recipe(models.Model):
    recipe_id = models.AutoField(
        'recipe_id', primary_key=True, db_column='recipe_id')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        db_column='user_id', related_name='user_recipe')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='category_id')

    recipe_title = models.CharField(max_length=100)
    recipe_image = models.ImageField(
        blank=True, null=True, upload_to=upload_path)
    external_url = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'recipe'


# 材料モデル
class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    recipe = ForeignKey(Recipe, on_delete=models.CASCADE,
                        db_column='recipe_id')
    material_name = models.CharField(max_length=100)
    amount = models.FloatField()
    unit = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material_name

    class Meta:
        db_table = 'material'


# 手順モデル
class Procedure(models.Model):
    procedure_id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, db_column='recipe_id')
    order = models.IntegerField(default=0)
    contents = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order) + self.recipe.recipe_title

    class Meta:
        db_table = 'procedure'


# メモモデル
class Memo(models.Model):
    memo_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        db_column='user_id', related_name='user_memo')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.memo_id) + ' ' + self.user.user_name

    class Meta:
        db_table = 'memo'


# メモ選択レシピモデル
class SelectedRecipe(models.Model):
    selected_recipe_id = models.AutoField(primary_key=True)
    memo = models.ForeignKey(
        Memo, on_delete=models.CASCADE, db_column='memo_id')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, db_column='recipe_id')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.memo.memo_id) + ' ' + self.recipe.recipe_title

    class Meta:
        db_table = 'selected_recipe'
