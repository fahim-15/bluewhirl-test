from rest_framework import serializers

from .models import CategoryMaster, SubCategoryMaster, KnowledgeBase, QuestionChoice, InquiryDetail


class CategoryMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryMaster
        fields = '__all__'


class SubCategoryMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategoryMaster
        fields = '__all__'


class KnowledgeBaseSerializer(serializers.ModelSerializer):
    choices = serializers.QuestionChoiceSerializer(source='questionchoice_set')

    class Meta:
        model = KnowledgeBase
        fields = '__all__'


class QuestionChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionChoice
        fields = '__all__'


class InquiryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InquiryDetail
        fields = '__all__'
