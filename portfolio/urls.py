from django.urls import path
from .views import PortfolioListView, PortfolioDetailView, PortfolioCreateView, PortfolioUpdateView, PortfolioDeleteView

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio_list'),
    path('<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('create/', PortfolioCreateView.as_view(), name='portfolio_create'),
    path('<int:pk>/update/', PortfolioUpdateView.as_view(), name='portfolio_update'),
    path('<int:pk>/delete/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
]
