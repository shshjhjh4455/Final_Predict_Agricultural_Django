from django.shortcuts import render
from django.http import HttpResponse
# from .models import Recommend
import pickle
import joblib
# from .serializers import PredictionMadeSerializer
# from rest_framework import viewsets
# from rest_framework import permissions

# def predict(request):
#     # if request.method == 'POST':
#     #     feature = Recommend.objects.all()
#     #     avr_top = models.FloatField()
#     #     max_top = models.FloatField()
#     #     min_top = models.FloatField()
#     #     rain_top = models.FloatField()
#     #     sun_top = models.FloatField()
#     #     avr_mid = models.FloatField()
#     #     max_mid = models.FloatField()
#     #     min_mid = models.FloatField()
#     #     rain_mid = models.FloatField()
#     #     sun_mid = models.FloatField()
#     #     avr_bot = models.FloatField()
#     #     max_bot = models.FloatField()
#     #     min_bot = models.FloatField()
#     #     rain_bot = models.FloatField()
#     #     sun_bot = models.FloatField()

#     example = [[22.30, 31.20, 14.50, 233.70, 339.280, 17.10, 28.50, 4.40, 177.10, 250.480, 9.30, 20.60, -1.80, 77.50, 246.490]]
#     with open("model/xgb_baechoo_bin_classify_scaler_jinhyeok.pickle", "rb") as s :
#         scaler = pickle.load(s)
#         feature = scaler.transform(scaler)

#     with open('xgb_baechoo_bin_classify_jinhyeok.pickle', 'rb') as f: 
#         model = pickle.load(f)
#         y_p = model.predict(feature)

#     print(y_p)

example = [[22.30, 31.20, 14.50, 233.70, 339.280, 17.10, 28.50, 4.40, 177.10, 250.480, 9.30, 20.60, -1.80, 77.50, 246.490]]
with open("../model/xgb_baechoo_bin_classify_scaler_jinhyeok.pkl", "rb") as s :
    scaler = joblib.load(s)
    feature = scaler.transform(example)

with open('../model/xgb_baechoo_bin_classify_jinhyeok.pickle', 'rb') as f: 
    model = pickle.load(f)
    y_p = model.predict(feature)

print(y_p)
    # context = {"feature" : feature}
    # return render(request, "recommend/feature.html", context)





# @login_required(login_url='common:login')
# def question_modify(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     if request.method == "POST":
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.modify_date = timezone.now()  # 수정일시 저장
#             question.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = QuestionForm(instance=question)
#     context = {'form': form}
#     return render(request, 'pybo/question_form.html', context)


# @login_required(login_url='common:login')
# def question_delete(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     question.delete()
#     return redirect('pybo:index')


# @login_required(login_url='common:login')
# def question_vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user == question.author:
#         messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
#     else:
#         question.voter.add(request.user)
#     return redirect('pybo:detail', question_id=question.id)


# class PredictionMadeViewSet(viewsets.ModelViewSet):
#     queryset = PredictionMade.objects.all()
#     serializer_class = PredictionMadeSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save()

#     def perform_update(self, serializer):
#         serializer.save()

#     def perform_destroy(self, serializer):
#         serializer.delete()

#     def get_queryset(self):
#         queryset = PredictionMade.objects.all()
#         avr1 = self.request.query_params.get("avr1", None)
#         max1 = self.request.query_params.get("max1", None)
#         min1 = self.request.query_params.get("min1", None)
#         rain1 = self.request.query_params.get("rain1", None)
#         sun1 = self.request.query_params.get("sun1", None)
#         avr2 = self.request.query_params.get("avr2", None)
#         max2 = self.request.query_params.get("max2", None)
#         min2 = self.request.query_params.get("min2", None)
#         rain2 = self.request.query_params.get("rain2", None)
#         sun2 = self.request.query_params.get("sun2", None)
#         avr3 = self.request.query_params.get("avr3", None)
#         max3 = self.request.query_params.get("max3", None)
#         min3 = self.request.query_params.get("min3", None)
#         rain3 = self.request.query_params.get("rain3", None)
#         sun3 = self.request.query_params.get("sun3", None)
#         if avr1 is not None:
#             queryset = queryset.filter(avr1=avr1)
#         if max1 is not None:
#             queryset = queryset.filter(max1=max1)
#         if min1 is not None:
#             queryset = queryset.filter(min1=min1)
#         if rain1 is not None:
#             queryset = queryset.filter(rain1=rain1)
#         if sun1 is not None:
#             queryset = queryset.filter(sun1=sun1)
#         if avr2 is not None:
#             queryset = queryset.filter(avr2=avr2)
#         if max2 is not None:
#             queryset = queryset.filter(max2=max2)
#         if min2 is not None:
#             queryset = queryset.filter(min2=min2)
#         if rain2 is not None:
#             queryset = queryset.filter(rain2=rain2)
#         if sun2 is not None:
#             queryset = queryset.filter(sun2=sun2)
#         if avr3 is not None:
#             queryset = queryset.filter(avr3=avr3)
#         if max3 is not None:
#             queryset = queryset.filter(max3=max3)
#         if min3 is not None:
#             queryset = queryset.filter(min3=min3)
#         if rain3 is not None:
#             queryset = queryset.filter(rain3=rain3)
#         if sun3 is not None:
#             queryset = queryset.filter(sun3=sun3)
#         return queryset

#     def get_serializer_class(self):
#         if self.action == "list":
#             return PredictionMadeSerializer
#         elif self.action == "create":
#             return PredictionMadeSerializer
#         elif self.action == "retrieve":
#             return PredictionMadeSerializer
#         elif self.action == "update":
#             return PredictionMadeSerializer
#         elif self.action == "partial_update":
#             return PredictionMadeSerializer
#         elif self.action == "destroy":
#             return PredictionMadeSerializer

#     def get_permissions(self):
#         if self.action == "list":
#             return [permissions.AllowAny()]
#         elif self.action == "create":
#             return [permissions.AllowAny()]
#         elif self.action == "retrieve":
#             return [permissions.AllowAny()]
#         elif self.action == "update":
#             return [permissions.AllowAny()]
#         elif self.action == "partial_update":
#             return [permissions.AllowAny()]
#         elif self.action == "destroy":
#             return [permissions.AllowAny()]
#         return [permissions.IsAuthenticatedOrReadOnly()]

#     def get_serializer_context(self):
#         context = super(PredictionMadeViewSet, self).get_serializer_context()
#         context.update({"request": self.request})
#         return context
