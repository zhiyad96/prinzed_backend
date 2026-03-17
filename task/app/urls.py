from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (MarketingSolutionView,PortfolioView,Serviceview,Coomessageview,Teammembersview,Creativeview,Desinglistview,Reviewview,coreserviceview )



urlpatterns = [

    path("marketing_solutions/", MarketingSolutionView.as_view()),
    path("marketing_solutions/<int:id>/", MarketingSolutionView.as_view()),

    path("portfolios/", PortfolioView.as_view()),
    path("portfolios/<int:id>/", PortfolioView.as_view()),

    path("services/", Serviceview.as_view()),
    path("services/<int:id>/", Serviceview.as_view()),

    path("coo_message/", Coomessageview.as_view()),
    path("coo_message/<int:id>/", Coomessageview.as_view()),

     path("teammembers/", Teammembersview.as_view()),
    path("teammembers/<int:id>/", Teammembersview.as_view()),

     path("creative/", Creativeview.as_view()),
    path("creative/<int:id>/", Creativeview.as_view()),

    path("designlist/", Desinglistview.as_view()),
    path("designlist/<int:id>/", Desinglistview.as_view()),
    
    path("reviews/", Reviewview.as_view()),
    path("reviews/<int:id>/", Reviewview.as_view()),
    
    path("coreservice/", coreserviceview.as_view()),
    path("coreservice/<int:id>/", coreserviceview.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
