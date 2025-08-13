from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Portfolio, Media
from .forms import PortfolioForm, MediaFormSet


class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'
    context_object_name = 'portfolios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        developer_ids = [1, 2, 3, 4, 5]  #треба не забути вставити справжні id розробників
        context['developer_portfolios'] = Portfolio.objects.filter(user__id__in=developer_ids)
        context['other_portfolios'] = Portfolio.objects.exclude(user__id__in=developer_ids)
        return context


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_details.html'
    context_object_name = 'portfolio'


class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio/portfolio_create.html'
    success_url = reverse_lazy('portfolio:portfolio_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['media_formset'] = MediaFormSet(self.request.POST, self.request.FILES)
        else:
            context['media_formset'] = MediaFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        media_formset = context['media_formset']

        if media_formset.is_valid():
            form.instance.user = self.request.user
            self.object = form.save()
            media_formset.instance = self.object
            media_formset.save()
            messages.success(self.request, 'Портфоліо успішно створено!')
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class PortfolioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio/portfolio_create.html'
    success_url = reverse_lazy('portfolio:portfolio_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['media_formset'] = MediaFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['media_formset'] = MediaFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        media_formset = context['media_formset']

        if media_formset.is_valid():
            self.object = form.save()
            media_formset.instance = self.object
            media_formset.save()
            messages.success(self.request, 'Портфоліо успішно оновлено!')
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        portfolio = self.get_object()
        return self.request.user == portfolio.user or self.request.user.is_staff


class PortfolioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Portfolio
    template_name = 'portfolio/portfolio_confirm_delete.html'
    success_url = reverse_lazy('portfolio:portfolio_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Портфоліо успішно видалено!')
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        portfolio = self.get_object()
        return self.request.user == portfolio.user or self.request.user.is_staff
