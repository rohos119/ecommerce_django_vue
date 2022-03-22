from unittest.util import _MAX_LENGTH
from djongo import models

class Category(models.Model) :
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta :
        ordering = ('name',)

    def __str__(self) :
        return self.name

    def get_absoulte_url(self) :
        return f'/{self.slug}'        
class prdDetailImg(models.Model) :
    prdDetailImg = models.CharField(max_length=500, blank=True)

class prdDetailThumb(models.Model) :
    prdDetailThumb = models.CharField(max_length=500, blank=True)
class Product(models.Model) :
    _id = models.ObjectIdField()
    prdCate = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    prdTitle = models.CharField(max_length=500)
    prdImgUrl = models.CharField(max_length=500)
    # prdImgUrl = models.ImageField(upload_to='uploads/', blank=True, null=True)
    prdImgLink = models.URLField(max_length=500)
    prdOriginPrice = models.DecimalField(max_digits=10, decimal_places=2)
    prdSalePrice = models.DecimalField(max_digits=10, decimal_places=2)
    prdDetailImgs = models.ManyToManyField(prdDetailImg)
    prdDetailThumbs = models.ManyToManyField(prdDetailThumb)
    update = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ['_id','update']

    def __str__(self) :
        return self.title
    
    def get_absolute_url(self) :
        return f'/{self.prdCate.slug}/{self._id}'

    # def get_image(self) :
    #     if self.image :
    #         return 'http://127.0.0.1:8000' + self.prdImgUrl