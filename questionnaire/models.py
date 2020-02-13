from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CategoryMaster(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class SubCategoryMaster(models.Model):
    category = models.ForeignKey(CategoryMaster, on_delete=models.SET_NULL, null=True)
    subcategory_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subcategory_name


class KnowledgeBase(models.Model):
    category = models.ForeignKey(CategoryMaster, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategoryMaster, on_delete=models.SET_NULL, null=True)
    question = models.TextField()
    parent_question = models.ForeignKey("KnowledgeBase", on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField()


class QuestionChoice(models.Model):
    question = models.ForeignKey(KnowledgeBase, on_delete=models.CASCADE, related_name='rq_question')
    choice = models.CharField(max_length=30)
    next_question = models.ForeignKey(KnowledgeBase, null=True, on_delete=models.SET_NULL,
                                      related_name='rq_next_question')


class CustomerInquiry(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rq_user_agent')

    created_at = models.DateTimeField()


class InquiryDetail(models.Model):
    inquiry = models.ForeignKey(CustomerInquiry, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionChoice,  on_delete=models.CASCADE)

    created_at = models.DateTimeField()



