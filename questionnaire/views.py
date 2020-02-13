from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import TimeZone
from questionnaire.models import CategoryMaster, SubCategoryMaster, KnowledgeBase, InquiryDetail
from questionnaire.serializers import CategoryMasterSerializer, SubCategoryMasterSerializer, KnowledgeBaseSerializer, \
    InquiryDetailSerializer


class CategoryMasterView(APIView):

    @staticmethod
    def get(request, category_id=None):
        try:
            if category_id is None:
                category_objs = CategoryMaster.objects.all()
                category_srlzr = CategoryMasterSerializer(category_objs, many=True)

                return Response({'list': category_srlzr.data, 'message': 'List of all categories.',
                                 'code': 200}, status=status.HTTP_200_OK)
            category_obj = CategoryMaster.objects.get(id=category_id)
            category_srlzr = CategoryMasterSerializer(category_obj)

            return Response({'object': category_srlzr.data, 'message': 'Get Category.',
                             'code': 200}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message': 'Something went wrong.', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        try:
            category_srlzr = CategoryMasterSerializer(data=request.data)
            if category_srlzr.is_valid():
                category_srlzr.save()
                return Response({'object': category_srlzr.data, 'message': 'New Category created successfully.',
                                 'code': 201}, status=status.HTTP_201_CREATED)
            return Response({'message': category_srlzr.errors, 'code': 400}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'message': 'Something went wrong.', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)


class SubCategoryMasterView(APIView):

    @staticmethod
    def get(request, category_id=None):
        try:
            if category_id is None:
                category_objs = SubCategoryMaster.objects.all()
            else:
                category_objs = SubCategoryMaster.objects.filter(id=category_id)

            category_srlzr = CategoryMasterSerializer(category_objs, many=True)
            return Response({'list': category_srlzr.data, 'message': 'List of all subcategories.',
                             'code': 200}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message': 'Something went wrong.', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        try:
            category_srlzr = SubCategoryMasterSerializer(data=request.data)
            if category_srlzr.is_valid():
                category_srlzr.save()
                return Response({'object': category_srlzr.data, 'message': 'New SubCategory created successfully.',
                                 'code': 201}, status=status.HTTP_201_CREATED)
            return Response({'message': category_srlzr.errors, 'code': 400}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'message': 'Something went wrong.', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)


class KnowledgeBaseView(APIView):
    @staticmethod
    def get(request, subcategory_id):
        try:
            question_objs = KnowledgeBase.objects.get(subcategory_id=subcategory_id, parent_question=None)

            question_srlzr = KnowledgeBaseSerializer(question_objs)
            return Response({'object': question_srlzr.data, 'message': 'Success.',
                             'code': 200}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message': 'Something went wrong.', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        try:
            if request.user.is_superuser:
                request.data['created_at'] = TimeZone.datetime()
                question_srlzr = KnowledgeBaseSerializer(data=request.data)
                if question_srlzr.is_valid():
                    question_srlzr.save()
                    return Response({'object': question_srlzr.data, 'message': 'New Question added successfully.',
                                     'code': 201}, status=status.HTTP_201_CREATED)
                return Response({'message': question_srlzr.errors, 'code': 400}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'user don\'t have permission', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'message': 'Something went wrong.', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)


class InquiryDetailView(APIView):
    @staticmethod
    def get(request, inquiry_id):
        try:
            inquiries = InquiryDetail.objects.get(inquiry_id=inquiry_id)

            question_srlzr = InquiryDetailSerializer(inquiries)
            return Response({'object': question_srlzr.data, 'message': 'Success.',
                             'code': 200}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message': 'Something went wrong.', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        try:
            request.data['created_at'] = TimeZone.datetime()
            question_srlzr = InquiryDetailSerializer(data=request.data)
            if question_srlzr.is_valid():
                question_srlzr.save()
                return Response({'object': question_srlzr.data, 'message': 'New Question added successfully.',
                                 'code': 201}, status=status.HTTP_201_CREATED)
            return Response({'message': question_srlzr.errors, 'code': 400}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'message': 'Something went wrong.', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)



