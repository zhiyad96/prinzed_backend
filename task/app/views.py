
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (MarketingSolution,Portfolio,Service,Coomessage,Teammembers,Creative,Desinglist,Reviews,coreservice )
from .serializers import (Marketingsolutionserializer,Portfolioserializer,Serviceserializer,CooMessageserializer,TeamMembersserializer,Creativeserializer,Desinglistserializer ,Reviewserializer,coreserviceserializer )
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser




        # =================================marketingview=====================


class MarketingSolutionView(APIView):

    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        solutions = MarketingSolution.objects.all()
        serializer = Marketingsolutionserializer(solutions, many=True, context={"request": request})
        return Response(serializer.data)



    def post(self, request):
        serializer = Marketingsolutionserializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def put(self, request, id):
        try:
            solution = MarketingSolution.objects.get(id=id)
        except MarketingSolution.DoesNotExist:
            return Response({"error": "Solution not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Marketingsolutionserializer(solution, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, id):
        try:
            solution = MarketingSolution.objects.get(id=id)
        except MarketingSolution.DoesNotExist:
            return Response({"error": "Solution not found"}, status=status.HTTP_404_NOT_FOUND)

        solution.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    # ===============================portfolioview=====================
    
class PortfolioView(APIView):

    parser_classes = [MultiPartParser, FormParser, JSONParser]


    def get(self, request):
        portfolio = Portfolio.objects.all()
        serializer = Portfolioserializer(portfolio, many=True, context={"request": request})
        return Response(serializer.data)


    def post(self, request):
        serializer = Portfolioserializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):
        try:
            portfolio = Portfolio.objects.get(id=id)
        except Portfolio.DoesNotExist:
            return Response({"error": "Portfolio not found"}, status=404)
        serializer = Portfolioserializer( portfolio, data=request.data,partial=True,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, id):
        try:
            portfolio = Portfolio.objects.get(id=id)
        except Portfolio.DoesNotExist:
            return Response({"error": "Portfolio not found"}, status=404)
        portfolio.delete()
        return Response({"message": "Deleted successfully"}, status=204)
    
    
# ====================================servieceview==============================


class Serviceview(APIView):

    parser_classes = [MultiPartParser, FormParser, JSONParser]


    def get(self, request):
        services = Service.objects.all()
        serializer = Serviceserializer(services, many=True, context={"request": request})
        return Response(serializer.data)


    def post(self, request):
        serializer = Serviceserializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):
        try:
            service = Service.objects.get(id=id)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=404)
        serializer = Serviceserializer(service,data=request.data,partial=True,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, id):
        try:
            service = Service.objects.get(id=id)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=404)
        service.delete()
        return Response({"message": "Deleted successfully"}, status=204)
    
    # =====================================Coomessageview===========================
    
class Coomessageview(APIView):

    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        message = Coomessage.objects.all()
        serializer = CooMessageserializer(message, many=True, context={"request": request})
        return Response(serializer.data)


    def post(self, request):
        serializer = CooMessageserializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):
        try:
            message = Coomessage.objects.get(id=id)
        except Coomessage.DoesNotExist:
            return Response({"error": "Message not found"}, status=404)
        serializer = CooMessageserializer( message,data=request.data,partial=True,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, id):
        try:
            message = Coomessage.objects.get(id=id)
        except Coomessage.DoesNotExist:
            return Response({"error": "Message not found"}, status=404)
        message.delete()
        return Response({"message": "Deleted successfully"}, status=204)
    
    
    # ================================Teammembersview================================
    
    
class Teammembersview(APIView):

    parser_classes = [MultiPartParser, FormParser, JSONParser]


    def get(self, request):
        members = Teammembers.objects.all()
        serializer = TeamMembersserializer( members, many=True, context={"request": request})
        return Response(serializer.data)


    def post(self, request):
        serializer = TeamMembersserializer( data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):
        try:
            member = Teammembers.objects.get(id=id)
        except Teammembers.DoesNotExist:
            return Response({"error": "Member not found"}, status=404)
        serializer = TeamMembersserializer( member,data=request.data,partial=True,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, id):
        try:
            member = Teammembers.objects.get(id=id)
        except Teammembers.DoesNotExist:
            return Response({"error": "Member not found"}, status=404)
        member.delete()
        return Response({"message": "Deleted successfully"}, status=204)
    
    
# =====================creative view =========================


class Creativeview(APIView):

    parser_classes = [MultiPartParser, FormParser, JSONParser]


    def get(self, request):
        creative = Creative.objects.all()
        serializer = Creativeserializer( creative, many=True, context={"request": request} )
        return Response(serializer.data)


    def post(self, request):
        serializer = Creativeserializer( data=request.data, context={"request": request} )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):
        try:
            creative = Creative.objects.get(id=id)
        except Creative.DoesNotExist:
            return Response({"error": "Creative not found"}, status=404)
        serializer = Creativeserializer( creative,data=request.data,partial=True,context={"request": request} )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, id):
        try:
            creative = Creative.objects.get(id=id)
        except Creative.DoesNotExist:
            return Response({"error": "Creative not found"}, status=404)
        creative.delete()
        return Response({"message": "Deleted successfully"}, status=204)
    
    
    # ===============================Desinglist view=======================
    
    
class Desinglistview(APIView):

    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        design = Desinglist.objects.all()
        serializer = Desinglistserializer( design, many=True, context={"request": request} )
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = Desinglistserializer( data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):
        try:
            design = Desinglist.objects.get(id=id)
        except Desinglist.DoesNotExist:
            return Response({"error": "Design not found"}, status=404)
        serializer = Desinglistserializer( design, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, id):
        try:
            design = Desinglist.objects.get(id=id)
        except Desinglist.DoesNotExist:
            return Response({"error": "Design not found"}, status=404)
        design.delete()
        return Response({"message": "Deleted successfully"}, status=204)
    
    # ===============================review section ====================
    
class Reviewview(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        reviews = Reviews.objects.all()
        serializer = Reviewserializer(reviews, many=True, context={"request": request})
        return Response(serializer.data)


    def post(self, request):
        serializer = Reviewserializer(data=request.data ,context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        try:
            review = Reviews.objects.get(id=id)
        except Reviews.DoesNotExist:
            return Response({"error": "Review not found"}, status=404)
        serializer = Reviewserializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, id):
        try:
            review = Reviews.objects.get(id=id)
        except Reviews.DoesNotExist:
            return Response({"error": "Review not found"}, status=404)
        review.delete()
        return Response({"message": "Deleted successfully"}, status=204)
    
    
    
class coreserviceview(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        coreservices = coreservice.objects.all()
        serializer = coreserviceserializer(coreservices, many=True, context={"request": request})
        return Response(serializer.data)


    def post(self, request):
        serializer = coreserviceserializer(data=request.data ,context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        try:
            Service = coreservice.objects.get(id=id)
        except coreservice.DoesNotExist:
            return Response({"error": "Review not found"}, status=404)
        serializer = coreserviceserializer(Service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, id):
        try:
            service = coreservice.objects.get(id=id)
        except coreservice.DoesNotExist:
            return Response({"error": "Review not found"}, status=404)
        service.delete()
        return Response({"message": "Deleted successfully"}, status=204)