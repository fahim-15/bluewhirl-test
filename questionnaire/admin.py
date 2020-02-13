from django.contrib import admin

# Register your models here.
from .models import CategoryMaster, SubCategoryMaster, KnowledgeBase, QuestionChoice, InquiryDetail, CustomerInquiry

admin.site.register(CategoryMaster)
admin.site.register(SubCategoryMaster)
admin.site.register(KnowledgeBase)
admin.site.register(QuestionChoice)
admin.site.register(CustomerInquiry)
admin.site.register(InquiryDetail)

